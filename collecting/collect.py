import serial
import re
from collecting import dev_info

try:
    arduino = serial.Serial(dev_info.DEVICE_PORT, timeout=dev_info.DEFAULT_TIMEOUT, baudrate=dev_info.DEFAULT_BAUDRATE)
except:
    print('Communication error. Check connection to device.')


def collect_raw_data(list_length):
    # Skips first empty line
    arduino.readline()

    raw_data = []
    while len(raw_data) < list_length:
        # info is the first line with values
        info = re.sub('[\n\r]', '', str(arduino.readline(), 'utf-8'))

        raw_data.append(info)
        print(info)
    return raw_data
