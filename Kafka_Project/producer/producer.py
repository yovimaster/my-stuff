import os
import sys
import time
from kafka import KafkaProducer
from prometheus_client import start_http_server, Summary, Counter

messeges_out = Counter('messeges_out', 'number of messages sent to kafka')

def main():
    try:
        producer = KafkaProducer(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])
    except:
        sys.stdout.write('Failed connecting to kafka\n')
        sys.exit(1)

    for i in range(1000):
        producer.send(os.environ['TOPIC_NAME'], b'Another kafka meesage')
        messeges_out.inc()
        sys.stdout.write('sended message\n')
        time.sleep(1)

if __name__ == '__main__':
    start_http_server(9101)
    sys.stdout.write('service is up!\n')
    main()
