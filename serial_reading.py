import serial,datetime

ser = serial.Serial('COM3', 115200, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
s = ser.read()
temp_reading = {}
if s:
    temp_reading['temp'] = s
    temp_reading['time'] = datetime.datetime.now()


