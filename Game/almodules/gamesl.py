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
from os import system
import pickle
from pathlib import Path

def clearscreen():
    system('cls')


def save(game):
    with open(f"{Path().resolve()}\\SaveGames\\save.alsave", "wb") as algs:
        pickle.dump(game, algs, protocol=pickle.HIGHEST_PROTOCOL)

def load(version='NULL'):
    try:
        with open(f"{Path().resolve()}\\SaveGames\\save.alsave", "rb") as algs:
            game = pickle.load(algs)
    except FileNotFoundError as e:
        print(e)
        input()
        return False
    else:
        if not (game.version==version) and not (version=='NULL'):
            while True:
                clearscreen()
                print('This save is outdated and some features likely will not work. Are you sure you wish to load it?')
                userin = input('(Y/N) >>> ')
                if userin.lower() in ('y','n'):
                    if (userin.lower()=='y'):
                        game.outdated = True
                        return game
                    else:
                        return 'NULL'
        return game