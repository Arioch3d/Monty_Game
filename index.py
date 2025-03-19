#Monty Python Game
print("Welcome to the Monty Python Adventure!")
print("You are about to embark on a quest for the Holy Grail. Beware of dangerous encounters!")
player_name = input("What is your name, brave adventurer? ")
print(f"Welcome, Sir {player_name} of Pythonia!")
print("A knight steps in front of you and says, 'None shall pass!'")
player_choice = input("Do you (1) fight the knight, or (2) try to reason with him?")
if player_choice == "1":
    print("The knight draws his sword. It's time for battle!")
elif player_choice == "2":
    print("The knight scoffs at your attempt to reason and attacks anyway.")
else:
    print("You hesitate... and the knight charges!")

while True:
    bridge_choice = input("Do you want to cross the Bridge of Death? (yes/no)")
    lowercase_input = bridge_choice.lower()
    if lowercase_input == "yes":
        print("A troll appears and asks you three questions!")
        break
    elif lowercase_input == "no":
       print("You wisely turn back.")
       break
    else:
       print("Please answer 'yes' or 'no'.")

print("Congratulations, you have completed your quest!")
print(f"Farewell, Sir {player_name}!")