FROM python:3.10

ADD main.py .
ADD ./df_contents  .

RUN pip install tweepy requests

CMD ["python", "./main.py"]
