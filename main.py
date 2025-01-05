print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Hawkins, Indiana.")
print("Your mission is to find the treasure.")
choice1 = input("You are on the biking from Hopper's police station. You are at a crossroads. "
                "Which way will you turn?\nType 'left or 'right'.\n").lower()
if choice1 == "left":
    choice2 = input("The sidewalk ends, and you are on a very busy road, next to the train station. "
                    "Would you like to wait for a train, or walk through the woods?\nType 'wait' or 'walk'.\n").lower()
    if choice2 == "wait":
        choice3 = input("The train drops you off at the Hawkins lab. You sneak in and see three doors."
                        " One of them is red, another is blue, and the last is green."
                        " Which would you like to go in?\nType 'blue', 'red', or 'green'.\n").lower()
        if choice3 == "red":
            print("You enter the gate into the upside down and are killed by the Mind Flayer and Vecna (at the same time). Game over.")
        elif choice3 == "blue":
            print("Dr. Brenner is in there. He locks you up for what you have seen. Game over.")
        elif choice3 == "green":
            print("As you enter, you see a treasure chest. You win!")
        else:
            print("A mysterious gun shoots you in the back of the head. Enter a valid response next time. Game over.")
    else:
        print("As you walk in the woods, a demogorgon comes up behind you and eats your head off. Game over.")
else:
    print("You ride your bike into a pack of demodogs, and they rip your head off. Game over.")
