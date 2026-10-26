from kafka import KafkaProducer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092')
producer.send('test', b'Hello, World!')
producer.flush()
print('Message sent successfully!')

