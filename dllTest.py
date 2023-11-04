import clr  # add C# suppor
from functionCode.get_cwd import get_cwd
a = get_cwd()
print(a)
dll_path = a+'/DLL_test'
clr.AddReference(dll_path)
from DLL_test import *

if __name__ == '__main__':
    print('test ClassLibrary1.dll by python')
    instance = My_Dll()
    # instance.ShowForm()
    print('2+3=', instance.Add(2, 3))
    print(instance.serial_port_Open('COM1'))
    print(instance.serial_port_Beep_ON('02'))
