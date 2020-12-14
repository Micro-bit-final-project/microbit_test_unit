# Add your Python code here. E.g.
from microbit import *


while True:
    # Send data to computer
    info = [accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()]
    print(info)
    # Retrieve data from computer
    message = uart.readline()
    if message:
        str_message = str(message)
        str_message = str_message[2:-1]
        mList = str_message.split(',')
        data = []
        try:
            for value in mList:
                data.append(float(value))
        except ValueError:
            continue
    sleep(200)
