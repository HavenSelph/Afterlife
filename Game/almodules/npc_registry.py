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

class Equipped():
    def __init__(self):
        self.helmet = None
        self.chestplate = None
        self.leggings = None
        self.weapon = None


id_sys = DynamicID('NPC')

def get_id_setup():
    global id_sys
    return id_sys

class NPC():
    class Wild():
        class Wolf():
            def __init__(self):
                self.id = get_id_setup().get_id('Wolf')
                self.hostility = 1
        class Bear():
            def __init__(self):
                self.id = get_id_setup().get_id('Bear')
                self.hostility = 1

    class Undead():
        class Zombie():
            def __init__(self):
                self.id = get_id_setup().get_id('Zombie')
                self.equipped = Equipped()
        class Skeleton():
            def __init__(self):
                self.id = get_id_setup().get_id('Skeleton')
                self.equipped = Equipped()

    class Bandit():
        class Thief():
            def __init__(self):
                self.id = get_id_setup().get_id('Thief')
                self.equipped = Equipped()

npc_registry = []
npc_registry.append(id_sys)
npc_registry.append(NPC.Wild.Wolf())
npc_registry.append(NPC.Wild.Bear())
npc_registry.append(NPC.Undead.Zombie())
npc_registry.append(NPC.Undead.Skeleton())
npc_registry.append(NPC.Bandit.Thief())

def get_registry():
    global npc_registry
    global id_sys
    for item in npc_registry[1:]:
        print(f'{id_sys[item.id]} : {item.id}\n')
    return npc_registry