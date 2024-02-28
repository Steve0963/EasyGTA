from pynput.keyboard import KeyCode
import Memory
from time import sleep
from Utils import ahk,press_and_release,press,release,move
import Initial as ini
import Utils
import Offsets
import KeyBindings 

HEALTH_LIMLI=Utils.health_limit()


def badsport_value():
    value=Utils.badsport()
    if value !=None:
        return int(value)
    else:
        return ''

def kill_game():
    if not Utils.is_pause():
        Memory.KillProcess()

def idle():
    if Utils.is_look_back():
        release(KeyBindings.GameKeyBind.LOOK_BACK)
    else:
        press(KeyBindings.GameKeyBind.LOOK_BACK)

def releaseC():
    if Utils.is_in_car():
        release(KeyBindings.GameKeyBind.LOOK_BACK) 
    else:
        press(KeyBindings.GameKeyBind.LOOK_BACK)

def heal():
    if not Utils.is_in_car() and Utils.crt_health()<HEALTH_LIMLI:
        armo=Memory.address_by_offsets(Offsets.ARMO)
        health=Memory.address_by_offsets(Offsets.CURRENT_HEALTH)
        press(KeyBindings.GameKeyBind.WEAPON_LIST)
        sleep(0.15)
        if Utils.is_weaponlist_open():
            while Utils.crt_health() <HEALTH_LIMLI:
                #press_and_release(KeyBindings.HEALTH)
                Memory.write_memory(health,"f",Utils.crt_health()+10)
            sleep(0.1)
            Memory.write_memory(armo,"f",50)
            #press_and_release(KeyBindings.ARMO)
        release(KeyBindings.GameKeyBind.WEAPON_LIST)
   

def auto_esc():
    if Utils.is_character_select() and Utils.is_in_car()  :
        sleep(0.18)
        press_and_release(KeyBindings.KeyBoard.ESC)

def tab():
    press_and_release(KeyBindings.GameKeyBind.WEAPON_LIST)

def auto_tab():
    sleep(0.075)
    tab()

def jump():
    if not Utils.is_in_car() and not Utils.is_home_open() and not ini.IS_JUMP:
                ini.IS_JUMP=True
                while ini.IS_JUMP:
                    press_and_release(KeyBindings.GameKeyBind.JUMP)
                    if 0<Utils.crt_health()<HEALTH_LIMLI*0.55:
                        heal()
                    sleep(0.05)

def reload_while_down():
    if not Utils.is_pause() and not Utils.is_in_car() :
        while ini.LEFT_PRESSED and Utils.is_in_game():
            if Utils.is_need_reload() and Utils.crt_weapon_ammo()!=0:
                if ini.CRT_WEAPON==KeyBindings.Weapons.SNIPER or not ini.LEFT_PRESSED:
                    break
                else:
                    quick_last_weapon()
            elif trans_weapon()==KeyBindings.Weapons.MELEE_WEAPON and not Utils.is_home_open() and not Utils.is_texting() :
                    press_and_release(KeyBindings.GameKeyBind.CONTEXT)
            else:
                pass
            for i in range(120):
                if not ini.LEFT_PRESSED:
                    break
                sleep(0.001)
        if ini.CRT_WEAPON==KeyBindings.Weapons.HEAVY_WEAPON and Utils.is_first_person():
            melee_hand()
    

def reload_while_up():
     if not Utils.is_pause() and not Utils.is_in_car():
        if ini.CRT_WEAPON==KeyBindings.Weapons.SNIPER and Utils.is_need_reload():
            quick_last_weapon()
    

def tab_run():
    while ini.X2_PRESSED:
       tab()
       if 0<Utils.crt_health()<HEALTH_LIMLI*0.55:
           heal()
    quick_last_weapon()

def melee_hand():
    ini.LEFT_PRESSED=False
    press(KeyCode.from_char(KeyBindings.Weapons.SPECIAL_WEAPON))
    press(KeyCode.from_char(KeyBindings.Weapons.HAND))
    release(KeyCode.from_char(KeyBindings.Weapons.HAND))
    release(KeyCode.from_char(KeyBindings.Weapons.SPECIAL_WEAPON))
    
def trans_weapon():
    weapon=Utils.crt_weapon()
    if weapon==0:
        weapon=KeyBindings.Weapons.PISTO
    elif weapon==1:
       weapon=KeyBindings.Weapons.MACHINE_GUN
    elif weapon==2:
        weapon=KeyBindings.Weapons.RIFLE
    elif weapon==3:
        weapon=KeyBindings.Weapons.SNIPER
    elif weapon==4:
        weapon=KeyBindings.Weapons.MELEE_WEAPON
    elif weapon==5:
        weapon=KeyBindings.Weapons.SHOT_GUN
    elif weapon==6:
        weapon=KeyBindings.Weapons.HEAVY_WEAPON
    else:
        weapon=ini.CRT_WEAPON
    ini.CRT_WEAPON=weapon
    return weapon

def quick_last_weapon():
    if ini.CRT_WEAPON==KeyBindings.Weapons.MELEE_WEAPON or ini.CRT_WEAPON==KeyBindings.Weapons.HEAVY_WEAPON and not Utils.is_first_person():
        ini.CRT_WEAPON=KeyBindings.Weapons.PISTO
    press(KeyCode.from_char(KeyBindings.Weapons.SPECIAL_WEAPON))
    press(KeyCode.from_char(ini.CRT_WEAPON))
    release(KeyCode.from_char(ini.CRT_WEAPON))
    release(KeyCode.from_char(KeyBindings.Weapons.SPECIAL_WEAPON))
    #press_and_release(KeyCode.from_char(KeyBindings.Weapons.SPECIAL_WEAPON))
    #press_and_release(KeyCode.from_char(ini.CRT_WEAPON))


def buy_ammo():
    ahk('m',delay=0.2)
    ahk(KeyBindings.KeyBoard.UP,7)
    ahk(KeyBindings.KeyBoard.ENTER,2)
    ahk(KeyBindings.KeyBoard.LEFT,Utils.ammo_left_times())
    ahk(KeyBindings.KeyBoard.DOWN)
    ahk(KeyBindings.KeyBoard.ENTER)
    ahk('m',delay=0)


def wear_necklace():
    ahk('m',delay=0.2)
    ahk(KeyBindings.KeyBoard.UP,6)
    ahk(KeyBindings.KeyBoard.ENTER)
    ahk(KeyBindings.KeyBoard.DOWN)
    ahk(KeyBindings.KeyBoard.ENTER)
    ahk(KeyBindings.KeyBoard.DOWN,6)
    ahk(KeyBindings.KeyBoard.LEFT)
    ahk('m',delay=0)

def start_egine():
    ahk('m',delay=0.2)
    ahk(KeyBindings.KeyBoard.UP,9)
    ahk(KeyBindings.KeyBoard.ENTER)
    ahk(KeyBindings.KeyBoard.UP)
    ahk(KeyBindings.KeyBoard.ENTER)
    ahk(KeyBindings.KeyBoard.DOWN,2)
    ahk(KeyBindings.KeyBoard.LEFT)
    ahk(KeyBindings.KeyBoard.ENTER)
    ahk(KeyBindings.KeyBoard.DOWN,4)
    ahk(KeyBindings.KeyBoard.ENTER,2)
    ahk('m',delay=0)
    
def snack_on_car():
    ahk('m',delay=0.2)
    ahk(KeyBindings.KeyBoard.UP,7)
    ahk(KeyBindings.KeyBoard.ENTER)
    ahk(KeyBindings.KeyBoard.DOWN,2)
    ahk(KeyBindings.KeyBoard.ENTER)

def change_session():
    ahk('p',delay=0.2)
    ahk(KeyBindings.KeyBoard.RIGHT,delay=0.5)
    ahk(KeyBindings.KeyBoard.ENTER,delay=0.6)
    ahk(KeyBindings.KeyBoard.UP,4)
    ahk(KeyBindings.KeyBoard.ENTER,delay=0.8)
    ahk(KeyBindings.KeyBoard.UP)

def act3():
    if Utils.is_in_facility():
        press(KeyBindings.KeyBoard.DOWN)
        press(KeyBindings.KeyBoard.RIGHT)
        sleep(0.005)
        press(KeyBindings.KeyBoard.SPACE)
        sleep(0.005)
        release(KeyBindings.KeyBoard.SPACE)
        release(KeyBindings.KeyBoard.DOWN)
        release(KeyBindings.KeyBoard.RIGHT)

def right_space():
    if Utils.is_in_facility():
        press(KeyBindings.KeyBoard.RIGHT)
        sleep(0.005)
        press(KeyBindings.KeyBoard.SPACE)
        sleep(0.005)
        release(KeyBindings.KeyBoard.SPACE)
        release(KeyBindings.KeyBoard.RIGHT)


def suspend_game():
        if ini.IS_SUSPEND:
            Memory.suspend()
            for i in range(100):
                if ini.IS_SUSPEND:
                    sleep(0.08)
                else: 
                    break
            Memory.resume()
            ini.IS_SUSPEND=False
            


def set_visual():
    if not Utils.is_texting() and not Utils.is_pause() and not Utils.is_weaponlist_open():
        addresses=[Memory.address_by_offsets(Offset) for Offset in Offsets.VISUAL]
        if Utils.is_in_car():

            if Utils.is_first_person():
                for address in addresses[1:]:
                    Memory.write_memory(address,"i",ini.THIRD_PERSON)
            else:
                for address in addresses[1:]:
                    Memory.write_memory(address,"i",ini.FIRST_PERSON)

        else:
            if Utils.is_first_person():
                Memory.write_memory(addresses[0],"i",ini.THIRD_PERSON)

            else:
                Memory.write_memory(addresses[0],"i",ini.FIRST_PERSON)
