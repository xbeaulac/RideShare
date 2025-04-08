import database

db = database.Database()

print("Welcome to RideShare! ")
username = None
role = None
user_input = input("Are you a new user (0) or returning user (1): ")
if user_input == "0":
    print("You selected: new user.")
    user_input = input("Create a rider (0) or driver (1) account: ")
    if user_input == "0":
        print("You selected: rider.")
        username = input("Enter username: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        db.createRider(username, first_name, last_name)
        role = 'rider'
    elif user_input == "1":
        print("You selected: driver.")
        username = input("Enter username: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        db.createDriver(username, first_name, last_name)
        role = 'driver'
elif user_input == "1":
    print("You selected: returning user.")
    user_input = input("Log in to a rider (0) or driver (1) account: ")
    if user_input == "0":
        print("You selected: rider.")
        while True:
            username = input("Enter rider username: ")
            res = db.signInRider(username)
            if res is None:
                print("That username does not exist.")
                continue
            else:
                role = 'rider'
                break
    elif user_input == "1":
        print("You selected: driver.")
        while True:
            username = input("Enter rider username: ")
            res = db.signInDriver(username)
            if res is None:
                print("That username does not exist.")
                continue
            else:
                role = 'driver'
                break

while True:
    if username is None or (role != "rider" and role != "driver"):
        break
    print()
    print(f"{username} ({role})")
    print("Which would you like to do?")
    if role == 'driver':
        print("(a) View rating")
        print("(b) Switch driver mode")
        print("(c) View rides")
        print("(exit) Exit")
        user_input = input("Enter your choice: ")
        print()
        if user_input == "a":
            pass
        elif user_input == "b":
            pass
        elif user_input == "c":
            pass
        elif user_input == "exit":
            print("Thank you for using RideShare!")
            break
        else:
            print("Invalid input.")
            continue
    elif role == 'rider':
        print("(a) Find a driver")
        print("(b) Rate my driver")
        print("(c) View rides")
        print("(exit) Exit")
        user_input = input("Enter your choice: ")
        if user_input == "a":
            pass
        elif user_input == "b":
            pass
        elif user_input == "c":
            pass
        elif user_input == "exit":
            print("Thank you for using RideShare!")
            break
        else:
            print("Invalid input.")
            continue
# Close connection
db.close()
