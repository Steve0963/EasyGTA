from Utils import is_in_game,auto_reload
from pynput.mouse import Button
from pynput.keyboard import Key
from  threading import Thread,Timer
import GameFunction as GF
import Initial as ini
from KeyBindings import Weapons
import KeyBindings
def vk(key):
    return key+48

def on_click(x, y, button, pressed):
    if is_in_game():
        if pressed:
            if button==Button.x1:
                Thread(target=GF.melee_hand).start()

            if button==Button.x2:
                ini.X2_PRESSED=True
                Thread(target=GF.tab_run).start()

            if button==Button.left:
                ini.LEFT_PRESSED=True
                Thread(target=GF.reload_while_down).start() 
        else:
            if button==Button.x2:
                ini.X2_PRESSED=False

            if button==Button.left:
                ini.LEFT_PRESSED=False
                GF.reload_while_up()  
            
                
def on_scroll(x, y, dx, dy):
    if is_in_game():
        delay_seconds = 1.0
        Timer(delay_seconds, GF.trans_weapon).start()
                
def on_press(key):
    if is_in_game():
        try:
            if  49<=key.vk<=58 and key.vk!=vk(Weapons.SPECIAL_WEAPON):#key.vk 49-58是数字键1-9
                GF.tab()
                if key.vk!=vk(Weapons.HAND) and key.vk!=vk(Weapons.MELEE_WEAPON):
                    ini.CRT_WEAPON=key.vk-48
                    #print(ini.CRT_WEAPON)
            if key.vk==86:#v键
                GF.set_visual()
            if key.vk==67:#v键
                ini.SNACKS=1

        except:
            if key==KeyBindings.AMMO:
               GF.buy_ammo()
            if key==KeyBindings.NECKLACE:
               GF.wear_necklace()
            if key==KeyBindings.START_EGINE:
                GF.start_egine()
            if key ==KeyBindings.SNACKS:
                GF.snack_on_car()
            if key ==KeyBindings.SESSION:
                #GF.change_session()
                pass
            if key==KeyBindings.IDLE:
                GF.idle()
            if key== Key.space:
                Thread(target=GF.jump).start() 
            if key==Key.tab:
                GF.heal()
            if key==Key.end:
                ini.IS_SUSPEND= not ini.IS_SUSPEND
                Thread(target=GF.suspend_game).start() 
            if key==Key.page_down:
                GF.act3()
            if key==Key.page_up:
                GF.right_space()
            if key==Key.delete:
                GF.kill_game()
                auto_reload()
    
    else:
       # print(key.vk)
        try:
            pass
        except:
            pass
    

#键盘释放事件
def on_release(key):
    if is_in_game():
        if key ==Key.alt_l:
            GF.esc()
        
