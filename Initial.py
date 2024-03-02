from os.path import join, dirname
import KeyBindings
# 进程名 应用名
GAME_NAME = "Grand Theft Auto V"
PROCESS_NAME = "GTA5.exe"

# 应用图标
ICON_PATH = join(dirname(__file__), "icon.png")

# 是否挂机
IS_SUSPEND = False
X2_PRESSED = False
LEFT_PRESSED = False

CRT_WEAPON = KeyBindings.Weapons.PISTO

FIRST_PERSON = 4
THIRD_PERSON = 0

PID = None
IS_JUMP = False
ICON=None