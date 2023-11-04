import clr  # add C# suppor

clr.FindAssembly("PythonNetTest.dll") ## 加载c#dll文件
clr.AddReference('DLL_test')
from DLL_test import *

if __name__ == '__main__':
    print('test ClassLibrary1.dll by python')
    instance = My_Dll()
    # instance.ShowForm()
    print('2+3=', instance.Add(2, 3))
