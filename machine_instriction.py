import serial

SERIAL_PORT = '/dev/tty.usbserial-140'
BAUD_RATE = 9600

def main():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
        print("Serial port opened successfully.")
        
        while True:
            user_input = input("Enter data to send (Press Enter to quit): ")
            if not user_input:
                break
            
            ser.write((user_input + '\n').encode())
            
            if ser.in_waiting > 0:
                response = ser.readline().decode().strip()
                print("Received:", response)
    
    except KeyboardInterrupt:
        print("Keyboard interrupt detected. Exiting...")
    except Exception as e:
        print("Error:", str(e))
    finally:
        if ser.is_open:
            ser.close()
            print("Serial port closed.")

if __name__ == "__main__":
    main()