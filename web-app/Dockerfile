FROM ubuntu

RUN apt-get update
RUN apt-get install curl -y
RUN apt-get install python -y
RUN apt-get install python-pip -y

RUN pip install flask 
RUN pip install flask-mysql 

WORKDIR /opt/source-code

COPY . /opt/source-code

ENTRYPOINT [ "python" ]
CMD [ "app.py" ] 
EXPOSE 3000
