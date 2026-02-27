direction=input("Do you go left or right? (Type 'left' or 'right'): ").lower()

if direction == "left":
    second_question=input("Will you swim or wait? (Type 'swim' or 'wait'): ").lower()
    if second_question.lower() == "swim":
        print("Congratulations! You'll find the treasure!")
    else:
        print("You're waiting too long! You won't find the treasure.")
elif direction == "right":
    print("Oh no! Your direction isn't a luckier one. The adventure ends here!")

else:
    print("Invalid input. Please type 'left' or 'right'.")