class Pointers:
    Global_Ptr = "4C 8D 05 ?? ?? ?? ?? 4D 8B 08 4D 85 C9 74 11"  # 
    World_Ptr = "48 8B 05 ?? ?? ?? ?? 45 ?? ?? ?? ?? 48 8B 48 08 48 85 C9 74 07"  # 0x2E1611
    Visual_Ptr = "48 8B 15 ?? ?? ?? 01 48 85 D2 74 14 83"  # 0x2491a8 #48 8B 15 ?? ?? ?? 01 48 85 D2 74 14 83 F9 07 77 0F 48 63 C1
    Lookback_Ptr = '58 8A 0D AD 17 FC 01 8A 15 A8 17 FC 01 8A 85 80 30 00 00 F3'  # 0x563e54 58 8A 0D ?? ?? ?? ?? 8A 15 ?? ?? ?? ??
    HomeMenu_Ptr = "48 8B 0D ?? ?? ?? ?? 4C 8B 11 48 8B D0 8B 40 18 44 8B 4A 20"  # 0x146F50C
    PauseMenu_Ptr = "14 38 1D ?? ?? ?? 01 75 0C 38 1D"  # 0x2C5917 14 38 1D ?? ?? ?? 01 75 0C 38 1D ?? ?? ?? 01 75 04 32 C0 EB          
    TextMenu_Ptr = "0F 95 05 1B E4 A7 02 E8 54 8D E7 FF 84 C0 0F 84 25 01 00 00"  # 0x195FF5 
    Faclity_Ptr = "48 8D 0D ?? ?? ?? ?? B2 01 E9 ?? ?? E3"  # 0x29BA8  48 8D 0D ?? ?? ?? ?? B2 01 E9 ?? ?? E3 00 ?? ?? 48 8B C4 48
    WeaponType_Ptr = "48 8D 0D ?? ?? ?? 01 4C 8B C3 89 45 20 E8 ?? 3D 17 00 EB 44"  # 0x2C6342
    Attribute_Ptr = "00 8A 0D 43 EB A8 01 45 84 C0 74 0D 84 C9 75 09 40 84 F6 74"  # 0x10218E7
    Selector_Ptr = "00 39 2D ?? ?? ?? 01 41 0F ?? F0 7F 54 40 38"  # 0x1B8BBF 00 39 2D ?? ?? ?? 01 41 0F ?? F0 7F 54 40 38 2D ?? ?? ?? 01
    FirstPerson_Ptr = "22 8B 0D 92 DD B5 01 85 C9 78 18 83 F8 04 74 0A 83 F9 04 75"
                      


class Basis:  # World_Ptr
    Health = [0x0,0x8, 0x280]
    Health_Max = [0x0,0x8, 0x284]
    Armor = [0x0,0x8, 0x150C]  # float, 50:Online 100:Story Mode
    Player_Info = 0x10A8
    Current_Weapon_Hash = [0x0,0x8, 0x10B8, 0x18]  # 武器hash
    Weapon_Manager = 0x10B8
    Online = [0x0,0x8, 0x1520]
    Ammo_Num = [0x48]
    Current_Clip_Num = [-0x1A]
    Current_Visual = [0x0]
    Is_In_Car = [0x0,0x8, 0xE32]
    Entity_Type = [0x0,0x8, 0x2B]
    BadSport_Value=[-0x120,0xDD8,0xA18]


class Visual:  # Visual_Ptr
    Visual_Out_Vehicle = [0x0, 0x0]
    Visual_On_4Wheel_Driver = [0x0, 0x4]
    Visual_On_Bike_Driver = [0x0, 0x8]
    Visual_On_Bike_Driver = [0x0, 0xC]
    Visual_On_Jet_Driver = [0x0, 0x10]
    Visual_On_Sea_Driver = [0x0, 0x14]
    Visual_On_Heli_Driver = [0x0, 0x18]
    Visual_On_Heli_Driver = [0x0, 0x1C]

    All_Visual = [
        Visual_Out_Vehicle,
        Visual_On_4Wheel_Driver,
        Visual_On_Bike_Driver,
        Visual_On_Bike_Driver,
        Visual_On_Jet_Driver,
        Visual_On_Sea_Driver,
        Visual_On_Heli_Driver,
        Visual_On_Heli_Driver,
    ]


class Menu:
    P_Menu = [0x0]  # Pause_Ptr
    Home_Menu = [0x0, 0x70, 0x104]  # HomeMenu_Ptr
    M_Menu = []
    Text_Menu = [0x0]  # TextMenu_Ptr
    Weapon_Menu = [0x64]  # WeaponMenu_Ptr
    Character_Selector = [0x0]  # Selector_Ptr


class Judge:
    Is_In_Faclity = [0x2819]  # Faclity_Ptr
    Weapon_Type = [0x1A48]  # WeaponType_Ptr
    Look_Back=[0x0]
    


class Index:
    Session_Type = 1575032
    Session_State = 1574589
    Session_Cache = 1574591

    Idle_Default=262145

    Cutscene_Parma1=2710132+3
    Cutscene_Parma2=1575079

