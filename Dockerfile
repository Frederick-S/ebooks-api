FROM python:3.8-slim

WORKDIR /app

ADD . /app

RUN pip install gunicorn
RUN python setup.py install

EXPOSE 5000

CMD [ "gunicorn", "-c", "gunicorn.conf.py", "app:app" ]