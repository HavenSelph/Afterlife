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
from .objects import SaveGame
from .gamesl import save as g_save
from .gamesl import load as g_load
from os import get_terminal_size
from os import system
from colorama import init as color
color()
from colorama import Fore
from pathlib import Path

def clearscreen():
    system('cls')

def choices(choices):
    while True:
        clearscreen()
        print(f'{Fore.BLUE}Welcome To Afterlife!\n')
        for i, choice in enumerate(choices):
            print(f'{i+1}. {Fore.BLUE}{choice}')
        print('\n')
        userin = input('>>>')
        for i, choice in enumerate(choices):
            if (userin.lower() == choice.lower()) or (userin==str(i+1)):
                return i

def setup():
    # Having trouble adding this at the moment 
    if Path(f"{Path().resolve()}\\SaveGames\\save.alsave").exists():
        while True:
            clearscreen()
            print('Hey! We found a savegame, are you sure you want to overwrite it?')
            userin = input('(Y/N) >>> ')
            if userin.lower() in ('y','n'):
                if (userin.lower()=='y'):
                    break
                else:
                    return 'NULL'
            else:
                continue
    while True:
        clearscreen()
        userin = input('Please name your world:\n>>> ')
        if (len(userin)>3):
            gname = userin
            break
    while True:
        clearscreen()
        userin = input('Please choose a seed (numbers only):\n>>> ')
        try:
            int(userin)
        except ValueError:
            continue
        else:
            mseed = userin
            break
    while True:
        clearscreen()
        userin = input('Please name your character:\n>>> ')
        if (len(userin)>3):
            pname = userin
            break
    return gname, pname, mseed

def mainmenu():
    userin = choices(('New', 'Load', 'Exit'))
    if (userin==0):
        game = setup()
        if (game=='NULL'):
            return game
        game = SaveGame(*game)
        g_save(game)
        return game
    elif (userin==1):
        clearscreen()
        print('Loading savegame...')
        game = g_load()
        if not game:
            input('No savegame was found...')
            return 'NULL'
        return game
#    elif (userin==2):
#        print('Settings')
    elif (userin==2):
        exit()
