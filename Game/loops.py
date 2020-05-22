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

def loop(game):
    # Health loops
    if (game.player.health.current<0):
        game.player.dead = True # Yes this is the single check for death lol
        # Need to add more here...
        pass
    elif (game.player.health.poison>0):
        print(f'- You lost {game.player.health.poison} health to poison.')
        game.player.health -= game.player.poison
        pass
    elif (game.player.health.regen>0):
        print(f'+ You gained {game.player.health.regen} to regeneration.')
        game.player.health += game.player.poison
        pass
    # Stat loops
    game.player.health.boost = 0
    game.player.damage.boost = 0
    for item in game.player.inventory.get_equipped().values():
        if not (item==None):
            game.player.health.boost += item.health_boost
            game.player.damage.boost += item.damage_boost
