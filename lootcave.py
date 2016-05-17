from random import randint


class Player:
    # Health and shield
    health = 10
    health_current = 0
    shield = 5
    shield_current = 0
    level = 0
    experience = 0
    light_level = 0
    damage = 0

    # skills
    grenade = "Sticky Grenade"
    grenade_cooldown = 3
    grenade_timer = 0

    # Weapons and ammo
    # Primary
    primary = ""
    primary_ammo = 0
    primary_ammo_max = 0
    primary_clip = 0
    primary_clip_size = 0

    # Special
    special = ""
    special_ammo = 0
    special_ammo_max = 0
    special_clip = 0
    special_clip_size = 0

    # Heavy
    heavy = ""
    heavy_ammo = 0
    heavy_ammo_max = 0
    heavy_clip = 0
    heavy_clip_size = 0

    currently_equipped = ""
    currently_equipped_stats = {"current_clip": 0,
                                "max_clip": 0,
                                "current_ammo": 0,
                                "max_ammo": 0,
                                "damage": 0,
                                "type": ""}

    # Armor
    head = ""
    head_def = 0
    head_light = 0
    body = ""
    body_def = 0
    body_light = 0
    legs = ""
    legs_def = 0
    legs_light = 0

    # What is the player doing
    player_position = ""
    # what is the player doing
    player_status = ""


class Enemy:
    # Enemy
    enemy_health_base = 10
    enemy_health_current = 0
    enemy_distance = ""


class Area:
    # Items dropped at the lootcave
    items_dropped = 0
    ammo_drop_primary = 0
    ammo_drop_special = 0
    ammo_drop_heavy = 0


class Inventory:
    # Inventory of dropped engrams
    engram_green = 0

    temp_g = 0

    engram_blue = 0

    temp_b = 0

    engram_purple = 0

    temp_p = 0

p = Player()
a = Area()
inv = Inventory()
p.health_current = p.health

weapons = {
    "primary": {
        "Basic Handcannon": {"maxclip": 10, "damage": 45, "maxammo": 100, "rarity": "Normal", "type": "Handcannon"},
        "Basic Auto Rifle": {"maxclip": 30, "damage": 24, "maxammo": 300, "rarity": "Normal", "type": "Auto Rifle"},
    },
    "special": {
        "Basic Fusion Cannon": {},
    },
    "heavy": {
        "Basic Rocketlauncher": {},
    }
}

classes = {
    "titan": {
        "striker": {"grenade": {}, "melee": {}, "super": {}, },
        "defender": {"grenade": {}, "melee": {}, "super": {}, },
        "solhammer": {"grenade": {}, "melee": {}, "super": {}, }
        },
    "warlock": {
        "sunsigner": {"grenade": {}, "melee": {}, "super": {}, },
        "voidwalker": {"grenade": {}, "melee": {}, "super": {}, },
        "stormcaller": {"grenade": {}, "melee": {}, "super": {}, }
        },
    "hunter": {
        "voidstalker": {"grenade": {}, "melee": {}, "super": {}, },
        "stormblade": {"grenade": {}, "melee": {}, "super": {}, },
        "gunslinger": {"grenade": {}, "melee": {}, "super": {}, },
        }

}

player_inventory = {
    "primary_inventory": [],
    "special_inventory": [],
    "heavy_inventory": [],
    "consumable_inventory": {"item1": 0}
}

comsumables = {}

tower_vault = {
    "weapon": {},
    "armor": {},
    "other": {}
}


# Search for items on the ground after killing enemies in the lootcave
def search_ground():
    print("You search on the ground for all the sweet sweet loot!")
    if a.items_dropped < 1:
        print("Looks like nothing has dropped yet.")
    else:
        while a.items_dropped > 0:
            i = randint(1, 100)
            if i < 70:
                a.items_dropped -= 1
                inv.temp_g += 1
                inv.engram_green += 1
            elif i < 90:
                a.items_dropped -= 1
                inv.temp_b += 1
                inv.engram_blue += 1
            else:
                a.items_dropped -= 1
                inv.temp_p += 1
                inv.engram_purple += 1
        print("You gathered: %d Green engrams, %d Blue Engrams and %d Purple Engrams" %
              (inv.temp_g, inv.temp_b, inv.temp_p))
        inv.temp_g = 0
        inv.temp_b = 0
        inv.temp_p = 0
        p.player_status = ""


def check_engrams():
    print("You have: %d Green engrams, %d Blue Engrams and %d Purple Engrams" %
          (inv.engram_green, inv.engram_blue, inv.engram_purple))


# Throw grenade and check if you can throw
def grenade():
    if p.grenade_timer == 0:
        print("You toss a %s!" % p.grenade)
        print("Dreg body parts fly everywhere")
        p.grenade_timer = p.grenade_cooldown
        if randint(1, 50) >= 20:
            a.items_dropped += 1
    else:
        print("%s is not ready yet!" % p.grenade)


def fire_weapon():
    print("Fire weapon not implemented yet")


def check_ammo_equipping(weapon_type):
    if weapon_type == "primary":
        if p.primary_ammo > p.primary_clip_size:
            p.primary_clip = p.primary_clip_size
            p.primary_ammo -= p.primary_clip_size
        elif p.primary_ammo <= p.primary_clip_size:
            p.primary_clip = p.primary_ammo
            p.primary_ammo = 0
    elif weapon_type == "special":
        if p.special_ammo > p.special_clip_size:
            p.special_clip = p.special_clip_size
            p.special_ammo -= p.special_clip_size
        elif p.special_ammo <= p.special_clip_size:
            p.special_clip = p.special_ammo
            p.special_ammo = 0
    elif weapon_type == "heavy":
        if p.heavy_ammo > p.heavy_clip_size:
            p.heavy_clip = p.heavy_clip_size
            p.heavy_ammo -= p.heavy_clip_size
        elif p.heavy_ammo <= p.heavy_clip_size:
            p.heavy_clip = p.heavy_ammo
            p.heavy_ammo = 0


# Equip a specific weapon from inventory
def equip(weapon_type):
    while p.player_status == "equipping":
        if weapon_type == "primary":
            print(player_inventory["primary_inventory"])
            i = input("Type a name above>")
            wtype = player_inventory["primary_inventory"]
            if i == wtype:
                p.currently_equipped = wtype[i]
                p.primary = i
                p.primary_ammo_max = wtype[i]["maxammo"]
                p.primary_clip_size = wtype[i]["maxclip"]
                p.damage = wtype[i]["damage"]
                check_ammo_equipping("primary")
        elif weapon_type == "special":
            print("Special Equip not implemented yet")
        elif weapon_type == "heavy":
            print("Heavy Equip not implemented yet")


# Function for keeping track of the player's current
# location and able to go back to the previous location
def player_status_change(change_status, status):
    go_to = ""
    come_from = ""
    if change_status == "go":
        come_from = p.player_status
        go_to = status
        p.player_status = go_to
    elif change_status == "revert":
        p.player_status = come_from
        come_from = ""
        go_to = ""


# Swap between currently equipped weapons
def swap_weapon(weapon_type):
    if weapon_type == "primary":
        print("Swap Primary not implemented")
    if weapon_type == "special":
        print("Swap Special not implemented")
    if weapon_type == "heavy":
        print("Swap Heavy not implemented")


# List player's currently equipped gear
def list_equipment():
    print("Primary: %s" % p.primary)
    print("Special: %s" % p.special)
    print("Heavy: %s" % p.heavy)
    print("Headgear: %s" % p.head)
    print("Chest: %s" % p.body)
    print("Legs: %s" % p.legs)


def check_full(a):
    if a == "primary":
        b = len(player_inventory["primary_inventory"])
        if b >= 9:
            print("Primary Inventory full.")
            return True
        else:
            return False
    if a == "special":
        b = len(player_inventory["special_inventory"])
        if b >= 9:
            print("Special inventory full.")
            return True
        else:
            return False
    if a == "heavy":
        b = len(player_inventory["heavy_inventory"])
        if b >= 9:
            print("Heavy inventory full.")
            return True
        else:
            return False


def weaponlookup(weapon_name, weapon_type, rarity, damage, max_clip):
    print("Name: %s" % weapon_name)
    print("Type: %s" % weapon_type)
    print("Rarity: %s" % rarity)
    print("Damage: %d" % damage)
    print("Max Clip: %d" % max_clip)


def search_ammo():
    if a.ammo_drop_primary == 0 | a.ammo_drop_special == 0 | a.ammo_drop_heavy == 0:
        print("Looks like there is no ammo dropped")
    if p.primary_ammo < p.primary_ammo_max:
        if a.ammo_drop_primary > 0:
            p.primary_ammo += a.ammo_drop_primary
            if p.primary_ammo > p.primary_ammo_max:
                p.primary_ammo = p.primary_ammo_max
    if p.special_ammo < p.special_ammo_max:
        if a.ammo_drop_special > 0:
            p.special_ammo += a.ammo_drop_special
            if p.special_ammo > p.special_ammo_max:
                p.special_ammo = p.special_ammo_max
    if p.heavy_ammo < p.heavy_ammo_max:
        if a.ammo_drop_heavy > 0:
            p.heavy_ammo += a.ammo_drop_heavy
            if p.heavy_ammo > p.heavy_ammo_max:
                p.heavy_ammo = p.heavy_ammo_max
    print("You start looking for ammo")


def player_ui():
    print("Heath: %d/%d, Shield: %d/%d, ""Weapon: %s, Clip: %d/%d, Ammo: %d/%d" %
          (p.health_current,
           p.health,
           p.shield_current,
           p.shield, p.currently_equipped,
           p.currently_equipped_stats["current_clip"],
           p.currently_equipped_stats["max_clip"],
           p.currently_equipped_stats["current_ammo"],
           p.currently_equipped_stats["max_ammo"],))


print("Welcome to Destiny Loot cave")

while p.health_current > 0:
    print("What would you like to do?")
    while p.player_status == "":
        i = input("[1]Start Shooting, [2]Decrypt, [3]Search, [4]menu>")
        if i == "1":
            print("You make your way to the illustrious Loot Cave")
            p.player_status = "shooting"
        elif i == "2":
            print("You travel back to the Tower")
            print("You stand in front of the devious Cryptarch")
            p.player_status = "decrypting"
        elif i == "3":
            search_ground()
        elif i == "4":
            p.player_status = "viewingmenu"
        else:
            print("Please use one of the numbers listed.")
    while p.player_status == "shooting":
        print("You ready your weapon.")
        i = input("[1]fire weapon, [2]Grenade, [3]Switch weapon, [4]Look for ammo, [5]Done with loot cave> ")
        if p.grenade_timer > 0:
            p.grenade_timer -= 1
        if i == "1":
            if p.currently_equipped == "primary":
                if p.primary_clip > 0:
                    p.primary_clip -= 1
                    print("You let off a %s round" % p.primary)
                else:
                    print("Looks like I need to reload")
                    if p.primary_ammo > p.primary_clip_size:
                        p.primary_ammo -= p.primary_clip_size
                    else:
                        print("You are out of ammo!")
                        print("You will need to look for more or change weapons.")
            if p.currently_equipped == "special":
                if p.special_clip > 0:
                    p.special_clip -= 1
                    print("You let off a %s round" % p.special)
                else:
                    print("Looks like I need to reload.")
                    if p.special_ammo > p.special_clip_size:
                        p.special_ammor = p.special_ammo - p.special_clip_size
                    else:
                        print("You are out of ammor!")
                        print("You will need to look for more or change weapons.")
            if p.currently_equipped == "heavy":
                if p.heavy_clip > 0:
                    p.heavy_clip -= 1
                    print("You let off a %s round" % p.heavy)

                    if randint(1, 10) > 3:
                        a.items_dropped += int(randint(1, 3))
                else:
                    print("Looks like I need to reload")
                    if p.heavy_ammo > p.heavy_clip_size:
                        p.heavy_ammo -= p.heavy_clip_size
                    else:
                        print("You are out of ammor!")
                        print("You will need to look for more or change weapons.")
        elif i == "2":
            grenade()
        elif i == "3":
            print("You chose 3")
        elif i == "4":
            search_ammo()
        elif i == "5":
            p.player_status = ""
    while p.player_status == "decrypting":
        if inv.engram_green == 0 & inv.engram_blue == 0 & inv.engram_purple == 0:
            print("You don't have any items to decrypt!")
            print("You travel back to the Loot Cave.")
            p.player_status = ""
        else:
            print("Not Implemented Yet")
            print("You travel back to the Loot Cave.")
            p.player_status = ""
    while p.player_status == "shopping":
        print("Shopping Not Implemented yet")
        print("You travel back to the loot cave.")
        p.player_status = ""
    while p.player_status == "viewingmenu":
        i = input("[1]Stats, [2]Equipment, [3]Inventory, [4]Leave Menu")
        if i == "1":
            print("Not Implemented(Stats)")
        elif i == "2":
            list_equipment()
            p.player_status = "equipment"
        elif i == "3":
            print("Not Implemented(Inventory)")
        elif i == "4":
            p.player_status = ""
        else:
            print("Invalid Selection")
    while p.player_status == "equipment":
        i = input("[1]Weapon, [2]Armor")
        if i == "1":
            print("What would you like to look up?")
            i = input("[1]Primary, [2]Special, [3]Heavy, [4]Go Back")
            if i == "1":
                weaponlookup(p.primary, "Primary", weapons["primary"][p.primary]["rarity"],
                             weapons["primary"][p.primary]["damage"], weapons["primary"][p.primary]["maxclip"])
            elif i == "2":
                weaponlookup(p.special, "Special", weapons["special"][p.special]["rarity"],
                             weapons["special"][p.special]["damage"], weapons["special"][p.special]["maxclip"])
            elif i == "3":
                weaponlookup(p.heavy, "Heavy", weapons["heavy"][p.heavy]["rarity"],
                             weapons["heavy"][p.heavy]["damage"], weapons["heavy"][p.heavy]["maxclip"])
            elif i == "4":
                p.player_status = "viewingmenu"
            else:
                print("invalid selection")
