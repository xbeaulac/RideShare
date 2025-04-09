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
            headers = ("Rider", "Pick Up", "Drop Off", "Rating")
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
        print("(a) Take a ride")
        print("(b) Rate my driver")
        print("(c) View rides")
        print("(exit) Exit")
        user_input = input("Enter your choice: ")
        if user_input == "a":
            driver_username, driver_first_name, driver_last_name = db.getActiveDriver()
            print(f"Located driver: {driver_first_name} {driver_last_name}")
            pick_up_location = input("Pick up location: ")
            drop_off_location = input("Drop off location: ")
            db.takeRide(username, driver_username, pick_up_location, drop_off_location)
            print(f"{driver_first_name} drove you from {pick_up_location} to {drop_off_location}.")
        elif user_input == "b":
            ride_id, rider, pick_up_location, drop_off_location, rating = db.getMostRecentRide(username)
            headers = ("Rider", "From", "Drop Off", "Rating")
            print(tabulate([[rider, pick_up_location, drop_off_location, rating]], headers=headers, tablefmt="grid"))
            is_correct_ride = input("Is this the ride you would like to rate? (y/n): ")
            if is_correct_ride == "y":
                rating = input("Rating (1 to 5): ")
                db.setRating(ride_id, rating)
                print(f"Set rating to {rating}.")
            elif is_correct_ride == "n":
                rides = db.viewRidesRidden(username)
                headers = ("Id", "Rider", "Pick Up", "Drop Off", "Rating")
                print(tabulate(rides, headers=headers, tablefmt="grid"))
                ride_id = input("Enter ride ID of ride to rate: ")
                rating = input("Rating (1 to 5): ")
                db.setRating(ride_id, rating)
                print(f"Set rating to {rating}.")
        elif user_input == "c":
            rides = db.viewRidesRidden(username)
            headers = ("Id", "Rider", "Pick Up", "Drop Off", "Rating")
            print(tabulate(rides, headers=headers, tablefmt="grid"))
        elif user_input == "exit":
            print("Thank you for using RideShare!")
            break
        else:
            print("Invalid input.")
            continue
# Close connection
db.close()
