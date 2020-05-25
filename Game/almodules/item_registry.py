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
    def get_id(self, object):
        self[self.id] = object
        self[object.name] = object
        self.id += 1
        return self.id - 1

id_sys = DynamicID('NPC')

def get_id_setup():
    global id_sys
    return id_sys

class Item():
    class Armor():
        def __init__(self, name: str, equip_place: int, health_modifier: int=0, armor_modifier: int=0, damage_modifier: int=0):
            self.name = name
            self.health_modifier = health_modifier
            self.armor_modifier = armor_modifier
            self.damage_modifier = damage_modifier
            if equip_place in (0,1,2,3):
                self.equip_place = equip_place
            else:
                print('Bad item! Please screenshchot below error:')
                raise ValueError(f'Equipment Place invalid!\nEquipment in question: {self.name}\nEP value: {equip_place}')
            self.equipped = False
            self.id = get_id_setup().get_id(self)
        
    class Weapon():
        def __init__(self, name: str, health_modifier: int=0, damage_modifier: int=0):
            self.name = name
            self.health_modifier = health_modifier
            self.damage_modifier = damage_modifier
            self.equip_place = 4
            self.equiped = False
            self.id = get_id_setup().get_id(self)
        
    class Coin():
        def __init__(self, name, value: int):
            self.name = name
            self.value = value
            self.id = get_id_setup().get_id(self)

"""
ep = equipment place [0 Helmet, 1 Chestplate, 2 Pants, 3 Boots, 4 Weapon]

hb = healthboost
db = damageboost
ab = armorboost
"""

item_registry = [id_sys]
item_registry.append(Item.Armor('Cloth Hat', 0, 0, 1, 0))
item_registry.append(Item.Armor('Cloth Shirt', 1, 0, 1, 0))
item_registry.append(Item.Armor('Cloth Leggings', 2, 0, 1, 0))
item_registry.append(Item.Armor('Cloth Sandals', 3, 0, 1, 0))
item_registry.append(Item.Weapon('Small Dagger', 0, 2))
# item_registry.append(Item.)

def get_registry():
    global item_registry
    return item_registry