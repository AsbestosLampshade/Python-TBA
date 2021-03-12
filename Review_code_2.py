import random

""" 8X7 Map (8 rows and7 columns)
    Total=56
    Floor=23
    Room=3
    Enemy=3
    Start=1
    Wall=26"""
"""Start=(4,3)
    (x,y)
    (row,column)"""

map = [["Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall"],
       ["Wall", "Floor", "Floor", "Floor", "Room", "Floor", "Wall"],
       ["Wall", "Floor", "Room", "Floor", "Floor", "Floor", "Wall"],
       ["Wall", "Floor", "Floor", "Floor", "Enemy", "Floor", "Wall"],
       ["Wall", "Enemy", "Floor", "Start", "Floor", "Floor", "Wall"],
       ["Wall", "Floor", "Floor", "Floor", "Room", "Floor", "Wall"],
       ["Wall", "Floor", "Floor", "Enemy", "Floor", "Floor", "Wall"],
       ["Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall"]]
map_row = 4
map_column = 3
gold_coins = 0
health = 100
player_score = 0
map_walls = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 0), (2, 0),
             (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (1, 6), (2, 6), (3, 6), (4, 6),
             (5, 6), (6, 6), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6)]


def boss_fight():
    global player_score
    health = 100
    n = random.randint(1, 10)
    if n % 2 == 0:
        boss = "Minotaur"
    else:
        boss = "Goblin King"
    if boss == "Minotaur":
        boss_health = 200
        boss_damage = 40
        boss_loss = 40
    else:
        boss_health = 125
        boss_damage = 35
        boss_loss = 35
    counts = 0
    countdef = 0
    i = True
    boss_turn = ["Get out of the way.", "Block", "Counter-Attack."]
    player_turn = ["Attack", "Special Attack"]
    print("Something lurks in the shadows. You see a huge figure move around. You draw your weapon, steeling yourself.")
    print(f"The Huge Figure comes closer and closer. It appears before you. It is the {boss}")
    print("It is time...")
    print("F I G H T")
    print(f"The {boss} attacks first. You need to move quick")
    while health > 0 and boss_health > 0:
        print(f"Alright. You know what to do.")
        if i:
            defend = accept_choice(boss_turn)
            if defend == "Get out of the way.":
                print("You get out of the way yet the attack does some minor damage!!")
                health -= boss_damage / 4
                print(f"Your health is {health}")
            elif defend == "Block":
                if countdef == 0:
                    print("You stand your ground. The attack has no effect "
                          "on you this time. However you grow tired.")
                    print("You cannot defend for 3 turns now")
                    countdef = 3
                else:
                    print(f"You  cannot defend for {countdef} more turns!")
                    print("You try to get out out of the way.")
                    health -= boss_damage / 4
                    print(f"Your health is now{health}")
            elif defend == "Counter-Attack.":
                print("You show nerves of steel. You decide to parry the"
                      " attack. You also stun the boss with your courage.")
                boss_health -= (boss_loss / 2)
                print(f"Its health is {boss_health}")
            countdef -= 1
            i = False
        elif not i:
            print("It's your turn to attack now. No time to rest.")
            attack = accept_choice(player_turn)
            if attack == "Attack":
                print("You attack the enemy, and it sustains some damage.")
                boss_health -= boss_loss
            else:
                if counts == 2:
                    print("You take a deep breath. It's time. You summon energy from the four corners of the Earth...")
                    print("...and  release it all in a single shout!!")
                    boss_health -= boss_loss * 2
                    print(f"Its health is now {boss_health}")
                    counts = 0
                else:
                    print(
                        f"You don't have enough energy to use this attack yet! You need to wait for {2 - counts} turns.")
                    print("You decide to use a regular attack.")
                    boss_health -= boss_loss
                    print(f"It's health is now {boss_health}")
                i = True
            counts += 1
    if health <= 0:
        status = "Dead"
        print("       Y O U  D I E D       ")
        exit()
    elif boss_health <= 0:
        status = "Alive"
        print("      D E M O N  V A N Q U I S H E D       ")
        player_score += 200
        return status, player_score


print("\nThe Year is 1774. ")
print("Primitivity has settled over Humanity again. The practise of Human Sacrifices has resumed.")
print("You have been selected as one of the 12 tributes, being sacrificed to the Labyrinth.")
print("Your end goal? To Survive. Bloodthirsty and feral monsters roam this maze, and so much more....")
print("\nRules : ")
print("- Enter the text up,down,left,right to move your character across the map.\n"
      "- You may encounter dangerous enemies,mysterious rooms and walls.\n"
      "- If you chose to flee the enemy your health decreases by 20.\n"
      "- Your health is reset to 100 after every fight.\n"
      "- You get 100 points for every enemy defeated.\n"
      "- Gold coins can be found in the mysterious rooms.\n")


class Playerchoice:
    def __init__(self):
        self.archer = {'Name': "Archer", 'Weapon': 'Bow & Arrow', 'Damage': 10, 'Health Loss': 4}
        self.magician = {'Name': "Magician", 'Weapon': 'Magic Staff', 'Damage': 30, 'Health loss': 14}
        self.knight = {'Name': "Knight", 'Weapon': 'Sword and Shield', 'Damage': 16, 'Health Loss': 6}
        self.choice = ""

    def select_choice(self):
        print("There are three characters. Archer, Magician, Knight ")
        print("These are the attributes for the different characters : ")
        for key, value in self.archer.items():
            print(' ', key, ':', value, end="")
        print('')
        for key, value in self.magician.items():
            print(' ', key, ':', value, end="")
        print('')
        for key, value in self.knight.items():
            print(' ', key, ':', value, end="")
        print('')
        self.choice = accept_choice([self.archer['Name'], self.magician['Name'], self.knight['Name']])


def accept_choice(lst_of_choices):
    choice = ""
    while choice not in lst_of_choices:
        print("Select one of the following:")
        for count, option in enumerate(lst_of_choices):
            print(f"{count + 1}:{option}")
        count = len(lst_of_choices)
        while True:
            try:
                choice = int(input(f"Enter your choice (1-{count}):"))
            except:
                print("Please enter an acceptable number")
            else:
                if not choice in range(1, count + 1):
                    print("Invalid choice")
                    choice = ""
                    continue
                else:
                    lst = list(lst_of_choices)
                    choice = lst[choice - 1]
                    break
            finally:
                print(choice)
    return choice


def player_movement(player_input):
    global map_row
    global map_column
    global coordinates
    coordinates = map_row, map_column
    if player_input == "Up":
        if coordinates not in [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (5, 2)]:
            map_row = map_row - 1
        elif coordinates in [(2, 5), (5, 2)]:
            boss_fight()
        else:
            print("There is a wall in front of you and cannot proceed in that direction!")
            player_input = ["Up", "Down", "Left", "Right", "Health", "Gold Coins", "Quit"]
            move = accept_choice(player_input)
            player_movement(move)
            print(coordinates)
    elif player_input == "Down":
        if coordinates not in [(6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (2, 5), (5, 2)]:
            map_row = map_row + 1
        elif coordinates in [(2, 5), (5, 2)]:
            boss_fight()
        else:
            print("There is a wall in front of you and cannot proceed in that direction!")
            player_input = ["Up", "Down", "Left", "Right", "Health", "Gold Coins", "Quit"]
            move = accept_choice(player_input)
            player_movement(move)
            print(coordinates)
    elif player_input == "Right":
        if coordinates not in [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (2, 5), (5, 2)]:
            map_column = map_column + 1
        elif coordinates in [(2, 5), (5, 2)]:
            boss_fight()
        else:
            player_input = ["Up", "Down", "Left", "Right", "Health", "Gold Coins", "Quit"]
            move = accept_choice(player_input)
            player_movement(move)
            print(coordinates)
    elif player_input == "Left":
        if coordinates not in [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (2, 5), (5, 2)]:
            map_column = map_column - 1
        elif coordinates in [(2, 5), (5, 2)]:
            boss_fight()
        else:
            player_input = ["Down", "Left", "Right", "Health", "Gold Coins", "Quit"]
            move = accept_choice(player_input)
            player_movement(move)
            print(coordinates)
    elif player_input == "Health":
        print("Health : ", health)
    elif player_input == "Gold Coins":
        print("Gold Coins : ", gold_coins)
    elif player_input == "Quit":
        print("Thank You for playing the game!")
        exit()
    else:
        player_input = ["Down", "Left", "Right", "Health", "Gold Coins", "Quit"]
        move = accept_choice(player_input)
        player_movement(move)
        print(coordinates)
    return coordinates


# Character defined and chosen here
p = Playerchoice()
p.select_choice()


def player_interaction():
    global gold_coins
    global health

    def room():
        import random
        global gold_coins
        player_input2 = ["Yes", "No"]
        input2 = accept_choice(player_input2)
        if input2 == "Yes":
            t = random.randrange(0, 201)
            print(f"You have found a sack containing {t} gold coins!")
            gold_coins = gold_coins + t
            print("Your Gold Coins : ", gold_coins)
        elif input2 == "No":
            print("You chose not to explore the room ")
            player_input = ["Down", "Left", "Right", "Health", "Gold Coins", "Quit"]
            move = accept_choice(player_input)
            player_movement(move)
        else:
            print("Please a valid input!")
            room()

    def enemy():
        global health
        global player_score

        def fight():
            health = 100
            enemy_health = 100
            status = "Alive"
            l2 = ["Dodge", "Block"]
            l = ["Attack", "Dodge"]
            player_chance = True
            if p.choice == "ARCHER":
                damage = p.archer['Damage']
                loss = p.archer['Health Loss']
            elif p.choice == "MAGICIAN":
                damage = p.magician['Damage']
                loss = p.magician['Health Loss']
            else:
                damage = p.knight['Damage']
                loss = p.knight['Health Loss']
                while health > 0 and enemy_health > 0:
                    if player_chance:
                        print(f"\nYour turn to attack.")
                        action = accept_choice(l)
                        if action == "Attack":
                            enemy_health -= damage
                            if enemy_health > 0:
                                print(f"Enemy's health is {enemy_health}")
                            else:
                                print(f"Enemy's health is 0")
                        elif action == "Dodge":
                            health -= loss / 2
                            print(f"Your health is {health}")
                            if enemy_health > 0:
                                print(f"Enemy's health is {enemy_health}")
                            else:
                                print(f"Enemy's health is 0")
                            # print(f"The enemy's health is {enemy_health}")
                        else:
                            status = "Dead"
                            print("      Y O U  D I E D      ")
                            break
                        player_chance = False
                    else:
                        print(
                            f"\nIt is  the enemy's turn to attack. He viciously "
                            f"attacks you!! ")
                        print("Enter your choice quickly, lest the enemy attack you!! ")
                        action = accept_choice(l2)
                        if action.upper() == "DODGE":
                            print("You dodge the attack, yet the enemy manages to land a heavy blow!!")
                            health -= (2 * loss)
                        elif action.upper() == "BLOCK":
                            print("You block the attack, yet, the enemy manages to land a blow on your body. You take light damage!!")
                            health -= (loss / 2)
                        print(f"Your health is {health}")
                        player_chance = True
            if health > 0 >= enemy_health:
                status = "Alive"
                print("You win!! You may proceed!")
                return status
            elif enemy_health > 0 >= health:
                status = "Dead"
                print("      Y O U   D I E D      ")
                exit()

        player_input = input("You have encountered an enemy! Would you like to fight (Yes/No) : ").upper().strip()
        if player_input == "YES":
            fight()
            print("You fought with the enemy and won!")
            player_score = player_score + 100
            print("Your score : ", player_score)
        elif player_input == "NO":
            print("You chose to flee!")
            health = health - 20
            print("Your health : ", health)
        else:
            print("Please enter the correct option!")
            enemy()

    if map[map_row][map_column] == "Room":
        room()
    elif map[map_row][map_column] == "Enemy":
        enemy()

while True:
    if health > 0:
        player_input = ["Up", "Down", "Left", "Right", "Health", "Gold Coins", "Quit"]
        move = accept_choice(player_input)
        player_movement(move)
        player_interaction()
        print(coordinates)
    else:
        print("Your health has become 0! \nY O U    D I E D")
        exit()
