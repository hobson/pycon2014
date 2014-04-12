import serial, time
 
s = serial.Serial('/dev/tty.usbmodem1421', 9600)
 
while True:
    s.write([1])
    time.sleep(1)
    s.write([0])
    time.sleep(1)
Martin Bircher