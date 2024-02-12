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
    Memory.KillProcess()

def idle():
    ini.IS_IDLE=not ini.IS_IDLE
    if ini.IS_IDLE:
        press(KeyBindings.LOOK_BACK)
    else:
        release(KeyBindings.LOOK_BACK)

def releaseC():
    if Utils.is_in_car():
        release(KeyBindings.LOOK_BACK) 
    else:
        press(KeyBindings.LOOK_BACK)

def heal():
    if not Utils.is_snakcs_none() and not Utils.is_in_car():
        cnt=0
        press(KeyBindings.WEAPON_LIST)
        sleep(0.15)
        crt_health=Utils.crt_health()
        while Utils.crt_health() <HEALTH_LIMLI:
            press_and_release(KeyBindings.HEALTH)
            cnt+=1
            if cnt>15:
                break
        if crt_health==Utils.crt_health() and crt_health!=HEALTH_LIMLI:
            ini.SNACKS=0
        sleep(0.1)
        press_and_release(KeyBindings.ARMO)
        release(KeyBindings.WEAPON_LIST)

def esc():
    sleep(0.2)
    press_and_release(KeyBindings.ESC)

def tab():
    press_and_release(KeyBindings.WEAPON_LIST)

def jump():
    if not Utils.is_in_car():
        press_and_release(KeyBindings.JUMP)

def reload_while_down():
    if not Utils.is_pause() and not Utils.is_in_car():
        while ini.LEFT_PRESSED:
            if Utils.is_need_reload() and Utils.crt_weapon_ammo()!=0:
                #weapon=trans_weapon()
                weapon=ini.CRT_WEAPON
                if weapon == KeyBindings.Weapons.HEAVY_WEAPON:
                    if Utils.is_first_person(Memory.address_by_offsets(Offsets.VISUAL[0])):
                        quick_last_weapon()
                    else:
                        continue
                elif weapon == KeyBindings.Weapons.SHOT_GUN:
                    sleep(0.05)
                    quick_last_weapon()
                elif weapon == KeyBindings.Weapons.SNIPER:
                    sleep(0.05)
                    quick_last_weapon()
                elif weapon==KeyBindings.Weapons.SPECIAL_WEAPON:
                    break
                else:  
                    quick_last_weapon()
                    pass
            elif Utils.crt_weapon_ammo()>10000 and Utils.is_first_person(Memory.address_by_offsets(Offsets.VISUAL[0])):
                sleep(0.45)
                quick_last_weapon()
            elif trans_weapon()==KeyBindings.Weapons.MELEE_WEAPON:
                for i in range(3):
                    press_and_release(KeyBindings.CONTEXT)
                    sleep(0.1)
            else:
                pass
            sleep(0.2)
    

def reload_while_up():
     if not Utils.is_pause() and not Utils.is_in_car():
        if trans_weapon()==KeyBindings.Weapons.SNIPER :
            quick_last_weapon()
    


def tab_run():
    while ini.X2_PRESSED:
       tab()
       if 0<Utils.crt_health()<HEALTH_LIMLI*0.7:
           heal()
    quick_last_weapon()

def melee_hand():
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
    #weapon=trans_weapon()
    if ini.CRT_WEAPON==KeyBindings.Weapons.MELEE_WEAPON:
        ini.CRT_WEAPON=KeyBindings.Weapons.PISTO
    if ini.CRT_WEAPON==KeyBindings.Weapons.HEAVY_WEAPON:
        if Utils.is_first_person(Memory.address_by_offsets(Offsets.VISUAL[0])):
            pass
        else:
            ini.CRT_WEAPON=KeyBindings.Weapons.PISTO

    press(KeyCode.from_char(KeyBindings.Weapons.SPECIAL_WEAPON))
    press(KeyCode.from_char(ini.CRT_WEAPON))
    release(KeyCode.from_char(ini.CRT_WEAPON))
    release(KeyCode.from_char(KeyBindings.Weapons.SPECIAL_WEAPON))


def buy_ammo():
    ahk('m',delay=0.2)
    ahk(KeyBindings.UP,7)
    ahk(KeyBindings.ENTER,2)
    ahk(KeyBindings.LEFT,Utils.ammo_left_times())
    ahk(KeyBindings.DOWN)
    ahk(KeyBindings.ENTER)
    ahk('m',delay=0)


def wear_necklace():
    ahk('m',delay=0.2)
    ahk(KeyBindings.UP,6)
    ahk(KeyBindings.ENTER)
    ahk(KeyBindings.DOWN)
    ahk(KeyBindings.ENTER)
    ahk(KeyBindings.DOWN,6)
    ahk(KeyBindings.LEFT)
    ahk('m',delay=0)

def start_egine():
    ahk('m',delay=0.2)
    ahk(KeyBindings.UP,9)
    ahk(KeyBindings.ENTER)
    ahk(KeyBindings.UP)
    ahk(KeyBindings.ENTER)
    ahk(KeyBindings.DOWN,2)
    ahk(KeyBindings.LEFT)
    ahk(KeyBindings.ENTER)
    ahk(KeyBindings.DOWN,4)
    ahk(KeyBindings.ENTER,2)
    ahk('m',delay=0)
    
def snack_on_car():
    ahk('m',delay=0.2)
    ahk(KeyBindings.UP,7)
    ahk(KeyBindings.ENTER)
    ahk(KeyBindings.DOWN,2)
    ahk(KeyBindings.ENTER)

def change_session():
    ahk('p',delay=0.2)
    ahk(KeyBindings.RIGHT,delay=0.5)
    ahk(KeyBindings.ENTER,delay=0.6)
    ahk(KeyBindings.UP,4)
    ahk(KeyBindings.ENTER,delay=0.8)
    ahk(KeyBindings.UP)

def act3():
    if Utils.is_in_facility():
        press(KeyBindings.DOWN)
        press(KeyBindings.RIGHT)
        sleep(0.005)
        press(KeyBindings.SPACE)
        sleep(0.005)
        release(KeyBindings.SPACE)
        release(KeyBindings.DOWN)
        release(KeyBindings.RIGHT)

def right_space():
    if Utils.is_in_facility():
        press(KeyBindings.RIGHT)
        sleep(0.005)
        press(KeyBindings.SPACE)
        sleep(0.005)
        release(KeyBindings.SPACE)
        release(KeyBindings.RIGHT)


def suspend_game():
        Memory.suspend()
        sleep(8)
        Memory.resume()


def set_visual():
    if not Utils.is_texting() and not Utils.is_pause():
        addresses=[Memory.address_by_offsets(Offset) for Offset in Offsets.VISUAL]
        if Utils.is_in_car():

            if Utils.is_first_person(addresses[1]):
                for address in addresses[1:]:
                    Memory.write_memory(address,"i",ini.THIRD_PERSON)

            else:
                for address in addresses[1:]:
                    Memory.write_memory(address,"i",ini.FIRST_PERSON)

        else:

            if Utils.is_first_person(addresses[0]):
                Memory.write_memory(addresses[0],"i",ini.THIRD_PERSON)

            else:
                Memory.write_memory(addresses[0],"i",ini.FIRST_PERSON)
