from flask import Flask, request

from text_processing import latex_to_md

# App configuration
app = Flask(__name__)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


def _to_md(latex: str):
    v = latex_to_md(latex)
    if not v:
        v = 'Latex To Markdown Conversion Failed'
    return {'v': v}

@app.route('/api/to_md', methods=['POST'])
def to_md():
    return _to_md(request.json['latex'])

@app.route('/api/test')
def test():
    return 'success'

if __name__ == '__main__':
    app.run(debug=True, port=10001)
