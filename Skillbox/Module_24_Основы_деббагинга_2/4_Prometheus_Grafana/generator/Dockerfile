FROM python:3-alpine

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ADD generator_events.py /var/server/generator.py

CMD /var/server/generator.py