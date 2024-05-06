FROM python:3.11

WORKDIR /app

RUN apt update
RUN apt install -y xclip

COPY . .
RUN pip install -r requirements.txt
RUN pip install -e .