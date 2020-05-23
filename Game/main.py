version = '0.0.5c'

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
# This file is mainly intended as a gameplay loop.
from loops import loop
from os import system
from time import sleep
from almodules.mainmenu import mainmenu
from almodules.gamesl import save
def clearscreen():
    system('cls')

from os import get_terminal_size
if (get_terminal_size()[0]<30) or (get_terminal_size()[1]<10):
    print('Oops!\nIt looks like your terminal is a little too small. Please consider making it bigger so you can enjoy a better experience.')
    input('...')

try:
    clearscreen()
    game = 'NULL'
    print(f'If you wish to leave, please use CTRL + C')
    print(f'Please keep in mind this game is in it\'s early stages.')
    print(f'Some if not all features will be unstable and or possibly removed.')
    print(f'Report bugs to the GitHub page, or on the Repl.it page please.','\n'*2)
    input('Press enter to continue...')
    clearscreen()
    while (game=='NULL'):
        game = mainmenu(version)
    while True:
        loop(game)
        pass

# Errors
except AttributeError as e:
    print('This likely results from your savegame being outdated. Please make a new game.')
    print('Screenshot this code and send it to my Repl.it and/or Github.', '\n'*2)
    print(e)

# Exits
except KeyboardInterrupt:
    print('Closing down game...')
    if not (game=='NULL'): # Check if game has been setup
        save(game)

except SystemExit:
    print('Closing down game...')
    if not (game=='NULL'): # Check if game has been setup
        save(game)
