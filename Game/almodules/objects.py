"""
MIT License

Copyright (c) 2020 Haven Selph

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
# Extra stuff needed at the top
class Equipped():
    def __init__(self):
        self.helmet = None
        self.chestplate = None
        self.leggings = None
        self.weapon = None

class LootTable():
    def __init__(self, *items):
        super().__init__()
        for item in items:
            self[item.name] = (item, item.chance, item.range)

class Health():
    def __init__(self, hp=100):
        self.current = hp
        self.base = hp
        self.boost = 0
        self.regen = 0
        self.poison = 0

class Damage():
    def __init__(self, dp=10):
        self.current = dp
        self.base = dp
        self.boost = 0

class Base():
    def __init__(self, name, hp, bd, lt):
        self.name = name
        self.health = Health(hp)
        self.damage = Damage(bd)
        self.loot_table = LootTable(lt)

# Constructors
class Item():
    class Armor():
        def __init__(self, name: str, ep: int, hb: int=0, db: int=0):
            self.name = name
            self.health_boost = hb
            self.damage_boost = db
            if ep in range(0,3):
                self.equip_place = ep
            else:
                raise ValueError(f'Equipment Place invalid!\nEquipment in question: {self.name}\nEP value: {ep}')
            self.equpied = False
    class Weapon():
        def __init__(self, name: str, hb: int=0, db: int=0):
            self.name = name
            self.health_boost = hb
            self.damage_bost = db
            self.equiped = False
    class Coin():
        def __init__(self, value: int):
            self.value = value

class NPC():
    class Wild():
        class Wolf(Base):
            def __init__(self):
                self.equipped = Equipped()
                self.hostility = 0.2
    class Undead():
        class Zombie(Base):
            def __init__(self):
                pass
    class Bandit(Base):
        class Thief():
            def __init__(self):
                pass

# Inventory
class Inventory(dict):
    def __init__(self):
        super().__init__()
        self.size = 100
        self.equipped = Equipped()
    
    def add(self, key, obj):
        if len(self.keys()>=size):
            return False
        else:
            self[key] = obj
            return True

    def remove(self, key):
        if (key in self.keys()):
            del self[key]
            return True
        else:
            return False
    
    def get_all(self):
        return self.keys()

    def equip(self, key):
        try:
            self[key].equipped = True
            if (self[key].ep==0):
                self.equipped.helmet = self[key]
            elif (self[key].ep==1):
                self.equipped.chestplate = self[key]
            elif (self[key].ep==2):
                self.equipped.leggins = self[key]
            elif (self[key].ep==3):
                self.equipped.weapon = self[key]
        except ValueError:
            return False
        else:
            return True

    def get_equipped(self):
        return {'Helmet':self.equipped.helmet,'Chestplate':self.equipped.chestplate,'Leggings':self.equipped.leggings,'Weapon':self.equipped.weapon}

# Player
class Player():
    def __init__(self, pname):
        self.name = pname
        self.type = None
        self.dead = False # If you want to cheat and disable hardcore mode, ~/loops has the check for death
        # Health Stats
        self.health = Health()
        # Damage Stats
        self.damage = Damage()
        self.damage.current = 0
        self.damage.base = 0
        self.damage.boost = 0
        # Balance Stats
        self.balance = 0
        self.inventory = Inventory()

# Gamemap
class GameMap():
    def __init__(self, mseed):
        self.seed = mseed

# All objects
class SaveGame():
    def __init__(self, version, gname, pname, mseed):
        self.version = version
        self.name = gname
        self.player = Player(pname)
        self.map = GameMap(mseed)
