def get_answer(question, answers):
    # waiting for answer which is in answers
    answer = str()
    while answer not in answers:
        answer = str(input(question)).lower()
    return answer


answer1 = get_answer('Choice 1: Do you want to go left or right?\n', ["left", "right"])
if answer1 == "left":
    print("\nYou came to the lake.")
    answer2 = get_answer('Choice 2: Do you want to swim or wait?\n', ["swim", "wait"])
    if answer2 == "wait":
        print("\nThere is a door from nowhere.")
        answer3 = get_answer('Choice 3: Which door? (red/blue/yellow)\n', ["red", "blue", "yellow"])
        if answer3 == "blue":
            print("Eaten by beasts. Game Over.")
        elif answer3 == "red":
            print("Burned by fire. Game Over.")
        elif answer3 == "yellow":
            print("YOU WIN!")
    else:
        print("Attacked by trout. Game Over.")
else:
    "Fall into a hole. Game Over."


