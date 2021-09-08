FROM python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install vim -y

COPY . .

CMD [ "python", "producer.py" ]
