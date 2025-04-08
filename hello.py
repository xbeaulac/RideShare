from actions import *

db = Database()

# print("Welcome to RideShare! ")
# user_input = input("Are you a new user (0) or returning user (1): ")
# if user_input == "0":
#     print("You selected: new user.")
#     user_input = input("Create a rider (0) or driver (1) account: ")
#     if user_input == "0":
#         print("You selected: rider.")
#         username = input("Enter username: ")
#         first_name = input("Enter first name: ")
#         last_name = input("Enter last name: ")
#         db.createRider(username, first_name, last_name)
#     if user_input == "1":
#         print("You selected: driver.")
#         username = input("Enter username: ")
#         first_name = input("Enter first name: ")
#         last_name = input("Enter last name: ")
# if user_input == "1":
#     print("You selected: returning user.")
#     user_input = input("Log in to a rider (0) or driver (1) account: ")
#     if user_input == "0":
#         print("You selected: rider.")
#         user_input = input("Enter rider username: ")
#     if user_input == "1":
#         print("You selected: driver.")
#         user_input = input("Enter driver username: ")

db.cursor.execute("SELECT * FROM Rider")
for (username, firstName, lastName) in db.cursor:
    print(username, firstName, lastName)

# Close connection
db.close()
