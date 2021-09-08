import sys
import time
from kafka import KafkaConsumer
from prometheus_client import start_http_server, Summary, Counter

consumer =  KafkaConsumer('simple-one', bootstrap_servers=['10.244.0.17:9092'])
messages_in = Counter('messeges_in', 'number of messages sent to kafka')

def main():
    for message in consumer:
        print("{}:{}:{}: key={} value={}".format(message.topic, message.partition, message.offset, message.key,message.value))
        messages_in.inc()

if __name__ == '__main__':
    start_http_server(9101)
    main()
    for i in range(100):
        sys.stdout.write('-------stdout-----')
        print('----------------p--------------')
        time.sleep(200)
