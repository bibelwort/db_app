FROM python:3.9

WORKDIR /db_app

ADD app.py

RUN apt-get update && pip install --upgrade pip

RUN pip install git+https://github.com/bibelwort/example_package.git@main

ENTRYPOINT ["python", "app.py"]