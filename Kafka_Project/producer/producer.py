import os
import sys
import random
import time
from kafka import KafkaProducer,KafkaClient
from prometheus_client import start_http_server, Summary, Counter



def connect_to_kafka(bootstrap_servers):
    try:
        connection = KafkaClient(bootstrap_servers=bootstrap_servers)
        print('Connected to Kafka')
        return connection.bootstrap_connected()
    except:
        return False


producer = KafkaProducer(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])

messeges_out = Counter('messeges_out', 'number of messages sent to kafka')


def main():
    for i in range(10000):
        producer.send('simple-one', b'random message-plap')
        messeges_out.inc()
        sys.stdout.write('sended message\n')
        time.sleep(2)

if __name__ == '__main__':
    start_http_server(9101)
    main()
