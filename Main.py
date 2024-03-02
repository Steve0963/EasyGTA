from threading import Thread
from pystray import Icon, Menu, MenuItem
from PIL import Image
from GameFunction import badsport_value
import Initial as ini
from Utils import restart, exit_click
from pynput import keyboard, mouse
from Input import on_press, on_release, on_click, on_scroll

def create_ui():
    icon_image = Image.open(ini.ICON_PATH)
    menu_items = [
        MenuItem(f"BadSportValue : {badsport_value()}", badsport_value),
        MenuItem("Reload", restart),
        MenuItem("Exit", exit_click),
    ]

    menu = Menu(*menu_items)
    ini.ICON = Icon(
        "Easy GTA5", icon_image, menu=menu, title="Created By QuoVadis8 For GTA5"
    )
    ini.ICON.run()

def create_listener():
    key_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    mouse_listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll)
    key_listener.start()
    mouse_listener.start()

if __name__ == "__main__":
    Thread(target=create_ui).start()
    Thread(target=create_listener).start()
    
