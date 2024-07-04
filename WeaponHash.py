
from KeyBindings import GameKeyBindings

class Melee:
    Dagger = "weapon_dagger"
    Bat = "weapon_bat"
    Bottle = "weapon_bottle"
    Crowbar = "weapon_crowbar"
    Unarmed = "weapon_unarmed"
    Flashlight = "weapon_flashlight"
    Golfclub = "weapon_golfclub"
    Hammer = "weapon_hammer"
    Hatchet = "weapon_hatchet"
    Knuckle = "weapon_knuckle"
    Knife = "weapon_knife"
    Machete = "weapon_machete"
    Switchblade = "weapon_switchblade"
    Nightstick = "weapon_nightstick"
    Wrench = "weapon_wrench"
    Battleaxe = "weapon_battleaxe"
    Poolcue = "weapon_poolcue"
    Stone_hatchet = "weapon_stone_hatchet"
    __type__=GameKeyBindings.Weapons.Melee_weapon


class Pistols:
    Pistol = "weapon_pistol"
    MK2_Pistol = "weapon_pistol_mk2"
    CombatPistol = "weapon_combatpistol"
    AP_Pistol = "weapon_appistol"
    StunGun = "weapon_stungun"
    Pistol50 = "weapon_pistol50"
    SNS_Pistol = "weapon_snspistol"
    MK2_SNS_Pistol = "weapon_snspistol_mk2"
    HeavyPistol = "weapon_heavypistol"
    VintagePistol = "weapon_vintagepistol"
    FlareGun = "weapon_flaregun"
    MarksmanPistol = "weapon_marksmanpistol"
    Revolver = "weapon_revolver"
    MK2_Revolver = "weapon_revolver_mk2"
    DoubleAction_Revolver = "weapon_doubleaction"
    RayPistol = "weapon_raypistol"
    CeramicPistol = "weapon_ceramicpistol"
    NavyRevolver = "weapon_navyrevolver"
    GadgetPistol = "weapon_gadgetpistol"
    StunGun_MP = "weapon_stungun_mp"
    __type__=GameKeyBindings.Weapons.Pistol


class MachineGuns:
    Microsmg = "weapon_microsmg"
    Smg = "weapon_smg"
    Smg_mk2 = "weapon_smg_mk2"
    Assaultsmg = "weapon_assaultsmg"
    Combatpdw = "weapon_combatpdw"
    Machinepistol = "weapon_machinepistol"
    Minismg = "weapon_minismg"
    Gusenberg = "weapon_gusenberg"
    Tecpistol = "weapon_tecpistol"
    Mg = "weapon_mg"
    Combatmg = "weapon_combatmg"
    Combatmg_mk2 = "weapon_combatmg_mk2"
    Raycarbine = "weapon_raycarbine"
    __type__=GameKeyBindings.Weapons.Machine_gun


class Shotguns:
    Pumpshotgun = "weapon_pumpshotgun"
    Pumpshotgun_mk2 = "weapon_pumpshotgun_mk2"
    Sawnoffshotgun = "weapon_sawnoffshotgun"
    Assaultshotgun = "weapon_assaultshotgun"
    Bullpupshotgun = "weapon_bullpupshotgun"
    Musket = "weapon_musket"
    Heavyshotgun = "weapon_heavyshotgun"
    Dbshotgun = "weapon_dbshotgun"
    Autoshotgun = "weapon_autoshotgun"
    Combatshotgun = "weapon_combatshotgun"
    __type__=GameKeyBindings.Weapons.Shot_gun


class AssaultRifles:
    Assaultrifle = "weapon_assaultrifle"
    Assaultrifle_mk2 = "weapon_assaultrifle_mk2"
    Carbinerifle = "weapon_carbinerifle"
    Carbinerifle_mk2 = "weapon_carbinerifle_mk2"
    Advancedrifle = "weapon_advancedrifle"
    Specialcarbine = "weapon_specialcarbine"
    Specialcarbine_mk2 = "weapon_specialcarbine_mk2"
    Bullpuprifle = "weapon_bullpuprifle"
    Bullpuprifle_mk2 = "weapon_bullpuprifle_mk2"
    Compactrifle = "weapon_compactrifle"
    Militaryrifle = "weapon_militaryrifle"
    Heavyrifle = "weapon_heavyrifle"
    Tacticalrifle = "weapon_tacticalrifle"
    __type__=GameKeyBindings.Weapons.Rifle


class SniperRifles:
    Sniperrifle = "weapon_sniperrifle"
    Heavysniper = "weapon_heavysniper"
    Heavysniper_mk2 = "weapon_heavysniper_mk2"
    Marksmanrifle = "weapon_marksmanrifle"
    Marksmanrifle_mk2 = "weapon_marksmanrifle_mk2"
    Precisionrifle = "weapon_precisionrifle"
    __type__=GameKeyBindings.Weapons.Sniper

    


class HeavyWeapons:
    Rpg = "weapon_rpg"
    Grenadelauncher = "weapon_grenadelauncher"
    Grenadelauncher_smoke = "weapon_grenadelauncher_smoke"
    Minigun = "weapon_minigun"
    Firework = "weapon_firework"
    Railgun = "weapon_railgun"
    Hominglauncher = "weapon_hominglauncher"
    Compactlauncher = "weapon_compactlauncher"
    Rayminigun = "weapon_rayminigun"
    Emplauncher = "weapon_emplauncher"
    __type__=GameKeyBindings.Weapons.Heavy_weapon



class Throwables:
    Grenade = "weapon_grenade"
    Bzgas = "weapon_bzgas"
    Molotov = "weapon_molotov"
    Stickybomb = "weapon_stickybomb"
    Proxmine = "weapon_proxmine"
    Snowball = "weapon_snowball"
    Pipebomb = "weapon_pipebomb"
    Ball = "weapon_ball"
    Smokegrenade = "weapon_smokegrenade"
    Flare = "weapon_flare"
    __type__=GameKeyBindings.Weapons.Special_weapon

all_weapons = {
    "Pistols": Pistols,
    "MachineGuns": MachineGuns,
    "Melee": AssaultRifles,
    "AssaultRifles": SniperRifles,
    "Melee": Melee,
    "Shotguns": Shotguns,
    "HeavyWeapons": HeavyWeapons,
    "Throwables": Throwables,
    
}
def joatt(statName):
    hash = 0

    for c in statName.lower():
        hash += ord(c)
        hash &= 0xFFFFFFFF
        hash += (hash << 10) & 0xFFFFFFFF
        hash &= 0xFFFFFFFF
        hash ^= (hash >> 6) & 0xFFFFFFFF
        hash &= 0xFFFFFFFF

    hash += (hash << 3) & 0xFFFFFFFF
    hash &= 0xFFFFFFFF
    hash ^= (hash >> 11) & 0xFFFFFFFF
    hash &= 0xFFFFFFFF
    hash += (hash << 15) & 0xFFFFFFFF
    hash &= 0xFFFFFFFF
    return hash & 0xFFFFFFFF

def calculate_hash(type):
    for key, name in vars(type).items():
        if key.startswith("__"):
            continue
        setattr(type, key, joatt(name))


def init():
    calculate_hash(Melee)
    calculate_hash(Pistols)
    calculate_hash(Shotguns)
    calculate_hash(MachineGuns)
    calculate_hash(AssaultRifles)
    calculate_hash(HeavyWeapons)
    calculate_hash(Throwables)


def get_weapon_type(value):
    # 遍历所有的类
    for weapon_name, weapon_obj in all_weapons.items():
        # 获取当前类的所有属性
        weapon_attrs = dir(weapon_obj)
        #print(weapon_attrs)
        # 检查该值是否在当前类中
        if value in [joatt(getattr(weapon_obj, attr)) for attr in weapon_attrs if not attr.startswith("__")]:
            return weapon_obj.__type__
    # 如果值不在任何一个类中，则返回 None
    return GameKeyBindings.Weapons.Pistol