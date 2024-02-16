from pynput import keyboard
HEALTH='='
ARMO='-'
LOOK_BACK='c'
PAUSE='p'
WEAPON_LIST=keyboard.Key.insert
JUMP=keyboard.Key.ctrl_r
CONTEXT='e'
ESC=keyboard.Key.esc
SPACE=keyboard.Key.space
UP=keyboard.Key.up
DOWN=keyboard.Key.down
LEFT=keyboard.Key.left
RIGHT=keyboard.Key.right
ENTER=keyboard.Key.enter

AMMO=keyboard.Key.f3
NECKLACE=keyboard.Key.f4
START_EGINE=keyboard.Key.f5
SNACKS=keyboard.Key.f6
SESSION=keyboard.Key.f7
IDLE=keyboard.Key.f11

class Weapons:
    PISTO=6
    MACHINE_GUN=8
    RIFLE=5
    SNIPER=7
    MELEE_WEAPON=1
    HAND=9
    SHOT_GUN=2
    HEAVY_WEAPON=4
    SPECIAL_WEAPON=3
