# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster


RUN apt update
RUN apt upgrade
RUN apt install -y pandoc pandoc-citeproc 
# texlive-full fig2dev make wget git
RUN apt-get clean -y

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
