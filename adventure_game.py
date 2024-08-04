import random
import time

enemies = ["trolls", "dragons", "wicked fairie", "zombies"]
enemy = random.choice(enemies)
weapons = ["sword", "knife"] 
weapon = random.choice(weapons)
cave_visited = False 

def print_sleep(message, wait_time):
    print(message)
    time.sleep(wait_time)

def intro():
    print_sleep("You find yourself standing in an open field", 2)
    print_sleep("it is filled with grass and yellow wildflowers.", 2)
    print_sleep("Rumor has it that is a magic land", 2)

def play_again():
    choice = ''
    while choice not in ['y' , 'n']:
        choice = input("would you like to play again? (y,n)\n")
    if choice == 'n':
        print_sleep("thanks for playing, see you soon!", 2)
        return game_over
    elif choice == 'y':
        print_sleep("excellent, restarting the game ...", 3)
        return 'running'

def game_over():
    print_sleep("game over my friend,")

def combat(weapon):
    print_sleep(f"you are now at combat against your {enemy}", 3)
    print_sleep(f"use your {weapon}", 2)
    while "sword" in weapon:
        print_sleep(f"you might be feeling a bit unprepared for this fighting against {enemy}", 2)
        fight = input ("Do you want to fight, y or n\n")
        while "y" in fight:
            print_sleep(f"you are doing your best.", 2)
            print_sleep("you just saved 10 workers from town! congratulations! you are victorius", 3)
            where_to()
        if "n" in fight:
            print_sleep("run to the field and pay attention if someone is following..", 2)
            where_to()
    if "knife" in weapon:
        print_sleep(f"you are doing your best", 2) 
        print_sleep(f"the knife is very sharp, but the enemy is very strong!", 3) 
        print_sleep("Im sorry, you have been defeated", 2)
        play_again()
        where_to()

def where_to():
    print_sleep("in front of you, there is a house and your left a cave.", 2)
    print_sleep("Enter 1 to knock on the door of the house.\n", 2)  
    print_sleep("Enter 2 to peer into the cave.\n", 2)
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")
    if "1" in choice:
        print_sleep("you chose to knock on the door!\n", 2)
        door()
    elif "2" in choice:
        print_sleep("you chose to peer on the cave!", 2)
        cave()
    
def door():
    print_sleep("you are entering the house", 2)
    print_sleep(f"a rare and valuable item from {enemy} is on display.", 2)
    print_sleep("if you chose to collect it be careful..",  2)
    print_sleep("the owner might be around", 2)
    player_input = input("Are you collecting it (1) or no(2)\n")
    while '1' in player_input:
        print_sleep(f"hurry up,watch out! look at {enemy}.", 2)
        print_sleep(f"oh feck!this is {enemy}'s house", 2)
        combat(weapon)
    if '2' in player_input:
        print_sleep("wise choice. You are walking out of here.", 2)
        where_to()
        
def cave():
    global cave_visited
    global weapon 
    print_sleep(f"you come inside the cave and put your {weapon} in front of you", 2)
    if cave_visited:
        print_sleep("you ve been before and got all you can.", 2)
    elif cave_visited is False:
        print_sleep("you are facing the fire of life,\n", 2)
        print_sleep("a rare and valuable item from a fairy.", 2)
        print_sleep("if you chose to collect it be careful", 2)
        print_sleep("the fairy might be close by", 2)
        player_input = ''
        player_input = input("are you collecting it? y or n\n")
        if "y" in player_input:
            print_sleep("hurry up, go back to field!", 2)
            where_to()
        elif "n" in player_input:
            print_sleep("wise choice. lets get you back.", 2)
            where_to()
    elif cave_visited is True:
        print_sleep("you walk back to the field", 2)
        where_to()

game_state = 'runing'
while game_state == 'running':
    enemies = ["trolls", "dragons", "wicked fairie", "zombies"]
    enemy = random.choice (enemies)
    weapon = "sword", "knife", "flame"  
    cave_visited = False 
    
intro()
where_to()

game_state = play_again()
