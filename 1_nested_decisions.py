# task 1 correct code errors
# task 2 set the scene
# task 3 add pass statements for invalid entries

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = (input("Would you like to light a torch? or continue in the dark?"))
    if action == "light a torch":
        print("You find a hidden treasure!")
    elif action == "continue in the dark":
        print("Oh no! a bear!")
    else:
        pass
else:
    pass 
