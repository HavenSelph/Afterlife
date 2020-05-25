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
from random import randint

def loop(game):
    # Stat loops
    game.player.health.modifier = 0
    game.player.damage.modifier = 0
    game.player.armor.modifier = 0
    for item in game.player.inventory.equipped.all.values():
        if not (item==None):
            try:
                game.player.armor.modifier += item.armor_modifier
                game.player.health.modifier += item.health_modifier
                game.player.damage.modifier += item.damage_modifier 
            except ValueError:
                pass
    game.player.health.calculate()

    # Encounters
    if (x:=randint(0,5)==0):
        print('Nothing happen')
    elif (x==1):
        print('Nothing happened')
    elif (x==2):
        print('Nothing happened')
    elif (x==3):
        print('Nothing happened')
    elif (x==4):
        print('Nothing happened')
    elif (x==5):
        print('Nothing happened')
    input()    
