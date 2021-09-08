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


producer = KafkaProducer(bootstrap_servers='10.244.0.17:9092')

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
    for i in range(100):
        sys.stdout.write('-------stdout-----')
        print('----------------p--------------')
        time.sleep(200)
        connect_to_kafka("10.244.0.17:9092")
