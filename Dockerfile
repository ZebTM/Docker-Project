FROM python:3
ADD requirements.txt /
ADD IF.txt /
ADD Limerick-1.txt /
RUN pip install -r requirements.txt
ADD main.py /
RUN mkdir /home/output/

CMD [ "python", "./main.py" ]