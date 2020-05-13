FROM ubuntu

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install python3-pip -y

RUN pip3 install requests

COPY hello-google.py /app/hello-google.py

CMD [ "python3", "/app/hello-google.py" ]