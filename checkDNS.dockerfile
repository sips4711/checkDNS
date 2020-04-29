FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt /usr/local/src/
RUN pip install --no-cache-dir -r /usr/local/src/requirements.txt


ENTRYPOINT [ "python", "./checkDNS.py" ]