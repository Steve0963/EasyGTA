from pynput.keyboard import Key


class GameKeyBind:
    HEALTH = "="
    ARMO = "-"
    LOOK_BACK = "c"
    WEAPON_LIST = Key.insert
    JUMP = Key.ctrl_r
    CONTEXT = "e"


class KeyBoard:
    V = 86
    C = 67
    ESC = Key.esc
    SPACE = Key.space
    UP = Key.up
    DOWN = Key.down
    LEFT = Key.left
    RIGHT = Key.right
    ENTER = Key.enter


class Function:
    AMMO = Key.f3
    NECKLACE = Key.f4
    START_EGINE = Key.f5
    SNACKS = Key.f6
    SESSION = Key.f7
    IDLE = Key.f11
    SUSPEND = Key.end
    KILL = Key.delete
    ACT3 = Key.page_down
    ACT1_ACT2 = Key.page_up
    HEAL = Key.tab
    JUMP = Key.space
    INSTANT_STOP = Key.alt_l


class Weapons:
    PISTO = 6
    MACHINE_GUN = 8
    RIFLE = 5
    SNIPER = 7
    MELEE_WEAPON = 1
    HAND = 9
    SHOT_GUN = 2
    HEAVY_WEAPON = 4
    SPECIAL_WEAPON = 3
