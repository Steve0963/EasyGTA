from pynput.keyboard import Key


class GameKeyBindings:

    class Character:
        Look_back = "c"
        Jump = Key.ctrl_r
        Context = "e"
        Health = "="
        Armo = "-"
        Menu = "m"

    class Weapons:
        Weapon_list = Key.insert
        Pistol = 6
        Machine_gun = 8
        Rifle = 5
        Sniper = 7
        Melee_weapon = 1
        Hand = 9
        Shot_gun = 2
        Heavy_weapon = 4
        Special_weapon = 3

        Current_Weapon = Pistol


class AppKeyBindings:
    Buy_Ammo = Key.f3
    Wear_Necklace = Key.f4
    Start_Engine = Key.f5
    Open_Snacks = Key.f6
    Change_Session = Key.f10
    Idle = Key.f11
    Suspend = Key.end
    Kill = Key.delete
    Act3 = Key.page_down
    Act1_Act2 = Key.page_up
    Heal = Key.tab
    Jump = Key.space
    Instant_Stop = Key.alt_l
    Reload_App = Key.f11


class KeyBoard:
    V = 86
    C = 67
    Esc = Key.esc
    Space = Key.space
    Up = Key.up
    Down = Key.down
    Left = Key.left
    Right = Key.right
    Enter = Key.enter
    Back = Key.backspace
