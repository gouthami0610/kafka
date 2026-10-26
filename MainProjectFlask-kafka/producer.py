from kafka import KafkaProducer
import json 
# Kafka producer configuration
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Send a message to Kafka topic 'my_topic'
def send_message_to_kafka(message):
    producer.send('my_topic', {'message': message})
    producer.flush()  # Ensure the message is sent                  
    print(f"Message '{message}' sent to Kafka topic 'my_topic'")

if __name__ == '__main__':
    # Example usage
    send_message_to_kafka("Hello, Kafka!")
    
