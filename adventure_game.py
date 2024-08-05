import random
import time

def set_enemy():
    return random.choice(["troll", "dragon", "wicked fairy", "zombie"])

def set_weapon():
    return random.choice(["sword", "knife"])

def print_sleep(message, wait_time=1):
    print(message)
    time.sleep(wait_time)

def intro():
    print_sleep("You find yourself standing in an open field")
    print_sleep("It is filled with grass and yellow wildflowers.")
    print_sleep("Rumor has it that this is a magic land")

def play_again():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)\n").lower()
        if choice not in ['y', 'n']:
            print("Please enter 'y' or 'n'.")
    return choice == 'y'

def game_over():
    print_sleep("Thanks for playing!")
    print_sleep("Game over, my friend")

def combat(weapon, enemy):
    print_sleep(f"You are now in combat against a {enemy}.")
    print_sleep(f"Use your {weapon}.")
    if weapon == "sword":
        print_sleep(f"You might be feeling a bit unprepared for this fight against the {enemy}.")
    else:
        print_sleep("The knife is very sharp, but the enemy is very strong!")
    fight = ''
    while fight not in ['y', 'n']:
        fight = input("Do you want to fight? (y/n)\n").lower()
        if fight not in ['y', 'n']:
            print("Please enter 'y' or 'n'.")
    if fight == "y":
        print_sleep("You are doing your best.")
        if weapon == "sword":
            print_sleep("You just saved 10 workers from town! Congratulations! You are victorious.")
            return True
        else:
            print_sleep("Despite your efforts, you were defeated.")
            return False
    else:
        print_sleep("You run back to the field and pay attention if someone is following...")
        return True

def where_to():
    print_sleep("In front of you, there is a house and to your left, a cave.")
    print_sleep("Enter 1 to knock on the door of the house.")
    print_sleep("Enter 2 to peer into the cave.")
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")
        if choice not in ['1', '2']:
            print("Please enter '1' or '2'.")
    return choice

def door(enemy):
    print_sleep("You are entering the house.")
    print_sleep(f"A rare and valuable item from the {enemy} is on display.")
    print_sleep(f"If you choose to collect it, be careful... The {enemy} might be close by.")
    player_input = ''
    while player_input not in ['1', '2']:
        player_input = input("Are you collecting it? (1 for yes, 2 for no)\n")
        if player_input not in ['1', '2']:
            print("Please enter '1' or '2'.")
    if player_input == "1":
        print_sleep(f"Watch out! The {enemy} is watching you.")
        print_sleep(f"Oh no! This is the {enemy}'s house.")
        return True
    else:
        print_sleep("Wise choice. You are walking out of here.")
        return False

def cave(cave_visited, weapon, enemy):
    print_sleep("You peer into the cave.")
    if cave_visited:
        print_sleep("You've been here before and got all you can.")
        print_sleep("You walk back to the field.")
        return True
    else:
        print_sleep("You are facing the fire of life,")
        print_sleep(f"a rare and valuable item from a {enemy}.")
        print_sleep("If you choose to collect it, be careful.")
        print_sleep(f"The {enemy} might be close by.")
        player_input = ''
        while player_input not in ['y', 'n']:
            player_input = input("Are you collecting it? (y/n)\n").lower()
            if player_input not in ['y', 'n']:
                print("Please enter 'y' or 'n'.")
        if player_input == "y":
            print_sleep("You carefully pick up the item.")
            print_sleep("Suddenly, the cave starts to shake and the entrance begins to close!")
            print_sleep("You run as fast as you can and barely make it out in time.")
            print_sleep("Congratulations! You have obtained a rare item.")
            fight = ''
            while fight not in ['y', 'n']:
                fight = input(f"Do you want to fight the {enemy} that appeared? (y/n)\n").lower()
                if fight not in ['y', 'n']:
                    print("Please enter 'y' or 'n'.")
            if fight == 'y':
                return combat(weapon, enemy)
            else:
                print_sleep("You chose to avoid the fight and safely return to the field.")
                return True
        else:
            print_sleep("Wise choice. Let's get you back to the field.")
            return True

def ask_continue():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Do you want to go home with the item you stole or continue to the other location? (y for go home, n for continue)\n").lower()
        if choice not in ['y', 'n']:
            print("Please enter 'y' or 'n'.")
    return choice

def main():
    while True:
        cave_visited = False
        house_visited = False
        intro()
        game_active = True
        while game_active:
            if cave_visited and house_visited:
                print_sleep("You've explored both the house and the cave. There's nothing left to explore.")
                game_active = False
                continue

            weapon = set_weapon()
            enemy = set_enemy()
            choice = where_to()
            if choice == "1" and not house_visited:
                if door(enemy):
                    game_active = combat(weapon, enemy)
                house_visited = True
            elif choice == "2" and not cave_visited:
                game_active = cave(cave_visited, weapon, enemy)
                cave_visited = True

            if game_active:
                continue_choice = ask_continue()
                if continue_choice == 'y':
                    print_sleep("You decide to go home with your item. Congratulations!")
                    game_active = False
                else:
                    print_sleep("You choose to continue your adventure.")
                    if cave_visited and house_visited:
                        print_sleep("You've explored both the house and the cave. There's nothing left to explore.")
                        game_active = False

        if not play_again():
            game_over()
            break

if __name__ == "__main__":
    main()

