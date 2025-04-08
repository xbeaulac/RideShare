from database import Database
from tabulate import tabulate

db = Database()

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

    if role == 'driver':
        isActive = db.getIsActive(username)
        print(f"{username} ({role}) is {'active' if isActive == 1 else 'inactive'}")
        print("Which would you like to do?")
        print("(a) View rating")
        print(f"(b) Set status to {'inactive' if isActive == 1 else 'active'}")
        print("(c) View rides")
        print("(exit) Exit")
        user_input = input("Enter your choice: ")
        print()
        if user_input == "a":
            print("Your rating:", db.viewRating(username))
        elif user_input == "b":
            print(db.toggleDrivingMode(username))
        elif user_input == "c":
            rides = db.viewRidesDriven(username)
            headers = ("Rider", "From", "To", "Rating")
            print(tabulate(rides, headers=headers, tablefmt="grid"))
        elif user_input == "exit":
            print("Thank you for using RideShare!")
            break
        else:
            print("Invalid input.")
            continue
    elif role == 'rider':
        print(f"{username} ({role})")
        print("Which would you like to do?")
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
