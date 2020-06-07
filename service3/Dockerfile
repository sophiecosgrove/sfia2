FROM python:latest

RUN mkdir /opt/sfia2

COPY . /opt/sfia2/

WORKDIR /opt/sfia2/

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]