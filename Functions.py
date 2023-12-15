#系统库
import threading
import os
from pynput import keyboard, mouse
from time import sleep
import pygetwindow as gw
#UI库
from pystray import Icon, Menu, MenuItem
from PIL import Image
#工具库
import MemoryTool as MT
import Input as In
import ctypes
import sys

PROCESS_NAME="GTA5.exe"
ICON_PATH ='C:/Users/iamas/Desktop/EasyGTA/icon.png'
controller = keyboard.Controller()

def press_and_release(key):
    controller.press(key)
    controller.release(key)

def press(key):
    controller.press(key)

def release(key):
    controller.release(key)

def getMenu(isInMission):
    if isInMission:
        return 10
    else :
        return 11

def badSportValue():
    Offsets=[0x02EF5880,0xDC8, 0xB0, 0xA08]
    value=MT.getValueByOffets(Offsets,ctypes.c_float)
    if value !=None:
        return int(value)
    else:
        return ''
def test():
    Offsets=[0x26AEC0C]
    value=MT.getValueByOffets(Offsets,ctypes.c_ulong)
    if value!=None:
        print(value)
    else:
        print('test none')

def endGTA5():
    MT.endProcess()

#28E8687 是否公寓
def isInGame():
    if gw.getActiveWindow()!=None:
        return "Grand Theft Auto V" in gw.getActiveWindow().title
    
def Esc():
    sleep(0.2)
    press_and_release(keyboard.Key.esc)

def Tab():
    press_and_release(keyboard.Key.insert)

def Space():
    press_and_release(keyboard.Key.ctrl_r)

def send_c():
    press_and_release('c')

def BuyAmmo(type):
    times = 3 if type==10 else 4
    press_and_release('m')
    sleep(0.2)
    [press_and_release(keyboard.Key.down) for i in range(times)]
    sleep(0.03)
    [press_and_release(keyboard.Key.enter) for i in range(2)]


def WearNecklace(type):
    times = 4 if type==10 else 5
    press_and_release('m')
    sleep(0.2)
    [press_and_release(keyboard.Key.down) for i in range(times)]
    sleep(0.03)
    press_and_release(keyboard.Key.enter)
    sleep(0.03)
    press_and_release(keyboard.Key.down)
    sleep(0.03)
    press_and_release(keyboard.Key.enter)
    sleep(0.03)
    [press_and_release(keyboard.Key.down) for i in range(6)]
    sleep(0.03)
    press_and_release(keyboard.Key.left)
    sleep(0.03)
    [press_and_release(keyboard.Key.backspace) for i in range(3)]

def StartEgine(type):
    times = 1 if type==10 else 2
    press_and_release('m')
    sleep(0.2)
    [press_and_release(keyboard.Key.down) for i in range(times)]
    sleep(0.03)
    press_and_release(keyboard.Key.enter)
    sleep(0.03)
    press_and_release(keyboard.Key.up)
    sleep(0.03)
    press_and_release(keyboard.Key.enter)
    sleep(0.03)
    [press_and_release(keyboard.Key.up) for i in range(3)]
    [press_and_release(keyboard.Key.enter) for i in range(2)]
    sleep(0.03)
    press_and_release(keyboard.Key.backspace)
    sleep(0.03)
    [press_and_release(keyboard.Key.up) for i in range(4)]
    sleep(0.03)
    press_and_release(keyboard.Key.enter)
    sleep(0.03)
    press_and_release(keyboard.Key.left)
    sleep(0.03)
    press_and_release(keyboard.Key.enter)
    sleep(0.03)
    [press_and_release(keyboard.Key.backspace) for i in range(3)]

def SnacksOnCar(type):
    times = 3 if type==10 else 4
    press_and_release('m')
    sleep(0.2)
    [press_and_release(keyboard.Key.down) for i in range(times)]
    sleep(0.03)
    press_and_release(keyboard.Key.enter)
    sleep(0.03)
    [press_and_release(keyboard.Key.down) for i in range(2)]
    sleep(0.03)
    press_and_release(keyboard.Key.enter)

def act3():
    press('s')
    press('d')
    sleep(0.005)
    press(keyboard.Key.space)
    sleep(0.005)
    release(keyboard.Key.space)
    release('s')
    release('d')

def right_space():
    press('d')
    sleep(0.005)
    press(keyboard.Key.space)
    sleep(0.005)
    release(keyboard.Key.space)
    release('d')


def stopGTA5():
    MT.suspend()
    sleep(8)
    MT.resume()

def specialWeapon():
    return 3

def hand():
    return 8

def exit_click(icon, item):
    icon.stop()  # 停止系统托盘应用
    In.stopListening=True
def creatUI():
    icon_image = Image.open(ICON_PATH)
    menu_items=[
        MenuItem("Test",test), 
        MenuItem(f'恶意值：{badSportValue()} (点击刷新)', badSportValue), 
        MenuItem('重新加载', restart),
        MenuItem('Exit', exit_click)]
    
    menu = Menu(*menu_items)
    icon = Icon("Easy GTA5", icon_image, menu=menu,title="Created By QuoVadis8 For GTA5")
    icon.run()
    print(In.stopListening)
    
def creatListener():
    key_listener=keyboard.Listener(on_press=In.on_press, on_release=In.on_release)
    mouse_listener=mouse.Listener(on_click=In.on_click)
    key_listener.start()
    mouse_listener.start()
    if In.stopListening:
        key_listener.stop()
        mouse_listener.stop()

def restart():
    print('restart')
    python_executable = sys.executable
        # 关闭当前应用程序，然后重新启动
    os.execl(python_executable, python_executable, *sys.argv)

def creatApp():
    threading.Thread(target=creatUI).start()
    creatListener()
    

        

    




