# Task 1 -  Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

user_input_fn = input("What is your first name?")
user_input_ln = input("What is your last name?")

def validation(user_input_fn, user_input_ln):
    if len(user_input_fn) < 2:
        print("First name must be more than 2 characters long")
    elif len(user_input_ln) < 2:
        print("Last name must be more than 2 characters long")
    else:
        print("First name and Last name validated")

validation(user_input_fn, user_input_ln)