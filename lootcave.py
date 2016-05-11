from random import randint

class Player():
    # Health and shield
    health = 10
    health_current = 0
    shield = 5
    shield_current = 0

    # skills
    grenade = "Sticky Grenade"
    grenade_cooldown = 3
    grenade_timer = 0

    # Weapons and ammo
    # Primary
    primary = "Standard Auto Rifle"
    primary_ammo = 300
    primary_ammo_max = 300
    primary_clip = 30
    primary_clip_size = 30

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
    player_status = ""


class Enemy():
    # Enemy
    enemy_health_base = 10
    enemy_health_current = 0
    enemy_distance = ""

class Area():
    # Items dropped at the lootcave
    items_dropped = 0
    ammo_drop_primary = 0
    ammo_drop_special = 0
    ammo_drop_heavy = 0

def weaponlookup(weapon_type,weapon_name,max_clip,max_ammo,rarity,damage):
    print("Name: %s" % weapon_name)
    print("Type: %s" % weapon_type)
    print("Rarity: %s" % rarity)
    print("Damage: %d" % damage)

class Inventory():
    # Inventory of dropped engrams
    engram_green = 0

    temp_g = 0

    engram_blue = 0

    temp_b = 0

    engram_purple = 0

    temp_p = 0

p =  Player()
a = Area()
inv = Inventory()
p.health_current = p.health

weapons={
    "primary":{
        "Basic Handcannon":{"maxclip":10,"damage":45,"maxammo":100,"rarity":"Normal"},
        "Basic Auto Rifle":{},
    },
    "special":{
        "Basic Fusion Cannon":{},
    },
    "heavy":{
        "Basic Rocketlauncher":{},
    }
}

titan={
    "subclass":{},
    "grenade":{},
    "melee":{},
    "super":{},
}

ability_list = {
    "titan":{},
    "warlock":{},
    "hunter":{},
}

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
        temp_g = 0
        temp_b = 0
        temp_p = 0
        p.player_status = ""

def grenade():
    if p.grenade_timer == 0:
        print("You toss a %s!" % p.grenade)
        print("Dreg body parts fly everywhere")
        p.grenade_timer = p.grenade_cooldown
        if randint(1, 50) >= 20:
            a.items_dropped += 1
        else:
            return
    else:
        print("%s is not ready yet!" % p.grenade)

def fire_weapon():
    return

def list_equipment():
    print("Primary: %s" % p.primary)
    print("Special: %s" % p.special)
    print("Heavy: %s" % p.heavy)
    print("Headgear: %s" % p.head)
    print("Chest: %s" % p.body)
    print("Legs: %s" % p.legs)

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
            print("Not Implemented")
        elif i == "2":
            list_equipment()
        elif i == "3":
            print("Not Implemented")
        elif i == "4":
            p.player_status = ""
        else:
            print("Invalid Selection")