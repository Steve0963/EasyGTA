from pygetwindow import getActiveWindow
from pynput import keyboard, mouse
from Memory import read_memory, address_by_offsets, get_process_id_by_name,GlobalAddress,write_memory
from ctypes import c_ulong, c_float, c_ubyte

from time import sleep
from sys import argv, executable
from os import execl

import Offsets
import Initial as ini

controller = keyboard.Controller()
mouse_controller = mouse.Controller()


def is_in_game():  # 是否在游戏内
    if getActiveWindow() != None:
        return ini.GAME_NAME in getActiveWindow().title


def is_in_facility():  # 是否在设施
    #Offsets = [0x200E130]
    return read_memory(address_by_offsets(Offsets.IS_IN_FACLITY), c_ulong) == 1


def is_online():  # 0-线上 #1-故事
    return read_memory(address_by_offsets(Offsets.IS_ONLINE), c_float) == 125


def is_in_car():  # 0-载具外 #1-载具内
    return read_memory(address_by_offsets(Offsets.IS_IN_CAR), c_ubyte) != 0


def is_first_person():
    return read_memory(address_by_offsets(Offsets.IS_FIRST_PERSON), c_ulong) == 4


def is_need_reload():
    # print(read_memory(address_by_offsets(Offsets.CLIP_NUM),c_ulong))
    return read_memory(address_by_offsets(Offsets.CLIP_NUM), c_ulong) == 0


def is_pause():
    return read_memory(address_by_offsets(Offsets.IS_PAUSE), c_ubyte) == 1


def is_snakcs_none():
    return ini.SNACKS == 0


def is_texting():
    return read_memory(address_by_offsets(Offsets.IS_TEXTING), c_ubyte) == 1


def is_home_open():
    return read_memory(address_by_offsets(Offsets.IS_HOME_MENU), c_ubyte) == 1


def is_look_back():
    return read_memory(address_by_offsets(Offsets.IS_LOOK_BACK), c_ubyte) == 0


def is_weaponlist_open():
    return read_memory(address_by_offsets(Offsets.IS_WEAPONLIST_OPEN), c_ubyte) == 1

def is_weaponwheel_open():
    return read_memory(address_by_offsets(Offsets.IS_WEAPONWHEEL_OPEN), c_ubyte) == 1


def is_space_down():
    return read_memory(address_by_offsets(Offsets.IS_SPACE_DOWN), c_ubyte) == 0


def is_character_select():
    return read_memory(address_by_offsets(Offsets.IS_CHARACTER_SELECT), c_ubyte) == 1

def is_menu_open():
    return read_memory(address_by_offsets(Offsets.IS_MENU_OPEN), c_ubyte)!=255

def is_self():
    return read_memory(address_by_offsets(Offsets.IS_SELF), c_ubyte) == 156


def crt_health():  # 当前血量
    return read_memory(address_by_offsets(Offsets.CURRENT_HEALTH), c_float)


def health_limit():  # 血量上限
    return read_memory(address_by_offsets(Offsets.HEALTH_LIMLI), c_float)


def crt_weapon():
    return read_memory(address_by_offsets(Offsets.CURRENT_WEAPON), c_ulong)


def crt_weapon_ammo():
    return read_memory(address_by_offsets(Offsets.CURRENT_WEAPON_AMMO), c_ulong)


def badsport():
    return read_memory(address_by_offsets(Offsets.BADSPORT), c_float)


def buy_ammo_times():
    if crt_weapon()==1:
        return 3
    return 2

def change_session_type(type):
    
    address=GlobalAddress(Offsets.Global.SESSION_TYPE)
    write_memory(address,'i',type)

def change_session_state(state):
    
    address=GlobalAddress(Offsets.Global.SESSION_STATE)
    write_memory(address,'i',state)

def change_session_cache(value):
    
    address=GlobalAddress(Offsets.Global.SESSION_CACHE)
    write_memory(address,'i',value)

def press_and_release(key):
    controller.press(key)
    controller.release(key)


def press(key):
    controller.press(key)


def release(key):
    controller.release(key)


def ahk(key, times=1, delay=0.02):
    for i in range(times):
        press_and_release(key)
    sleep(delay)

def mouse_position():
    return  mouse_controller.position
def move(x, y):
    #mouse_controller.position=(x, y)
    mouse_controller.move(x,y)

def press_left():
    mouse_controller.press(mouse.Button.left)
def release_left():
    mouse_controller.release(mouse.Button.left)

    

def restart():  # 重启脚本
    print(ini.ICON)
    ini.ICON.stop()
    python_executable = executable
    execl(python_executable, python_executable, *argv)
    
def exit_click(icon):
    icon.stop()

def auto_reload():  # 自动重启脚本
    sleep(10)
    while get_process_id_by_name(ini.PROCESS_NAME) == None:
        sleep(3)
    ini.PID = get_process_id_by_name(ini.PROCESS_NAME)
    ini.ALL_PID= get_process_id_by_name(ini.ALL_GTA_PROCESS)
    sleep(10)
    while not is_online():
        sleep(1)
    sleep(8.5)
    restart()


def block():

    print("blcok")


def unblock():
    print("restore")
