from pynput.keyboard import KeyCode
import Memory
from time import sleep
from Utils import ahk, press_and_release, press, release
import Initial as ini
import Utils
import Offsets
import KeyBindings

HEALTH_LIMLI = Utils.health_limit()


def badsport_value():
    value = Utils.badsport()
    if value != None:
        return int(value)
    else:
        return ""


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
    if Utils.is_self():
        if not Utils.is_in_car() and Utils.crt_health() < HEALTH_LIMLI:
            armo = Memory.address_by_offsets(Offsets.ARMO)
            health = Memory.address_by_offsets(Offsets.CURRENT_HEALTH)
            press(KeyBindings.GameKeyBind.WEAPON_LIST)
            sleep(0.15)
            if Utils.is_weaponlist_open():
                while Utils.crt_health() < HEALTH_LIMLI:
                    #press_and_release(KeyBindings.GameKeyBind.HEALTH)
                    Memory.write_memory(health, "f", Utils.crt_health() + 20)
                    sleep(0.02)
                sleep(0.1)
                Memory.write_memory(armo, "f", 50)
                # press_and_release(KeyBindings.GameKeyBind.ARMO)
            release(KeyBindings.GameKeyBind.WEAPON_LIST)
       



def auto_esc():
    if  Utils.is_in_car() and Utils.is_character_select():
        sleep(0.18)
        press_and_release(KeyBindings.KeyBoard.ESC)


def tab():
    press_and_release(KeyBindings.GameKeyBind.WEAPON_LIST)


def auto_tab():
    ini.IS_JUMP = False
    sleep(0.11)
    tab()


def jump():
    if not ini.IS_JUMP and not Utils.is_in_car() and not Utils.is_home_open() :
        ini.IS_JUMP = True
        while ini.IS_JUMP:
            press_and_release(KeyBindings.GameKeyBind.JUMP)
            if 0 < Utils.crt_health() < HEALTH_LIMLI * 0.6:
                heal()
            sleep(0.03)


def reload_while_down():
    if (
        not Utils.is_weaponwheel_open()
        and not Utils.is_in_car()
        and not Utils.is_pause()
    ):
        while ini.LEFT_PRESSED and Utils.is_in_game():
            if Utils.is_need_reload() and Utils.crt_weapon_ammo() != 0:
                if (
                    ini.CRT_WEAPON == KeyBindings.Weapons.SNIPER
                    or not ini.LEFT_PRESSED
                    or ini.CRT_WEAPON == KeyBindings.Weapons.HEAVY_WEAPON
                ):
                    break
                quick_last_weapon()
            elif (
                trans_weapon() == KeyBindings.Weapons.MELEE_WEAPON
                and not Utils.is_pause()
                and not Utils.is_home_open()
                and not Utils.is_texting()
            ):
                press_and_release(KeyBindings.GameKeyBind.CONTEXT)
            else:
                pass
            for _ in range(10):
                if not ini.LEFT_PRESSED:
                    break
                sleep(0.011)

def tab_run():
    while ini.X2_PRESSED:
        tab()
        if 0 < Utils.crt_health() < HEALTH_LIMLI * 0.6:
            heal()
    #if not Utils.is_texting() and not Utils.is_home_open():
    quick_last_weapon()


def melee_hand():
    #if not Utils.is_texting() and not Utils.is_home_open():
        press(KeyCode.from_char(KeyBindings.Weapons.SPECIAL_WEAPON))
        press(KeyCode.from_char(KeyBindings.Weapons.HAND))
        release(KeyCode.from_char(KeyBindings.Weapons.HAND))
        release(KeyCode.from_char(KeyBindings.Weapons.SPECIAL_WEAPON))
    


def trans_weapon():
    weapon_mapping = {
        0: KeyBindings.Weapons.PISTO,
        1: KeyBindings.Weapons.MACHINE_GUN,
        2: KeyBindings.Weapons.RIFLE,
        3: KeyBindings.Weapons.SNIPER,
        4: KeyBindings.Weapons.MELEE_WEAPON,
        5: KeyBindings.Weapons.SHOT_GUN,
        6: KeyBindings.Weapons.HEAVY_WEAPON,
    }
    ini.CRT_WEAPON = weapon_mapping.get(Utils.crt_weapon(), ini.CRT_WEAPON)

    return ini.CRT_WEAPON


def quick_last_weapon():
    if (
        ini.CRT_WEAPON == KeyBindings.Weapons.MELEE_WEAPON
        or ini.CRT_WEAPON == KeyBindings.Weapons.HEAVY_WEAPON
        and not Utils.is_first_person()
    ):
        ini.CRT_WEAPON = KeyBindings.Weapons.PISTO
    press(KeyCode.from_char(KeyBindings.Weapons.SPECIAL_WEAPON))
    press(KeyCode.from_char(ini.CRT_WEAPON))
    release(KeyCode.from_char(ini.CRT_WEAPON))
    release(KeyCode.from_char(KeyBindings.Weapons.SPECIAL_WEAPON))


def buy_ammo():
        dir_key=KeyBindings.KeyBoard.LEFT
        if Utils.crt_weapon()==6:
            dir_key=KeyBindings.KeyBoard.RIGHT
        ahk("m", delay=0.2)
        ahk(KeyBindings.KeyBoard.UP, 7)
        ahk(KeyBindings.KeyBoard.ENTER, 2)
        ahk(dir_key, Utils.buy_ammo_times())
        ahk(KeyBindings.KeyBoard.DOWN)
        ahk(KeyBindings.KeyBoard.ENTER)
        ahk("m", delay=0)


def wear_necklace():
        ahk("m", delay=0.2)
        ahk(KeyBindings.KeyBoard.UP, 6)
        ahk(KeyBindings.KeyBoard.ENTER)
        ahk(KeyBindings.KeyBoard.DOWN)
        ahk(KeyBindings.KeyBoard.ENTER)
        ahk(KeyBindings.KeyBoard.DOWN, 6)
        ahk(KeyBindings.KeyBoard.LEFT)
        ahk("m", delay=0)


def start_egine():
        ahk("m", delay=0.2)
        ahk(KeyBindings.KeyBoard.UP, 9)
        ahk(KeyBindings.KeyBoard.ENTER)
        ahk(KeyBindings.KeyBoard.UP)
        ahk(KeyBindings.KeyBoard.ENTER)
        ahk(KeyBindings.KeyBoard.DOWN, 2)
        ahk(KeyBindings.KeyBoard.LEFT)
        ahk(KeyBindings.KeyBoard.ENTER)
        ahk(KeyBindings.KeyBoard.DOWN, 4)
        ahk(KeyBindings.KeyBoard.ENTER, 2)
        ahk("m", delay=0)


def snack_on_car():
    if Utils.is_self():
            ahk("m", delay=0.2)
            ahk(KeyBindings.KeyBoard.UP, 7)
            ahk(KeyBindings.KeyBoard.ENTER)
            ahk(KeyBindings.KeyBoard.DOWN, 2)
            ahk(KeyBindings.KeyBoard.ENTER)
            lAST_HEALTH=Utils.crt_health()
            while Utils.crt_health() < HEALTH_LIMLI and Utils.is_in_game():
                ahk(KeyBindings.KeyBoard.ENTER)
                if(lAST_HEALTH==Utils.crt_health()):
                    break
            ahk(KeyBindings.KeyBoard.BACK)
            ahk(KeyBindings.KeyBoard.UP)
            ahk(KeyBindings.KeyBoard.ENTER)
            ahk(KeyBindings.KeyBoard.UP,3)
            ahk(KeyBindings.KeyBoard.ENTER)
            ahk('m', delay=0)


def change_session():
    ahk("p", delay=0.2)
    ahk(KeyBindings.KeyBoard.RIGHT, delay=0.5)
    ahk(KeyBindings.KeyBoard.ENTER, delay=0.6)
    ahk(KeyBindings.KeyBoard.UP, 4)
    ahk(KeyBindings.KeyBoard.ENTER, delay=0.8)
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
        ini.IS_SUSPEND = False


def set_visual():
    if (
        not Utils.is_texting()
        and not Utils.is_home_open()
        # and not Utils.is_pause()
        and not Utils.is_weaponlist_open()
    ):
        addresses = [Memory.address_by_offsets(Offset) for Offset in Offsets.VISUAL]
        if Utils.is_in_car():

            if Utils.is_first_person():
                for address in addresses[1:]:
                    Memory.write_memory(address, "i", ini.THIRD_PERSON)
            else:
                for address in addresses[1:]:
                    Memory.write_memory(address, "i", ini.FIRST_PERSON)

        else:
            if Utils.is_first_person():
                Memory.write_memory(addresses[0], "i", ini.THIRD_PERSON)

            else:
                Memory.write_memory(addresses[0], "i", ini.FIRST_PERSON)
