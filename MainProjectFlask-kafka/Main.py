#pip install flask ==2.3.3
#pip install kafka-python==2.3.0
#start the kafka server 
#kafka-server-start.bat C:\kafka_2.13-3.5.0\config\server.properties
from flask import Flask, render_template, request,jsonify
from kafka import KafkaProducer
import json

app = Flask(__name__)

# Kafka producer configuration
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message')
    
    if message:
        # Send the message to Kafka topic 'my_topic'
        producer.send('my_topic', {'message': message})
        producer.flush()  # Ensure the message is sent
        return jsonify({'status': 'Message sent to Kafka'}), 200
    else:
        return jsonify({'error': 'No message provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)