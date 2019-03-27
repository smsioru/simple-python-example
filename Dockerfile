FROM python:3.5

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r ./requirements.txt

COPY ./simple-example.py /usr/src/app/simple-example.py

CMD [ "python", "./simple-example.py" ]
