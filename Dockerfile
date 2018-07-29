FROM python:3.6.2

WORKDIR /root
COPY . /root
CMD [ "python", "run.py" ]