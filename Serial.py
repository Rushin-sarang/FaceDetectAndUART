import serial
port = 'COM14'
baud_rate = 9600
try:
    ser = serial.Serial(port, baud_rate, timeout=1)
    print("port opened")
    data_to_send = 1
   # data_to_send_in_bytes = data_to_send.encode('utf-8')
    ser.write(data_to_send)
    ser.close()
except serial.SerialException as e:
    print(f"error {e}")