from kafka import KafkaClient

def connect_to_kafka(bootstrap_servers):
    try:
        connection = KafkaClient(bootstrap_servers=bootstrap_servers)
        print('Connected to Kafka')
        return connection.bootstrap_connected()
    except:
        return False

if __name__ == '__main__':
    connect_to_kafka("10.244.0.17:9092")
