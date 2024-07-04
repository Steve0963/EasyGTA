from threading import Thread, Timer
from Config import Listener, GameParmas, KeyStatus, Process
from pynput import mouse, keyboard
from KeyBindings import GameKeyBindings, KeyBoard, AppKeyBindings
import Scripts
from pygetwindow import getActiveWindow


def origin(num):
    return num - 48


def is_in_game():
    active_window = getActiveWindow()
    if active_window is not None:
        return Process.Game_Name in active_window.title
    return False


def on_click(x, y, button, pressed):
    if is_in_game():
        if pressed:
            if button == mouse.Button.x1:
                Thread(target=Scripts.hand).start()
            elif button == mouse.Button.x2:
                KeyStatus.X2_Pressed = True
                Thread(target=Scripts.speed_run).start()
            elif button == mouse.Button.left:
                KeyStatus.Left_Pressed = True
                Thread(target=Scripts.reload_while_down).start()
        else:
            if button == mouse.Button.x2:
                KeyStatus.X2_Pressed = False
            if button == mouse.Button.left:
                KeyStatus.Left_Pressed = False


def on_scroll(x, y, dx, dy):
    if is_in_game():
        delay_seconds = 0.5
        Timer(delay_seconds, Scripts.scroll_weapon).start()


def on_move(x, y):
    pass


def on_press(key):
    if is_in_game():
        try:
            key_v = key.vk
            if (
                0 <= origin(key_v) <= 9
                and origin(key_v) != GameKeyBindings.Weapons.Special_weapon
            ):
                Scripts.auto_tab()
                if (
                    origin(key_v) != GameKeyBindings.Weapons.Hand
                    and origin(key_v) != GameKeyBindings.Weapons.Melee_weapon
                ):
                    GameKeyBindings.Weapons.Current_Weapon = origin(key_v)
            elif key_v == KeyBoard.V:
                Scripts.set_visual()
            elif key_v == KeyBoard.C:
                pass
        except AttributeError:
            if key == AppKeyBindings.Buy_Ammo:
                Scripts.buy_ammo()
            elif key == AppKeyBindings.Wear_Necklace:
                Scripts.wear_necklace()
            elif key == AppKeyBindings.Start_Engine:
                Scripts.start_egine()
            elif key == AppKeyBindings.Open_Snacks:
                Scripts.open_snacks()
            elif key == AppKeyBindings.Change_Session:
                Scripts.change_session()
            elif key == AppKeyBindings.Idle:
                Scripts.idle()
            elif key == AppKeyBindings.Jump:
                if not KeyStatus.Space_Pressed:
                    Thread(target=Scripts.continuous_jump).start()
            elif key == AppKeyBindings.Heal:
                if not KeyStatus.Tab_Pressed:
                    Thread(target=Scripts.heal).start()
            elif key == AppKeyBindings.Suspend:
                GameParmas.Is_Suspend = not GameParmas.Is_Suspend
                Thread(target=Scripts.suspend_game).start()
            elif key == AppKeyBindings.Act3:
                Scripts.act3()
            elif key == AppKeyBindings.Act1_Act2:
                Scripts.right_space()
            elif key == AppKeyBindings.Kill:
                Thread(target=Scripts.kill_game).start()


def on_release(key):
    if key == AppKeyBindings.Jump:
        KeyStatus.Space_Pressed = False
    if key == AppKeyBindings.Instant_Stop:
        Scripts.auto_esc()


def init():
    print("开始初始化Listener")
    try:
        Listener.Keyboard = keyboard.Listener(on_press=on_press, on_release=on_release)
        Listener.Mouse = mouse.Listener(
            on_click=on_click, on_scroll=on_scroll, on_move=on_move
        )
        Listener.Keyboard.start()
        Listener.Mouse.start()
        print("初始化完毕")
    except Exception as e:
        print("创建Listener时发生异常:", e)


def destroy():
    print("销毁Listener")
    Listener.Keyboard.stop()
    Listener.Mouse.stop()


def restart():
    print("重启Listener")
    destroy()
    init()
