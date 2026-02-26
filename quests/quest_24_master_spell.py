def ask_for_age():
    return int(input("Enter your age: "))

def can_they_vote(age):
    if age >= 18:
        print("You can vote!")
    else:
        print("You cannot vote yet.")

user_age = ask_for_age()
can_they_vote(user_age)