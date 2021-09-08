import os
import sys
import time
from kafka import KafkaConsumer
from prometheus_client import start_http_server, Summary, Counter

messages_in = Counter('messages_in', 'number of messages sent to kafka')

def main():
    try:
        consumer =  KafkaConsumer(os.environ['TOPIC_NAME'], bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])
    except:
        sys.stdout.write('Failed connecting to kafka\n')
        sys.exit(1)

    for message in consumer:
        print("{}:{}:{}: key={} value={}".format(message.topic, message.partition, message.offset, message.key,message.value))
        messages_in.inc()

if __name__ == '__main__':
    start_http_server(9101)
    sys.stdout.write('service is up!\n')
    main()
