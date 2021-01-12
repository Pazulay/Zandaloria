# Zandaloria
# Made by Pedro A.

import time
import cmd
import textwrap
import sys
import os
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.maxhp = 100
        self.hp = self.maxhp
        self.items = ['potion']
        self.weapons = []
        self.currentWeap = 'wood sword'
        self.gold = 10
        self.baseattack = 10


#Enemies

class Slime:
    def __init__(self, name):
        self.name = name
        self.maxhp = 40
        self.hp = self.maxhp
        self.golddrop = 20
        self.attackdmg = 5

testslime = Slime('slimer')



class troll:
    def __init__(self):
        pass



class skeleton:
    def __init__(self):
        pass


#tresures

def treasure1():
    pass



def titlescreen():
    os.system('cls')
    print('###########################')
    print('#                         #')
    print('#                         #')
    print('#          Start          #')
    print('#          Leave          #')
    print('#                         #')
    print('#                         #')
    print('###########################')
    playeroptions = input('> ')
    if playeroptions.lower() == 'start':
        startgame()
    elif playeroptions.lower() == 'leave':
        exitgame()
    else:
        print('\n')
        print(f'"{playeroptions}" is not a valid command. Try using "start" or "leave"')
        print('\n')
        time.sleep(3.0)
        titlescreen()

def startgame():
    print('Hello Adventurer. Welcome to Zandaloria')
    print('\n')
    time.sleep(1.0)
    print('What is your name?')
    print('\n')
    playername = input('> ')
    global player1
    player1 = Player(playername)
    zandaloria()

def zandaloria():
    os.system('cls')
    print('You are in Zandaloria')
    print('You can either go to the left or to the right.')
    print('Where do you want to go? (Type the option number)')
    print('[1] Left Path (Griffon Road)')
    print('[2] Right Path (Dalton Road)')
    playeroptions = input('> ')
    if playeroptions == '1':
        griffonroad()
    elif playeroptions == '2':
        daltonroad()
    else:
        print(f'"{playeroptions}" is not an option. Choose one of the options listed.')
        time.sleep(2.0)
        zandaloria()

def griffonroad():
    os.system('cls')
    print('You are now in Griffon Road')
    print('What do you want to do? Type one of the options')
    print('[1] Go back to Zandaloria')
    print('[2] Continue on the path.')
    playeroptions = input('> ')
    if playeroptions == '1':
        zandaloria()
    elif playeroptions == '2':
        dice = random.randrange(1, 3)
        if dice == 2:
            fork1()
        else:
            print('You have been spotted by a hostile slime. You initiate a fight!')
            time.sleep(1.5)
            slimefight()
    else:
        print(f'"{playeroptions}" is not an option. Please choose one of the listed options.')
        time.sleep(2.0)
        griffonroad()


def treasure1():
    pass

def fork1():
    pass

def daltonroad():
    pass

def exitgame():
    print('Thanks for playing.')
    sys.exit()

def slimefight():
    os.system('cls')
    print(f'{player1.name}                             {testslime.name}')
    print(f'HP: {player1.hp}/{player1.maxhp}                      HP:{testslime.hp}/{testslime.maxhp}')

    def fightoptionsslime():
        print('[1] Attack')
        print('[2] Items')
        print('[3] Run')
        playeroptions = input('> ')
        if playeroptions == '1':
            print(f'You attack {testslime.name}')
            testslime.hp -= player1.baseattack
            if testslime.hp <= 0:
                print(f'You defeated {testslime.name}')
                player1.gold += testslime.golddrop
                print(f'You receive {testslime.golddrop} gold!')
                time.sleep(2.0)
                griffonroad()
            print(f'{testslime.name} attacks you!')
            dice = random.randrange(1, 6)
            if dice >= 3:
                player1.hp -= testslime.attackdmg
                print(f'{testslime.name} does {testslime.attackdmg} damage to you!')
                time.sleep(2.0)
                slimefight()
            else:
                print(f'{testslime.name} missed his attack!')
                time.sleep(2.0)
                slimefight()
        elif playeroptions == '2':
            print(f'These are your available items: {player1.items}')
            print('What item do you want to use?')
            playeroptions2 = input('> ')
            if playeroptions2.lower() == 'potion' and playeroptions2 in player1.items:
                print('You healed yourself by 10 HP')
                player1.hp += 10
                if player1.hp > player1.maxhp:
                    player1.hp = 100
                time.sleep(2.0)
                fightoptionsslime()

    fightoptionsslime()



titlescreen()

