def start():
    print("You wake up in a dark forest.")
    choice = input("Do you go north or south? ")
    if choice == "north":
        cave()
    else:
        river()

def cave():
    print("You enter a dark cave.")
    choice = input("Do you light a torch or continue in darkness? ")
    if choice == "light":
        print("You find treasure! You win!")
    else:
        print("You fall into a pit. Game over.")

def river():
    print("You reach a river.")
    choice = input("Do you swim or build a raft? ")
    if choice == "swim":
        print("You swim across and escape the forest. You win!")
    else:
        print("Your raft breaks. Game over.")

start()