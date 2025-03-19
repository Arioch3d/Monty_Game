# Monty_Game

This is for Week 2 "Let's Make a Game!" Assignment.

1. Set Up the Scene
   Print "Welcome to the Monty Python Adventure!"
   Print "You are about to embark on a quest for the Holy Grail. Beware of dangerous encounters!"

2. Character Setup

Define variables to store basic player information:

Define the variable player_name
Take an input to get player_name.
"What is your name, brave adventurer? "
As a reminder we can do custom inputs so we will test it in the background for you.
Welcome the player to the game
use a f string for this
"Welcome, Sir player_name of Pythonia!"

3. Set the Scene Add the following lines to introduce the knight’s challenge:

Display: A knight steps in front of you and says, 'None shall pass!'
Take in a players choice
1 fight the knight
2 try to reason with him?
If the user enters 1 to fight the knight, "The knight draws his sword. It's time for battle!"
If the user enters 2 to try to reason with him, "The knight scoffs at your attempt to reason and attacks anyway."
If there is any other input, "You hesitate... and the knight charges!"

4. Loops for Repeated Choices

In this step, you’ll add a while loop that will keep asking the player if they want to cross the Bridge of Death until they enter a valid response. This will ensure that the player only proceeds if they choose "yes" or "no."

Write the Loop Add the following lines to create the bridge-crossing scene:

Display: "Do you want to cross the Bridge of Death? (yes/no)"
Take in a player’s response
Convert the player’s input to lowercase using .lower()
Add Conditional Responses

Use an if statement inside the while loop to check the player’s response:

if response is "yes"
Display: "A troll appears and asks you three questions!"
End the loop with break
elif response is "no"
Display: "You wisely turn back."
End the loop with break
else
Display: "Please answer 'yes' or 'no'."
The loop will continue, asking again

5. Ending the Game

In this final step, you’ll display a message congratulating the player for completing their quest and saying farewell. This will conclude your Monty Python-themed adventure game.

Display the Ending Messages Add the following lines to announce the player’s success and say goodbye:

Display: "Congratulations, you have completed your quest!"
Display: A farewell message that includes the player’s name:
Use an f-string to personalize the message by inserting player_name`
