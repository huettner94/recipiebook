FROM python:3-alpine

RUN pip install --no-cache-dir virtualenv

RUN python3 -m virtualenv -p python3 /env
ENV PATH /env/bin:$PATH

ADD requirements.txt /app/requirements.txt
RUN /env/bin/pip install --upgrade pip && /env/bin/pip install -r /app/requirements.txt
COPY recipiebook/ /app
COPY start.sh /app/start.sh

WORKDIR /app
CMD /app/start.sh