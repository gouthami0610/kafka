from kafka import KafkaProducer
import json 
# Kafka consumer configuration
consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                        auto-offset-reset='earliest',
                        value_deserializer=lambda v: json.loads(v.decode('utf-8')))

# Subscribe to Kafka topic 'my_topic'
def consume_messages_from_kafka(data):
    consumer.subscribe(['my_topic'])

    for message in consumer:
        print(f"Received message: {message.value}")

if __name__ == '__main__':
    # Example usage
    consume_messages_from_kafka()


## To run the consumer, execute this script. It will listen for messages on the 'my_topic' Kafka topic and print them to the console.
