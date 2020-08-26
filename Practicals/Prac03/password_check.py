def main():
    password = get_password()
    while len(password) < 2 or len(password) > 5:
        print("Invalid length.")
        password = get_password()
    print_asterisk(password)


def print_asterisk(password):
    if len(password) > 2 or len(password) < 5:
        for i in range(0, len(password)):
            print("*", end='')


def get_password():
    password = input("Password: ")
    return password


main()
