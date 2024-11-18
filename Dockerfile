FROM python:3.13-slim-bullseye

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./src /app/
COPY ./whc-sites.csv /data/

WORKDIR "/app"
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]