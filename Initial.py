from  os.path import join,dirname
#进程名 应用名
GAME_NAME="Grand Theft Auto V"
PROCESS_NAME="GTA5.exe"

#应用图标
ICON_PATH =join(dirname(__file__), 'icon.png')

#是否挂机
IS_IDLE=False

X2_PRESSED = False
LEFT_PRESSED =False

CRT_WEAPON=6

FIRST_PERSON=4
THIRD_PERSON=0

STOP_LISTENING=False

PID=None

SNACKS=1