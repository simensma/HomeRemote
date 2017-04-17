import serial
ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    command = input('Enter command: ')

    ser.write(str(command).encode())
