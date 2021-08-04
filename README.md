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
curl --location --request POST '<server_address>/api/to_md' \
--header 'Content-Type: application/json' \
--data-raw '{
    "latex": "\\documentclass[12pt]{article}\n\\begin{document}\nHello world!\n$$Hello world!$$ %math mode \n\\end{document}"
}'
```

# Deploying on Google Cloud Run

## Building a docker image
```
gcloud config set account abc@sophize.org 
gcloud config set project md-convert-server
gcloud builds submit --tag gcr.io/md-convert-server/md-convert-server
```

Find it container registry:
https://console.cloud.google.com/gcr/images/md-convert-server

## Deploy
`https://console.cloud.google.com/run?project=md-convert-server`
OR 
Click 'EDIT AND DEPLOY NEW VERSION' here:
`https://console.cloud.google.com/run/detail/us-central1/md-convert-cloud-run`
