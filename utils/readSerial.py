import serial

# Define the serial port and baud rate

serial_port = '/dev/ttyUSB0'  # Change this to your specific USB port
baud_rate = 9600  # Match the baud rate of your device

# Initialize serial communication
ser = serial.Serial(serial_port, baud_rate, timeout=1)

try:
    while True:
        # Read one line of data from the serial port
        line = ser.readline().decode('utf-8').strip()
        
        if line:
            print(f"Received: {line}")

except KeyboardInterrupt:
    print("Serial reading terminated by user")

finally:
    # Close the serial connection
    ser.close()
    print("Serial port closed")
