from actions import *

db = Database()

print("Welcome to RideShare! ")
username = None
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
    elif user_input == "1":
        print("You selected: driver.")
        username = input("Enter username: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        db.createDriver(username, first_name, last_name)
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
                print(f"Welcome, {res[1]}!")
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
                print(f"Welcome, {res[1]}!")
                break

print("username:", username)

# Close connection
db.close()
