from pynput import keyboard, mouse
import Functions as func
import threading

isInMission=True
x2_pressed = False
tab_pressed=False
initWeapon=keyboard.KeyCode.from_char(6)
stopListening=False


def TabRun():
    while x2_pressed:
        func.press_and_release(keyboard.Key.insert)
    func.press_and_release(keyboard.KeyCode.from_char(func.specialWeapon()))
    func.press_and_release(initWeapon)
    
def on_click(x, y, button, pressed):
    if func.isInGame():
        global x2_pressed
        if pressed:
            if button==mouse.Button.x2:
                x2_pressed=True
                threading.Thread(target=TabRun).start()
            if button==mouse.Button.x1:
                func.press_and_release(keyboard.KeyCode.from_char(func.specialWeapon()))
                func.press_and_release(keyboard.KeyCode.from_char(func.hand()))
        else:
            if button==mouse.Button.x2:
                x2_pressed=False
                

#键盘按下事件
def on_press(key):
    if func.isInGame():
        global initWeapon,isInMission,tab_pressed
        try:
            if  49<=key.vk<=58 and key.vk!=func.specialWeapon()+48:#key.vk 49-58是数字键1-9
                func.Tab()
                if key.vk!=func.hand()+48:
                    initWeapon=key
            elif keyboard.KeyCode.from_char('`')==key:
                isInMission=not isInMission
                print(isInMission)
            else:pass

        except:
            if key==keyboard.Key.f3:
                func.BuyAmmo(func.getMenu(isInMission))
            if key==keyboard.Key.f4:
                func.WearNecklace(func.getMenu(isInMission))
            if key==keyboard.Key.f5:
                func.StartEgine(func.getMenu(isInMission))
            if key ==keyboard.Key.f6:
                func.SnacksOnCar(func.getMenu(isInMission))
            if key== keyboard.Key.space:
                func.Space()
            if key==keyboard.Key.tab:
                func.send_c()
            if key==keyboard.Key.end:
                func.stopGTA5()
            if key==keyboard.Key.page_down:
                func.act3()
            if key==keyboard.Key.page_up:
                func.right_space()
            if key==keyboard.Key.delete:
                func.endGTA5()
#键盘释放事件
def on_release(key):
    global tab_pressed
    if func.isInGame():
        if key ==  keyboard.Key.alt_l:
            func.Esc()
