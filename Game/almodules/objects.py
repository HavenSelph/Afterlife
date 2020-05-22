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

class GameMap():
    def __init__(self, mseed):
        self.seed = mseed

class Inventory(dict):
    def __init__(self):
        super().__init__()
        self.size = 100
    
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

    def getall(self):
        return self.keys()

class Player():
    def __init__(self, pname):
        self.name = pname
        self.type = None
        self.dead = False # If you want to cheat and disable hardcore mode, ~/loops has the check for death
        self.health = 100
        self.regen = 0
        self.poison = 0
        self.balance = 0
        self.inventory = Inventory()


class SaveGame():
    def __init__(self, version, gname, pname, mseed):
        self.version = version
        self.name = gname
        self.player = Player(pname)
        self.map = GameMap(mseed)
