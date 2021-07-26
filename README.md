# md-convert-server

Converts latex input to Markdown. 

## Running the server locally

```
python -m venv env
source env/bin/activate OR .\env\Scripts\activate
pip install  -r requirements.txt
python app.py
```

## Sample request

```
curl --location --request POST 'http://localhost:10001/api/to_md' \
--header 'Content-Type: application/json' \
--data-raw '{
    "latex": "\\documentclass[12pt]{article}\n\\begin{document}\nHello world!\n$$Hello world!$$ %math mode \n\\end{document}"
}'
```
