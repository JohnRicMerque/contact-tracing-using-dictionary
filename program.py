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
# 2. ask user input for option selected
# 2. create navigation to commands based on the input
# 3. for command 1, create a series of user input and store details in a dictionary
# 4. for command 2, access the dictionary and display dictionary values
# 5. for command 3, enclose the everuthing in a loop and add break statement to terminate

# for command 1, create a series of user input and store details in a nested dictionary
def addItem(dictionary):
    data = {}

    print("Please fill this form to add a profile.\n")

    fullname = input("Fullname: ")
    age = input("Age: ")
    address = input("Address: ")
    gender = input("Gender: ")
    vaccinationStatus = input("Vaccination Status: ")
    email = input("Email: ")

    data["Fullname"] = fullname
    data["Age"] = age
    data["Address"] = address
    data["Gender"] = gender
    data["Vaccination Status"] = vaccinationStatus
    data["Email"] = email

    dictionary[fullname] = data
    print("\nProfile added!") 
 
# for command 2, access the dictionary and display dictionary values
def searchProfile(dictionary, search_query):
    print("\nWe have found the profile on our database!\n")
    
    if search_query in dictionary:
        for key,value in dictionary[search_query].items():
            print(key, ":", value)
        print()

    else:
        print("Item does not exist in our database.") 

# display menu
print("\nWELCOME TO CONTACT TRACING DATABASE")
print("~~~~~~Menu:~~~~~~")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit (y/n)")
print("~~~~~~~~~~~~~~~~~")

userCommandChoice = ""
allPersonalData = {}

# for command 3, enclose everything in a loop and add break statement to terminate
while True:
# ask user input for option selected
    try:
        print()
        userCommandChoice = int(input("Please select a command option (1-3): "))
        print()
    except:
        print("Invalid input. Make sure to enter a number from (1-3)")

    # create navigation to commands based on the input
    if userCommandChoice == 1:
        addItem(allPersonalData)

    elif userCommandChoice == 2:
        searchQuery = input("Enter the Fullname: ")
        searchProfile(allPersonalData, searchQuery)

    elif userCommandChoice == 3:
        exitBoolean = input("Do you wish to exit the program (y/n): ")
        if exitBoolean.lower() == "y":
            print("\nBye User!\n")
            break
        else:
            continue

    else:
        print("Command does not exist")






