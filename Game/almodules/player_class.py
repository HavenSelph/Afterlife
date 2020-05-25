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
# Subs
class Health():
    def __init__(self, health_points=100):
        self.base = health_points
        self.modifier = 0
        self.current = self.base + self.modifier
        self.regen = 0
        self.poison = 0

    def calculate(self):
        self.current += self.regen if ((self.regen + self.current)<=self.max) else (self.max)
        self.current -= self.poison
        if (self.current <= 0):
            self.dead = True

    @property
    def max(self):
        return self.base + self.modifier

class Armor():
    def __init__(self, armor_points=0):
        self.armor = armor_points
        self.armor_boost = 0
    
    @property
    def current(self):
        return self.armor + self.armor_boost

class Damage():
    def __init__(self, damage_points=10):
        self.base = damage_points
        self.boost = 0
    
    @property
    def current(self):
        return self.base + self.boost

# Inventory management (by me)
class Equipped():
    def __init__(self):
        self.helmet = None
        self.chestplate = None
        self.leggings = None
        self.weapon = None

    @property
    def all(self):
        return {'Helmet':self.helmet,'Chestplate':self.chestplate,'Leggings':self.leggings,'Weapon':self.weapon}

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
        self[key].equipped = True
        if (self[key].ep==0):
            self.equipped.helmet = self[key]
        elif (self[key].ep==1):
            self.equipped.chestplate = self[key]
        elif (self[key].ep==2):
            self.equipped.leggins = self[key]
        elif (self[key].ep==3):
            self.equipped.weapon = self[key]

class Player():
    def __init__(self, pname):
        # Initial
        self.name = pname

        # Stat Priming
        # -- health
        self.health = Health()
        
        # -- armor
        self.armor = Armor()

        # -- damage
        self.damage = Damage()

        # -- inventory
        self.inventory = Inventory()