password = input("Password: ")
while len(password) < 2 or len(password) > 5:
    print("Invalid length.")
    password = input("Password: ")
if len(password) > 2 or len(password) < 5:
    for i in range(0, len(password)):
        print("*", end='')