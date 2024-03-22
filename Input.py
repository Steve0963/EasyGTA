from Utils import is_in_game, auto_reload,restart
from pynput.mouse import Button
from threading import Thread, Timer
import GameFunction as GF
import Initial as ini
from KeyBindings import Weapons
import KeyBindings


def vk(key):
    return key + 48


def on_click(x, y, button, pressed):
    ini.IS_JUMP = False
    if is_in_game():
        if pressed:
            if button == Button.x1:
                Thread(target=GF.melee_hand).start()

            if button == Button.x2:
                ini.X2_PRESSED = True
                Thread(target=GF.tab_run).start()

            if button == Button.left:
                ini.LEFT_PRESSED = True
                Thread(target=GF.reload_while_down).start()
        else:
            if button == Button.x2:
                ini.X2_PRESSED = False

            if button == Button.left:
                ini.LEFT_PRESSED = False


def on_scroll(x, y, dx, dy):
    if is_in_game():
        delay_seconds = 1.0
        Timer(delay_seconds, GF.trans_weapon).start()
        #move(0,-10)
    else:
        pass
        #move(0,1)
        #print(ini.Y)
        


def on_move(x, y):
    ini.X=x
    ini.Y=y


def on_press(key):
    if is_in_game():
        try:
            if vk(Weapons.MELEE_WEAPON) <= key.vk <= vk(Weapons.HAND) and key.vk != vk(
                Weapons.SPECIAL_WEAPON
            ):  # key.vk 49-58是数字键1-9
                GF.auto_tab()
                if key.vk != vk(Weapons.HAND) and key.vk != vk(Weapons.MELEE_WEAPON):
                    ini.CRT_WEAPON = key.vk - 48
                    # print(ini.CRT_WEAPON)

            if key.vk == KeyBindings.KeyBoard.V:  # v键
                GF.set_visual()

            if key.vk == KeyBindings.KeyBoard.C:  # c键
                # ini.SNACKS=1
                pass

        except:
            if key == KeyBindings.Function.AMMO:
                GF.buy_ammo()

            if key == KeyBindings.Function.NECKLACE:
                GF.wear_necklace()

            if key == KeyBindings.Function.START_EGINE:
                GF.start_egine()

            if key == KeyBindings.Function.SNACKS:
                GF.snack_on_car()

            if key == KeyBindings.Function.SESSION:
                #GF.drill()
                pass

            if key == KeyBindings.Function.IDLE:
                GF.idle()

            if key == KeyBindings.Function.JUMP:
                Thread(target=GF.jump).start()

            if key == KeyBindings.Function.HEAL:
                Thread(target=GF.heal).start()
                
            if key==KeyBindings.Function.RELOAD:
                restart()

            if key == KeyBindings.Function.SUSPEND:
                ini.IS_SUSPEND = not ini.IS_SUSPEND
                Thread(target=GF.suspend_game).start()

            if key == KeyBindings.Function.ACT3:
                GF.act3()

            if key == KeyBindings.Function.ACT1_ACT2:
                GF.right_space()

            if key == KeyBindings.Function.KILL:
                GF.kill_game()
                auto_reload()

    else:
        # print(key.vk)
        try:
            pass
        except:
            pass


# 键盘释放事件
def on_release(key):
    if is_in_game():

        if key == KeyBindings.Function.INSTANT_STOP:
            GF.auto_esc()

        if key == KeyBindings.Function.JUMP:
            ini.IS_JUMP = False
