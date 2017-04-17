import serial
import warnings
import serial
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

for i,p in enumerate(ports):
    print i, p

p = input("Select serial port: ")

port = ports[p].device

ser = serial.Serial(port, 9600)

print "Waiting for input..."

while True:
    command = input('Enter command: ')

    ser.write(str(command).encode())
