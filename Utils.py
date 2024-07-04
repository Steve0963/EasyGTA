from ctypes import c_float, c_ubyte, c_ulong
from time import sleep
from Config import GameParmas, Process, Listener,AppParmas
from pygetwindow import getActiveWindow, getWindowsWithTitle
from KeyBindings import GameKeyBindings
from Listener import restart as listerner_restart
from Memory import (
    read,
    write_GA,
    write,
    suspend_process,
    kill_process,
    resume_process,
    pid_init,
)
from Address import Pointers, Basis, Menu, Index, Judge, Visual
from pynput import keyboard, mouse

def init():
    Listener.Keyboard_Controller = keyboard.Controller()
    Listener.Mouse_Controller = mouse.Controller()


def origin(num):
    return num - 48


def is_in_game():
    if getActiveWindow() != None:
        return Process.Game_Name in getActiveWindow().title


def is_first_person():
    return (
        read(Pointers.World_Ptr, Basis.Current_Visual, c_ubyte)
        == GameParmas.First_Person
    )


def is_in_facility():  # 是否在设施
    return (
        read(Pointers.Faclity_Ptr, Judge.Is_In_Faclity, c_ubyte)
        == GameParmas.Status_True
    )


def is_online():  # 0-线上 #1-故事
    return read(Pointers.World_Ptr, Basis.Online, c_float) == GameParmas.Online


def is_in_car():  # 0-载具外 #1-载具内
    return read(Pointers.World_Ptr, Basis.Is_In_Car, c_ubyte) == GameParmas.Status_True


def is_texting():
    return (
        read(Pointers.TextMenu_Ptr, Menu.Text_Menu, c_ubyte) == GameParmas.Status_True
    )


def is_home_open():
    return (
        read(Pointers.HomeMenu_Ptr, Menu.Home_Menu, c_ubyte) == GameParmas.Status_True
    )


def is_character_select():
    return (
        read(Pointers.Selector_Ptr, Menu.Character_Selector, c_ubyte)
        == GameParmas.Status_True
    )


def is_need_reload():
    return (
        read(Pointers.World_Ptr, Basis.Current_Clip_Num, c_ulong)
        == GameParmas.Status_False
    )


def is_pause():
    return read(Pointers.PauseMenu_Ptr, Menu.P_Menu, c_ubyte) == GameParmas.Status_True


def is_weaponlist_open():
    return (
        read(Pointers.WeaponMenu_Ptr, Menu.Weapon_Menu, c_ubyte)
        == GameParmas.Status_True
    )


def is_look_back():
    #print(read(Pointers.Lookback_Ptr, Judge.Look_Back, c_ubyte))
    return (
        read(Pointers.Lookback_Ptr, Judge.Look_Back, c_ubyte) == GameParmas.Status_True
    )



def is_menu_open():
    return 1 != 255


def is_self():
    return (
        read(Pointers.World_Ptr, Basis.Entity_Type, c_ubyte) == GameParmas.Entity_Self
    )


def suspend():
    suspend_process()
    # suspend_process(Process.ProcessPids.Process_Rockstar_Service)


def resume():
    # resume_process(Process.ProcessPids.Process_Rockstar_Service)
    resume_process()


def kill():
    kill_process()


def current_health():  # 当前血量
    return read(Pointers.World_Ptr, Basis.Health, c_float)


def health_limit():  # 血量上限
    return read(Pointers.World_Ptr, Basis.Health_Max, c_float)


def add_health():
    write(Pointers.World_Ptr, Basis.Health, "f", current_health() + 15)


def add_armo():
    write(Pointers.World_Ptr, Basis.Armor, "f", 50)


def set_visual_in_car(person):
    for visual in Visual.All_Visual[1:]:
        write(Pointers.Visual_Ptr, visual, "i", person)


def set_visual_out_car(person):
    write(Pointers.Visual_Ptr, Visual.Visual_Out_Vehicle, "i", person)


def current_weapon_type():
    weapon = read(Pointers.WeaponType_Ptr, Judge.Weapon_Type, c_ubyte)
    return GameParmas.Weapon_Mapping.get(weapon)

def get_weapon_hash():
    return read(Pointers.World_Ptr, Basis.Current_Weapon_Hash, c_ulong)

def set_current_weapon(hash):
    write(Pointers.World_Ptr, Basis.Current_Weapon_Hash,'i',hash)

def current_weapon_ammo_num():
    return read(Pointers.World_Ptr, Basis.Ammo_Num, c_ulong)


def badsport():
    return read(Pointers.Global_Ptr, Basis.BadSport_Value, c_float)


def buy_ammo_times():
    if current_weapon_type() == GameKeyBindings.Weapons.Machine_gun:
        return 3
    return 2
def joatt(statName):
    hash = 0

    for c in statName.lower():
        hash += ord(c)
        hash &= 0xFFFFFFFF
        hash += (hash << 10) & 0xFFFFFFFF
        hash &= 0xFFFFFFFF
        hash ^= (hash >> 6) & 0xFFFFFFFF
        hash &= 0xFFFFFFFF

    hash += (hash << 3) & 0xFFFFFFFF
    hash &= 0xFFFFFFFF
    hash ^= (hash >> 11) & 0xFFFFFFFF
    hash &= 0xFFFFFFFF
    hash += (hash << 15) & 0xFFFFFFFF
    hash &= 0xFFFFFFFF
    return hash & 0xFFFFFFFF

def change_session_type(type):

    write_GA(Index.Session_Type, "i", type)


def change_session_state(state):
    write_GA(Index.Session_State, "i", state)


def change_session_cache(value):
    write_GA(Index.Session_Cache, "i", value)

def end_custence():
    write_GA(Index.Cutscene_Parma1,GameParmas.Status_True)
    write_GA(Index.Cutscene_Parma2,GameParmas.Status_True)
    sleep(1)
    write_GA(Index.Cutscene_Parma1,GameParmas.Status_False)
    write_GA(Index.Cutscene_Parma2,GameParmas.Status_False)



'''
def reverse_joatt(hash):

    data = {"input": hash}

    # 发送 POST 请求
    response = post("https://joaat.sh/api/convert", data=data)

    if response.status_code == 200:
        json_data = response.json()
        if "output" in json_data:
            return json_data["output"]
        elif "error" in json_data:
            return f"Error: {json_data['error']}"
    else:
        return f"Error: {response.status_code}"
'''
def press_and_release(key):
    Listener.Keyboard_Controller.press(key)
    Listener.Keyboard_Controller.release(key)


def press(key):
    Listener.Keyboard_Controller.press(key)


def release(key):
    Listener.Keyboard_Controller.release(key)


def ahk(key, times=1, delay=0.02):
    for i in range(times):
        press_and_release(key)
    sleep(delay)


def restart():
    GameParmas.Health_Limit =health_limit()
    listerner_restart()


def exit_click():
    AppParmas.Icon.stop()
    try:
        Listener.Keyboard.stop()
        Listener.Mouse.stop()
    except Exception as e:
        print("销毁Listener时发生异常:", e)

def auto_reload():  # 自动重启脚本
    sleep(10)
    while not getWindowsWithTitle(Process.Game_Name):
        sleep(3)
    print('重新初始化内存')
    pid_init()
    restart()
    sleep(10)
    print('开始等待上线')
    while not is_online():
        sleep(1)
    print('上线')
    sleep(10)
    GameParmas.Health_Limit =health_limit()
    print('重启')
    


def block():

    print("blcok")


def unblock():
    print("restore")



