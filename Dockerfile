FROM python:3
WORKDIR /app
ADD . /app
RUN pip install gunicorn
RUN python setup.py install
EXPOSE 5000
CMD ["gunicorn", "-c", "gunicorn.py", "app:app"]