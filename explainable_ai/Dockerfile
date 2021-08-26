FROM python:3.8.1
RUN mkdir -p /opt/explainable_ai
WORKDIR /opt/explainable_ai
ADD . /opt/explainable_ai
RUN pip3 install -r requirements.txt
CMD python3 online/app.py