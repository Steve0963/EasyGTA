from os.path import join, dirname
import KeyBindings
# 进程名 应用名
GAME_NAME = "Grand Theft Auto V"
PROCESS_NAME = "GTA5.exe"
LAUNCHER="Launcher.exe"
PLAY_GTA5="PlayGTAV.exe"
ROCKSTAR_SERVICE="RockstarService.exe"
ERROR_HANDLER="RockstarErrorHandler.exe"
SC_HELPER="SocialClubHelper.exe"
ALL_GTA_PROCESS=[PROCESS_NAME,LAUNCHER,PLAY_GTA5,ERROR_HANDLER,SC_HELPER]
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
ALL_PID=None
IS_JUMP = False
ICON=None

GLOBAL_PTR=0

CLOSED_FRIEND=6
SESSION_STATE=33
SESSION_CACHE=0
