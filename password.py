flag = 0
while flag != 1:
    password = input("Enter a password:")
    if len(password) < 8:
        print("Error!!! Less than 8 characters")
    elif not password[0].isupper():
        print("Error!!! First character is not uppercase")
    elif password.isalpha():
        print("Error!!! Password doesn't have any numeric character")
    elif not password[-1].islower():
        print("Error!!! Last character is not lowercase")
    else:
        print("Password is correct\nThanks")
        flag = 1