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
            self[item.id] = LootTable.build(*items)
    @classmethod
    def build(cls, *itmes):
        return [(a, b, c) for (a, b, c) in (items)]

id_sys = DynamicID('NPC')

def get_id_setup():
    global id_sys
    return id_sys

class NPC():
    class Wild():
        def __init__(self, name, health_points, armor_points, damage_points, neutrality, loot_table):
            # Prime
            self.name = name
            self.health_points = health_points
            self.armor_points = armor_points
            self.damage_points = damage_points
            self.neutrality = neutrality
            self.loot_table = LootTable()

            # Final
            self.id = get_id_setup().get_id(self)            

    class Undead():
        def __init__(self, name, health_points, armor_points, damage_points, neutrality, loot_table):
            # Prime
            self.name = name
            self.health_points = health_points
            self.armor_points = armor_points
            self.damage_points = damage_points
            self.neutrality = neutrality
            self.loot_table = LootTable()

            # Final
            self.id = get_id_setup().get_id(self)

    class Bandit():
        def __init__(self, name, health_points, armor_points, damage_points, neutrality, loot_table):
            # Prime
            self.name = name
            self.health_points = health_points
            self.armor_points = armor_points
            self.damage_points = damage_points
            self.neutrality = neutrality
            self.loot_table = LootTable()

            # Final
            self.id = get_id_setup().get_id(self)

npc_registry = [id_sys]
npc_registry.append(NPC.Wild('Wolf', 20, 1, 2, 1, 'NULL'))
npc_registry.append(NPC.Wild('Bear', 50, 1, 2, 2, 'NULL'))
npc_registry.append(NPC.Undead('Zombie', 20, 2, 1, 2, 'NULL'))
npc_registry.append(NPC.Undead('Skeleton', 20, 1, 1, 2, 'NULL'))
npc_registry.append(NPC.Bandit('Thief', 20, 1, 1, 2, 'NULL'))

def get_registry():
    global npc_registry
    return npc_registry