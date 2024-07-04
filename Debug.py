from threading import Thread
import Memory
from Address import Pointers
from Config import Process

Memory.init()

print('debug开始')
base_address=Process.Game_Base_Address
print(hex(base_address))
start=0x000000
end=0x1000000
thread_num=10
test="0x7ff71cf0e4b8"

def slove(part0,part1):
    print('计算开始')
    for i in range(part0,part1):
        result=Memory.calculate_ptr(base_address+i)
        #print(hex(result))
        if hex(result)==test:#0x7ff7e95551c4
            print(hex(i))
            print(hex(result))
            print('线程结束')
            return
    print('没有结果')




slove(start,end)

