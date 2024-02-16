from pygetwindow import getActiveWindow
from pynput import keyboard, mouse
from Memory import read_memory,address_by_offsets,get_process_id_by_name
from  ctypes import c_ulong,c_float,c_ubyte

from time import sleep
from  sys import argv,executable
from os import execl

import Offsets
import Initial as ini
controller = keyboard.Controller()
mouse_controller=mouse.Controller()


def is_in_game():#是否在游戏内
    if getActiveWindow()!=None:
        return ini.GAME_NAME in getActiveWindow().title

def is_in_facility():#是否在设施
    Offsets=[0x200E130]
    return read_memory(address_by_offsets(Offsets),c_ulong)==1

def is_online(): #0-线上 #1-故事
    return read_memory(address_by_offsets(Offsets.IS_ONLINE),c_ulong)!=1

def is_in_car(): #0-载具外 #1-载具内
    return read_memory(address_by_offsets(Offsets.IS_IN_CAR),c_ubyte)!=0

def is_first_person():
    return read_memory(address_by_offsets(Offsets.IS_FIRST_PERSON),c_ulong)==4

def is_need_reload():
    #print(read_memory(address_by_offsets(Offsets.CLIP_NUM),c_ulong))
    return read_memory(address_by_offsets(Offsets.CLIP_NUM),c_ulong)==0

def is_pause():
    return read_memory(address_by_offsets(Offsets.IS_PAUSE),c_ulong)==1

def is_snakcs_none():
    return ini.SNACKS==0
def is_texting():
    return read_memory(address_by_offsets(Offsets.IS_TEXTING),c_ubyte)==1
def is_home_open():
    return read_memory(address_by_offsets(Offsets.IS_HOME_MENU),c_ubyte)==1
def is_look_back():
    return read_memory(address_by_offsets(Offsets.IS_LOOK_BACK),c_ubyte)==0

def is_weaponlist_open():
    return read_memory(address_by_offsets(Offsets.IS_WEAPONLIST_OPEN),c_ubyte)==1


def crt_health():#当前血量
    return read_memory(address_by_offsets(Offsets.CURRENT_HEALTH),c_float)

def health_limit():#血量上限
    return read_memory(address_by_offsets(Offsets.HEALTH_LIMLI),c_float)

def crt_weapon():
    return read_memory(address_by_offsets(Offsets.CURRENT_WEAPON),c_ulong)

def crt_weapon_ammo():
    return read_memory(address_by_offsets(Offsets.CURRENT_WEAPON_AMMO),c_ulong)

def badsport():
    return read_memory(address_by_offsets(Offsets.BADSPORT),c_float)

def ammo_left_times():
    if is_in_car():
        left_times=1
    else:
        left_times=0
        if 0<=crt_weapon()<=5 and crt_weapon()!=1:
            left_times=1
        elif crt_weapon()==1:
            left_times=2
        elif crt_weapon()==6:
            left_times=6
        else:
            left_times=5
    return left_times+1

def press_and_release(key):
    controller.press(key)
    controller.release(key)

def press(key):
    controller.press(key)

def release(key):
    controller.release(key)

def ahk(key,times=1,delay=0.02):
    for i in range(times):
        press_and_release(key)
    sleep(delay)

def move(x,y):
    mouse_controller.move(x,y)

def restart():#重启脚本
    python_executable = executable
    execl(python_executable, python_executable, *argv)

def auto_reload():#自动重启脚本
    sleep(10)
    while get_process_id_by_name(ini.PROCESS_NAME)==None:
        sleep(3)
    ini.PID=get_process_id_by_name(ini.PROCESS_NAME)
    sleep(10)
    while not is_online():
        sleep(3)
    sleep(8)
    restart()

def block():
    
    print('blcok')

def unblock():
   print("restore")


