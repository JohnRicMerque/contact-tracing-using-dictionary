# John Ric Merque | BSCOE 2-6 | DSA

# Write a python program for contact tracing:

# - Display a menu of options
# 	Menu:
# 		 1 -> Add an item
# 		 2 -> Search
# 		 3 -> Exit (y/n)
# - Allow user to select item in the menu (check if valid)
# - Perform the selected option
# 		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# 				   Use dictionary to store the info
# 				   Use the full name as key
# 				   The value is another dictionary of personal information
# 		- Option 2: Search, ask full name then display the record
# 		- Option 3: Ask the user if want to exit or retry.

# PseudoCode
 
# 1. display menu
print("\n~~~~~~Menu:~~~~~~")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit (y/n)")
print("~~~~~~~~~~~~~~~~~\n")

# 2. ask user input for option selected
try:
    userCommandChoice = int(input("Please select a command option (1-3): "))
except:
    print("Invalid input. Make sure to enter a number from (1-3)")
# 2. create navigation to commands based on the input
# 3. for command 1, create a series of user input and store details in a dictionary
# 4. for command 2, access the dictionary and display dictionary values
# 5. for command 3, enclose everything in a loop and add break statement to terminate




