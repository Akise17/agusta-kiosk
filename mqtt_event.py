import paho.mqtt.client as mqtt
import serial
import time

# Define callback function to handle incoming messages
class SerialCommand():
    def send(command):
        SERIAL_PORT = '/dev/ttyUSB0'
        BAUD_RATE = 9600
        
        try:
            ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
            print("Serial port opened successfully.")
            print(command)
            time.sleep(1.5)
            ser.write((command + '\n').encode())

            response = ser.readline().decode().strip()
            print("Response:", response)
        
        except Exception as e:
            print("Error:", str(e))
        finally:
            if ser.is_open:
                ser.close()
                print("Serial port closed.")
def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
          + message.topic + "' with QoS " + str(message.qos))
    if message.topic == "topics/machine":
            if str(message.payload) == "b'dryer_on'":
                SerialCommand.send("run_dryer:60")

# Set up MQTT client instance
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "Agusta_DEV_001")

# Set up callback function
client.on_message = on_message

# Set username and password
username = "agusta-dev"
password = "12345678"
client.username_pw_set(username, password)

# Connect to MQTT broker
broker_address = "agusta-dev.siap.tech"
port = 1880
client.connect(broker_address, port)

# Subscribe to a topic
topic = "topics/#"
client.subscribe(topic)

# Start the network loop to process incoming messages
client.loop_forever()