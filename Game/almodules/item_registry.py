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

class DynamicID(dict):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.id = 0
    def get_id(self, name):
        self[name] = self.id
        self[self.id] = name
        self.id += 1
        return self[name]

id_sys = DynamicID('NPC')

def get_id_setup():
    global id_sys
    return id_sys

class Item():
    class Armor():
        def __init__(self, name: str, ep: int, hb: int=0, db: int=0, ap: int=0):
            self.id = get_id_setup().get_id(name)
            self.name = name
            self.health_boost = hb
            self.damage_boost = db
            self.armor_boost = ab
            if ep in range(0,3):
                self.equip_place = ep
            else:
                raise ValueError(f'Equipment Place invalid!\nEquipment in question: {self.name}\nEP value: {ep}')
            self.equpied = False
    class Weapon():
        def __init__(self, name: str, hb: int=0, db: int=0):
            self.id = get_id_setup().get_id(name)
            self.name = name
            self.health_boost = hb
            self.damage_bost = db
            self.equiped = False
    class Coin():
        def __init__(self, name, value: int):
            self.id = get_id_setup().get_id(name)
            self.value = value

"""
ep = equipment place [0 Helmet, 1 Chestplate, 2 Pants, 3 Boots, 4 Weapon]

hb = healthboost
db = damageboost
ab = armorboost
"""

item_registry = [id_sys]
item_registry.append(Item.Armor('Wooden Helmet', 0, 0, 0, 1))