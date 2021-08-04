"""Functions for processing data from text"""
from os import replace
import re
import pypandoc

# Map for replacement of features not supported by Katex.
TAG_REPLACEMENT_MAP = {
    '\\mbox': '\\text',
    '\\hbox': '\\text',
    '\\intertext': '\\text', # Causes alignment issues. See BrunsPureSieve.
    '\\mathbbmss': '\\mathbb',
    '\\nonumber': '', # Can cause alignment issues?
    '\\notag': '', # Can cause alignment issues?
    '\\xspace': '', # Can cause alignment issues?
    '\\operatornamewithlimits': '\\operatorname*',
    '\\ensuremath': '\\relax',
    # this is inaccurate, should be supported in next katex release
    # https://github.com/KaTeX/KaTeX/pull/2429
    '\\varprojlim': '\\lim_\\leftarrow',
    #  hack, should be supported in next katex release https://github.com/KaTeX/KaTeX/pull/2369
    r'{split}': r'{aligned}', # ProofOfMinkowskisBound
}

def latex_to_md(latex_str: str, doc: str=None):
    """Convert from LaTeX to markdown."""
    try:
        latex_str = _latex_preprocess(latex_str)
        # For the full list of extensions run `pandoc --list-extensions=markdown`
        # -header_attributes are needed for \begin{lemma}?
        output_format =  'markdown-fenced_divs-raw_html-native_divs-header_attributes'
        md_text = pypandoc.convert_text(latex_str, output_format, 'latex', extra_args=['--wrap=none']).strip()
        for txt in TAG_REPLACEMENT_MAP:
            md_text = md_text.replace(txt, TAG_REPLACEMENT_MAP[txt])
        if '\\label' in md_text: # KaTeX can't handle \label
            md_text = re.sub(r'\\label\s*\{[^\}]*\}\s*', '', md_text)
        return md_text
    except Exception as e:
        return str(e)


def _latex_preprocess(latex_str: str):
    """Attach Planetmath Latex commands and neatly print bibiliography."""
    # Add a subsection (h2) named 'References' for bibliography.
    latex_str = latex_str.replace('\\begin{thebibliography}', r'\n\subsection{References}\n\begin{thebibliography}')
    latex_str = latex_str.replace('\\bibitem', '\n\n\\bibitem') # Create space between each item.
    # Remove 'thebibiliography' parameter that typically indicates max number of references.
    latex_str = re.sub(r'\\begin\s*\{thebibliography\}\s*\{[^}]*\}', r'\\begin{thebibliography}', latex_str)
    return latex_str
