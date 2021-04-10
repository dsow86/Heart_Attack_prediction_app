FROM python:3.8
RUN apt-get update -y && apt-get install -y build-essential
COPY . /usr/ML/app
EXPOSE 5000
WORKDIR /usr/ML/app
RUN pip3 install --upgrade pip
RUN pip3 install pandas sklearn numpy tensorflow==2.4.1 flask keras==2.4.3
CMD python app.py