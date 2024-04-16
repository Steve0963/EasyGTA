WORLD_ADDRESS = 0x01D70168  # 30 E5 36 8C 2B 02 00 00 05 00 00 00 05 00 00
                             # 70 63 30 8C EF 01 00 00 05 00 00 00 05 00 00
                             # ? ? ? ? ? 01 00 00 05 00 00 00 05 00 00
GLOBAL_ADDRESS=0x2EF59A0
# 生命
HEALTH_LIMLI = [WORLD_ADDRESS, 0x284]  # ctypes.c_float
CURRENT_HEALTH = [WORLD_ADDRESS, 0x280]  # ctypes.c_float
# 护甲
ARMO = [WORLD_ADDRESS, 0x150C]

# 恶意值
BADSPORT = [WORLD_ADDRESS + 0x1185718, 0xDC8, 0xB0, 0xA08]  # ctypes.c_float 0x02EF5880

# 视角
VISUAL_GA = WORLD_ADDRESS + 0x290B18
VISUAL = [
    [VISUAL_GA, 0x0],  # 载具外 #ctypes.c_ulong 0x02000C80
    [VISUAL_GA, 0x4],  # 载具内主驾驶 #ctypes.c_ulong
    [VISUAL_GA, 0x8],  # 载具内副驾驶 #ctypes.c_ulong
    [VISUAL_GA, 0xC],
    [VISUAL_GA, 0x10],
    [VISUAL_GA, 0x14],
    [VISUAL_GA, 0x18],
    [VISUAL_GA, 0x1C],
]  # 载具内乘客 #ctypes.c_ulong

# 当前视角
IS_FIRST_PERSON = [WORLD_ADDRESS - 0x13190]  # 0x1D5CFD8
# 是否在载具内
IS_IN_CAR = [WORLD_ADDRESS- 0x1355C]  # ctypes.c_ubyte

# 武器
CURRENT_WEAPON = [WORLD_ADDRESS + 0x2A14C0]  # ctypes.c_ulong 0x2011628
CLIP_NUM = [WORLD_ADDRESS + 0x4C]  # ctypes.c_ulong 0x1D701B4
CURRENT_WEAPON_AMMO = [WORLD_ADDRESS + 0x48]  # ctypes.c_ulong 0x1D701B0
# 设施
IS_IN_FACLITY = [WORLD_ADDRESS + 0x29DFC8]  # ctypes.c_ulong 0x200E130
# 是否在线
IS_ONLINE = [WORLD_ADDRESS, 0x1520]  # ctypes.c_float
# 是否p暂停
IS_PAUSE = [WORLD_ADDRESS + 0x2A7169]  # ctypes.c_ulong 0x20172D1
# 是否在打字
IS_TEXTING = [WORLD_ADDRESS + 0xFC813E]  # ctypes.c_ubyte 0x2D382A6
# 是否home菜单
IS_HOME_MENU = [WORLD_ADDRESS + 0xFC8140]  # ctypes.c_ubyte 0x2D382A8
IS_LOOK_BACK = [WORLD_ADDRESS + 0x88E0E0]  # ctypes.c_ubyte 0x25FE248
IS_WEAPONLIST_OPEN = [WORLD_ADDRESS + 0x29FADC]  # 0x200FC44
IS_WEAPONWHEEL_OPEN = [WORLD_ADDRESS + 0x2A14AE] # ctypes.c_ubyte
IS_SPACE_DOWN = [WORLD_ADDRESS + 0x893FD0]  # ctypes.c_ubyte

IS_CHARACTER_SELECT = [WORLD_ADDRESS + 0x29CEB9]  # ctypes.c_ubyte
IS_MENU_OPEN=[WORLD_ADDRESS + 0x914FB0]  # ctypes.c_ubyte

IS_SELF=[WORLD_ADDRESS , 0x2B]

class Global:
    SESSION_TYPE=1575032
    SESSION_STATE=1574589
    SESSION_CACHE=1574591