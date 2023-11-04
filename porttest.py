from serial.tools import list_ports
import serial
import time
#------------------开始寻找可用串口--------------------
port_list = list(list_ports.comports())
num = len(port_list)
ports = []
if num <= 0:
    print("找不到任何串口设备")
else:
    for i in range(num):
        # 将 ListPortInfo 对象转化为 list
        port = list(port_list[i])[0]
        ports.append(port)

print('所有com口',ports)
#------------------打开设备--------------------
baudrate_ = 9600
port = ports[0] #
try:
    serial_op = serial.Serial(port=port, baudrate=baudrate_, bytesize=8, parity='O', stopbits=1)
except:
    print('打开设备出错')

#------------------发送命令--------------------
# 需要发送的串口指令
command= '66 AA FF FF 01 00 FF BB'
command_ = bytes.fromhex(command)
# print(command_)
serial_op.write(command_)
time.sleep(1)
serial_op.close()