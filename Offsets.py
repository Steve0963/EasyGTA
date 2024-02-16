#生命
HEALTH_LIMLI=[0x01D70168,0x284] #ctypes.c_float
CURRENT_HEALTH=[0x01D70168,0x280] #ctypes.c_float
ARMO=[0x01D70168,0x150c]

#恶意值
BADSPORT=[0x02EF5880,0xDC8, 0xB0, 0xA08] #ctypes.c_float

#视角
VISUAL=[[0x02000C80,0x0],#载具外 #ctypes.c_ulong
    [0x02000C80,0x4],#载具内主驾驶 #ctypes.c_ulong
    [0x02002B68,0x168,0xD8],#载具内副驾驶 #ctypes.c_ulong
    [0x02000C80,0x428,0x63C]]#载具内乘客 #ctypes.c_ulong
IS_FIRST_PERSON=[0x1D5CFD8] 
#载具
IS_IN_CAR=[0x01D70168,0xE32] #ctypes.c_ubyte

#武器
CURRENT_WEAPON=[0x2011628] #ctypes.c_ulong
CLIP_NUM=[0x1D701B4]#ctypes.c_ulong
CURRENT_WEAPON_AMMO=[0x1D701B0] #ctypes.c_ulong
#设施eeeeee
IS_IN_FACLITY=[0x200E130] #ctypes.c_ulong
#是否在线
IS_ONLINE=[0x1D89E48] #ctypes.c_ulong
#是否p暂停
IS_PAUSE=[0x1FFB758] #ctypes.c_ulong
#是否在打字
IS_TEXTING=[0x2D382A6]#ctypes.c_ubyte
#是否home菜单
IS_HOME_MENU=[0x2D382A8]#ctypes.c_ubyte
IS_LOOK_BACK=[0x25FE248]#ctypes.c_ubyte
IS_WEAPONLIST_OPEN=[0x200FC44]