from pynput.keyboard import KeyCode
from time import sleep
import Utils
from Utils import ahk, press, release, press_and_release
from KeyBindings import GameKeyBindings, KeyBoard
from Config import GameParmas, KeyStatus
from WeaponHash import Melee, get_weapon_type


def init():
    GameParmas.Health_Limit = Utils.health_limit()


def tab():
    press_and_release(GameKeyBindings.Weapons.Weapon_list)


def auto_tab():
    sleep(0.1)
    tab()


def hand():
    # if not Utils.is_texting() and not Utils.is_home_open():
    press(KeyCode.from_char(GameKeyBindings.Weapons.Special_weapon))
    press(KeyCode.from_char(GameKeyBindings.Weapons.Hand))
    release(KeyCode.from_char(GameKeyBindings.Weapons.Hand))
    release(KeyCode.from_char(GameKeyBindings.Weapons.Special_weapon))


def quick_last_weapon():
    if (
        GameKeyBindings.Weapons.Current_Weapon == GameKeyBindings.Weapons.Melee_weapon
        or GameKeyBindings.Weapons.Current_Weapon
        == GameKeyBindings.Weapons.Heavy_weapon
        #or GameKeyBindings.Weapons.Current_Weapon
        # == GameKeyBindings.Weapons.Special_weapon
        and not Utils.is_first_person()
    ):
        GameKeyBindings.Weapons.Current_Weapon = GameKeyBindings.Weapons.Pistol
    press(KeyCode.from_char(GameKeyBindings.Weapons.Special_weapon))
    press(KeyCode.from_char(GameKeyBindings.Weapons.Current_Weapon))
    release(KeyCode.from_char(GameKeyBindings.Weapons.Current_Weapon))
    release(KeyCode.from_char(GameKeyBindings.Weapons.Special_weapon))


def reload_while_down():
    if (
        not Utils.is_weaponlist_open()
        and not Utils.is_in_car()
        and not Utils.is_pause()
        and not Utils.is_home_open()
        and not Utils.is_texting()
    ):
        #print(get_weapon_type(Utils.get_weapon_hash()))
        while KeyStatus.Left_Pressed and Utils.is_in_game():
            if (
                Utils.is_need_reload()
                and get_weapon_type(Utils.get_weapon_hash())
                != GameKeyBindings.Weapons.Melee_weapon
            ):
                if (
                    GameKeyBindings.Weapons.Current_Weapon
                    == GameKeyBindings.Weapons.Pistol
                    or GameKeyBindings.Weapons.Current_Weapon
                    == GameKeyBindings.Weapons.Machine_gun
                    or GameKeyBindings.Weapons.Current_Weapon
                    == GameKeyBindings.Weapons.Rifle
                ):
                    quick_last_weapon()

            if Utils.current_weapon_type() == GameKeyBindings.Weapons.Melee_weapon:
                press_and_release(GameKeyBindings.Character.Context)
            else:
                pass
            sleep(0.2)


def speed_run():
    while KeyStatus.X2_Pressed:
        tab()
        if 0 < Utils.current_health() < GameParmas.Health_Limit * 0.6:
            heal()
    quick_last_weapon()


def set_weapon():
    sleep(2)
    Utils.set_current_weapon(GameParmas.Current_Weapon_Hash)


def scroll_weapon():
    weapon=Utils.current_weapon_type()
    if weapon!=GameKeyBindings.Weapons.Special_weapon:
        GameKeyBindings.Weapons.Current_Weapon = Utils.current_weapon_type()


def continuous_jump():
    if not Utils.is_in_car() and not Utils.is_home_open() and not Utils.is_texting():
        KeyStatus.Space_Pressed = True
        while KeyStatus.Space_Pressed:
            sleep(0.05)
            if KeyStatus.Space_Pressed:
                Utils.press_and_release(GameKeyBindings.Character.Jump)
            if 0 < Utils.current_health() < GameParmas.Health_Limit * 0.6:
                heal()
            sleep(0.2)


def jump():
    Utils.press_and_release(GameKeyBindings.Character.Jump)


def auto_esc():
    if Utils.is_in_car():
        sleep(0.2)
        if Utils.is_character_select():
            press_and_release(KeyBoard.Esc)


def buy_ammo():
    dir_key = KeyBoard.Left
    if Utils.current_weapon_type() == GameKeyBindings.Weapons.Heavy_weapon:
        dir_key = KeyBoard.Right
    ahk(GameKeyBindings.Character.Menu, delay=0.2)
    ahk(KeyBoard.Up, 7)
    ahk(KeyBoard.Enter, 2)
    ahk(dir_key, Utils.buy_ammo_times())
    ahk(KeyBoard.Down)
    ahk(KeyBoard.Enter)
    ahk(GameKeyBindings.Character.Menu, delay=0)


def wear_necklace():
    ahk(GameKeyBindings.Character.Menu, delay=0.2)
    ahk(KeyBoard.Up, 6)
    ahk(KeyBoard.Enter)
    ahk(KeyBoard.Down)
    ahk(KeyBoard.Enter)
    ahk(KeyBoard.Down, 6)
    ahk(KeyBoard.Left)
    ahk(GameKeyBindings.Character.Menu, delay=0)


def start_egine():
    ahk(GameKeyBindings.Character.Menu, delay=0.2)
    ahk(KeyBoard.Up, 9)
    ahk(KeyBoard.Enter)
    ahk(KeyBoard.Up)
    ahk(KeyBoard.Enter)
    ahk(KeyBoard.Down, 2)
    # ahk(KeyBoard.Right)
    ahk(KeyBoard.Enter)
    ahk(KeyBoard.Down, 4)
    ahk(KeyBoard.Enter, 2)
    ahk(GameKeyBindings.Character.Menu, delay=0)


def open_snacks():
    if Utils.is_self():
        ahk(GameKeyBindings.Character.Menu, delay=0.2)
        ahk(KeyBoard.Up, 7)
        ahk(KeyBoard.Enter)
        ahk(KeyBoard.Down, 2)
        ahk(KeyBoard.Enter)
        lAST_HEALTH = Utils.current_health()
        while Utils.current_health() < GameParmas.Health_Limit and Utils.is_in_game():
            ahk(KeyBoard.Enter)
            if lAST_HEALTH == Utils.current_health():
                break
        ahk(KeyBoard.Back)
        ahk(KeyBoard.Up)
        ahk(KeyBoard.Enter)
        ahk(KeyBoard.Up, 3)
        ahk(KeyBoard.Enter)
        ahk(GameKeyBindings.Character.Menu, delay=0)


def act3():
    if Utils.is_in_facility():
        press(KeyBoard.Down)
        press(KeyBoard.Right)
        sleep(0.005)
        press(KeyBoard.Space)
        sleep(0.005)
        release(KeyBoard.Space)
        release(KeyBoard.Down)
        release(KeyBoard.Right)


def right_space():
    if Utils.is_in_facility():
        press(KeyBoard.Right)
        sleep(0.005)
        press(KeyBoard.Space)
        sleep(0.005)
        release(KeyBoard.Space)
        release(KeyBoard.Right)


def change_session():
    Utils.change_session_type(GameParmas.Closed_Friend)
    Utils.change_session_state(GameParmas.Session_State)
    Utils.change_session_cache(GameParmas.Session_Cache)


def set_visual():
    if (
        not Utils.is_texting()
        and not Utils.is_home_open()
        and not Utils.is_pause()
        and not Utils.is_weaponlist_open()
    ):
        if Utils.is_in_car():

            if Utils.is_first_person():
                Utils.set_visual_in_car(GameParmas.Third_Person)
            else:
                Utils.set_visual_in_car(GameParmas.First_Person)

        else:
            if Utils.is_first_person():
                Utils.set_visual_out_car(GameParmas.Third_Person)
            else:
                Utils.set_visual_out_car(GameParmas.First_Person)


def badsport_value():
    value = Utils.badsport()
    if value != None:
        return int(value)
    else:
        return ""


def idle():
    if Utils.is_look_back():
        release(GameKeyBindings.Character.Look_back)
    else:
        press(GameKeyBindings.Character.Look_back)


def kill_game():
    if not Utils.is_pause():
        Utils.kill_process()
        Utils.auto_reload()


def suspend_game():
    if GameParmas.Is_Suspend:
        Utils.suspend()
        for i in range(100):
            if GameParmas.Is_Suspend:
                sleep(0.08)
            else:
                break
        Utils.resume()
        GameParmas.Is_Suspend = False


def heal():
    if Utils.is_self():
        KeyStatus.Tab_Pressed = True
        if not Utils.is_in_car() and Utils.current_health() < GameParmas.Health_Limit:
            press(GameKeyBindings.Weapons.Weapon_list)
            sleep(0.15)
            if Utils.is_weaponlist_open():
                while Utils.current_health() < GameParmas.Health_Limit:
                    # press_and_release(KeyBindings.GameKeyBind.HEALTH)
                    Utils.add_health()
                    sleep(0.03)
                sleep(0.1)
                Utils.add_armo()
                # press_and_release(KeyBindings.GameKeyBind.ARMO)
            release(GameKeyBindings.Weapons.Weapon_list)
        KeyStatus.Tab_Pressed = False
