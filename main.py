# Zandaloria
# Made by Pedro A.

import time
import cmd
import textwrap
import sys
import os
import random


#locations
zanda = False
griffonrd = False
fork1standing = False

#treasures
treasuregriffonrd = True

# #weapons
# woodsw = True
# ironsw = False


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

    def weaponsts(self):
        if self.currentWeap == 'iron sword':
            self.baseattack = 20



#Enemies

class Slime:
    def __init__(self, name):
        self.name = name
        self.maxhp = 40
        self.hp = self.maxhp
        self.golddrop = 20
        self.attackdmg = 5

slime1 = Slime('slimer')



class troll:
    def __init__(self):
        pass



class skeleton:
    def __init__(self):
        pass

def titlescreen():
    os.system('cls')
    print('##############################')
    print('#                            #')
    print('#                            #')
    print('#          [1]Start          #')
    print('#          [2]Leave          #')
    print('#                            #')
    print('# (Type one of the numbers.) #')
    print('##############################')
    playeroptions = input('> ')
    if playeroptions.lower() == '1':
        startgame()
    elif playeroptions.lower() == '2':
        exitgame()
    else:
        print('\n')
        print(f'"{playeroptions}" is not a valid command. Try using "1" or "2')
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
    global zanda
    zanda = True
    print('You are in Zandaloria')
    print('You can either go to the left or to the right.')
    print('Where do you want to go? (Type the option number)')
    print('[1] Left Path (Griffon Road)')
    print('[2] Right Path (Dalton Road)')
    print('[3] View Character')
    playeroptions = input('> ')
    if playeroptions == '1':
        zanda = False
        griffonroad()
    elif playeroptions == '2':
        zanda = False
        daltonroad()
    elif playeroptions == '3':
        character()
    else:
        print(f'"{playeroptions}" is not an option. Choose one of the options listed.')
        time.sleep(2.0)
        zandaloria()

def griffonroad():
    os.system('cls')
    global griffonrd
    griffonrd = True
    print('You are now on Griffon Road')
    print('What do you want to do? Type one of the options')
    print('[1] Go back to Zandaloria')
    print('[2] Continue on the path.')
    print('[3] View Character')
    playeroptions = input('> ')
    if playeroptions == '1':
        griffonrd = False
        zandaloria()
    elif playeroptions == '2':
        dice = random.randrange(1, 10)
        if dice <= 5:
            treasure()
            fork1()
        else:
            print('You have been spotted by a hostile slime. You initiate a fight!')
            time.sleep(1.5)
            fight()
    elif playeroptions == '3':
        character()
    else:
        print(f'"{playeroptions}" is not an option. Please choose one of the listed options.')
        time.sleep(2.0)
        griffonroad()

def fork1():
    os.system('cls')
    global fork1standing
    fork1standing = True
    print('You have arrived at a fork')
    print('The left path leads tow the volcanoes.')
    print('The right path leads to the coast.')
    print('What do you want to do? Type one of the options')
    print('[1] Go back to Griffon Road')
    print('[2] Go to the volcanoes.')
    print('[3] Go to the Coast')
    print('[4] View Character')
    playeroptions = input('> ')
    if playeroptions == '1':
        fork1standing = False
        griffonroad()
    elif playeroptions == '2':
        volcanoes()
    elif playeroptions == '3':
        coast()
    elif playeroptions == '4':
        character()
    else:
        print(f'"{playeroptions}" is not an option. Please choose one of the listed options.')
        time.sleep(2.0)
        fork1()

def volcanoes():
    pass

def coast():
    pass



def items():
    pass

def character():
    os.system('cls')
    print(f'Name: {player1.name}')
    print(f'HP {player1.hp}/{player1.maxhp}')
    print(f'Equiped Weapon: {player1.currentWeap}')
    print(f'ATK: {player1.baseattack}')
    print(f'Gold {player1.gold}')
    print(f'Items: {player1.items}')
    print(f'Weapons: {player1.weapons}')
    print('\n')
    print('[1] Go Back')
    print('[2] Change Weapon')
    print('[3] Use Item')
    playeroptions = input('> ')
    if playeroptions == '1':
        if zanda == True:
            zandaloria()
        elif griffonrd == True:
            griffonroad()
        elif fork1standing == True:
            fork1()
    elif playeroptions == '2':
        if len(player1.weapons) < 1:
            print("You don't have any other Weapons to equip.")
            time.sleep(1.5)
            character()
        else:
            print('Type the name of the weapon you want to equip.')
            playeroptions2 = input('> ')
            if playeroptions2.lower() in player1.weapons:
                player1.weapons.append(player1.currentWeap)
                player1.currentWeap = playeroptions2.lower()
                player1.weapons.remove(playeroptions2)
                print(f'You have equipped the {playeroptions2}')
                if player1.currentWeap == 'iron sword':
                    print('Your attack increased by 10')
                player1.weaponsts()
                time.sleep(1.5)
            character()
    elif playeroptions == '3':
        pass

def treasure():
    global treasuregriffonrd
    if treasuregriffonrd and griffonrd == True:
        treasuregriffonrd = False
        print('You have found a Treasure Chest!')
        time.sleep(1.5)
        print('You open the Chest and receive an Iron Sword!')
        player1.weapons.append('iron sword')
        time.sleep(1.5)
        fork1()


def daltonroad():
    pass

def exitgame():
    print('Thanks for playing.')
    sys.exit()



def fight():
    os.system('cls')
    print(f'{player1.name}                             {slime1.name}')
    print(f'HP: {player1.hp}/{player1.maxhp}                      HP:{slime1.hp}/{slime1.maxhp}')

    def fightoptions():
        print('[1] Attack')
        print('[2] Items')
        print('[3] Run')
        playeroptions = input('> ')
        if playeroptions == '1':
            print(f'You attack {slime1.name}')
            slime1.hp -= player1.baseattack
            if slime1.hp <= 0:
                print(f'You defeated {slime1.name}')
                slime1.hp = slime1.maxhp
                player1.gold += slime1.golddrop
                print(f'You receive {slime1.golddrop} gold!')
                time.sleep(2.0)
                if zanda == True:
                    zandaloria()
                elif griffonrd == True:
                    griffonroad()
            print(f'{slime1.name} attacks you!')
            dice = random.randrange(1, 6)
            if dice >= 3:
                player1.hp -= slime1.attackdmg
                print(f'{slime1.name} does {slime1.attackdmg} damage to you!')
                time.sleep(2.0)
                fight()
            else:
                print(f'{slime1.name} missed his attack!')
                time.sleep(2.0)
                fight()
        elif playeroptions == '2':
            print(f'These are your available items: {player1.items}')
            print('What item do you want to use?')
            playeroptions2 = input('> ')
            if playeroptions2.lower() == 'potion' and playeroptions2 in player1.items:
                print('You healed yourself by 10 HP')
                player1.hp += 10
                player1.items.remove('potion')
                if player1.hp > player1.maxhp:
                    player1.hp = 100
                time.sleep(2.0)
                fight()
        elif playeroptions == '3':
            print('You have escaped successfully!')
            time.sleep(1.5)
            if zanda == True:
                zandaloria()
            elif griffonrd == True:
                griffonroad()


    fightoptions()



titlescreen()

