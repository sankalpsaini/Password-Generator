# Written by Sankalp Saini 2022/2023

# import statements
import random
from os import system
import time

def getInputs():
    """Gets Inputs required to create password

    parameters:
    returns: 
        lengthOfPassword:int
        removeList:list
        accessList:list    
    """
    lengthOfPassword = input("\nHow long would you like the password to be (default 10)? ")
    try:
        int(lengthOfPassword)
    except:
        lengthOfPassword = "10"
    remove = input("Any special characters you would like to remove (enter character seperated by spaces or leave blank)? ")
    uppercase = input("Would you like uppercase letters? (yes/no): ")
    numbers = input("Would you like numbers? (yes/no): ")
    specialCharacters = input("Would you like special characters? (yes/no): ")

    uppercase = True if uppercase.lower()=="yes" else False
    numbers = True if numbers.lower()=="yes" else False
    specialCharacters = True if specialCharacters.lower()=="yes" else False

    # create array of which type of elements are required
    accessList = [uppercase, numbers, specialCharacters]

    # create array of special characters to remove
    removeList = remove.split()

    return lengthOfPassword, removeList, accessList

def getAccessibleCharacters(removeList):
    """Gets character lists for required password
    
    parameters:
        removeList:list
    returns: 
        specialCharacters:list
        capitalLetters:str
        lowercaseLetters:str    
    """
    specialCharacters = ["~","`","!","@",'#',"$","%","^","&","*","(",")","_","-","+","=","{","[","}","]","|",":",";","<",">",",",".","?","/","'",'"']
    
    # removes specified characters from special characters list
    for remove in removeList:
            if remove in specialCharacters:
                specialCharacters.remove(remove)

    capitalLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercaseLetters = "abcdefghijklmnopqrstuvwxyz"

    return specialCharacters, capitalLetters, lowercaseLetters

def createPassword(lengthOfPassword, accessList, specialCharacters, capitalLetters, lowercaseLetters):
    """Creates password using specified length and characters
    
    parameters:
        lengthOfPassword:int
        accessList:list
        specialCharacters:list
        capitalLetters:str
        lowercaseLetters:str 
    returns: 
        password:str   
    """
    password = ""

    # checks how many of each type of character is in the password string
    passwordPicks = {"capital":0, "numbers":0, "special":0}

    # add character randomly to return string
    while len(password) != int(lengthOfPassword):
        # higher probability for lowercase and uppercase characters
        pick = random.randint(0,5)
        if pick == 0 or pick == 4:
            password += random.choice(lowercaseLetters)
        elif (pick == 1 or pick == 5) and (accessList[0]):
            password += random.choice(capitalLetters)
            passwordPicks["capital"] += 1
        elif (pick == 2) and (accessList[2]):
            password += random.choice(specialCharacters)
            passwordPicks["special"] += 1
        elif (pick == 3) and (accessList[1]):
            password += str(random.randint(0,9))
            passwordPicks["numbers"] += 1
    
    # calls function to check if all requirements are met
    password = checkPasswordRequirements(password, accessList, passwordPicks, specialCharacters, capitalLetters)

    return password

def checkPasswordRequirements(password, accessList, passwordPicks, specialCharacters, capitalLetters):
    """Checks password to see if specified requirements are met
    
    parameters:
        password:str
        passwordPicks:dict
        specialCharacters:list
        capitalLetters:str
        lowercaseLetters:str 
    returns: 
        password:str   
    """

    # if any of the dict values are zero (and required, add random element of type into a random spot
    if passwordPicks["capital"] == 0 and accessList[0]:
        replace = random.randint(0,len(password)-1)
        password = password.replace(password[replace], random.choice(capitalLetters))
    if passwordPicks["special"] == 0 and accessList[2]:
        replace = random.randint(0,len(password)-1)
        password = password.replace(password[replace], random.choice(specialCharacters))
    if passwordPicks["numbers"] == 0 and accessList[1]:
        replace = random.randint(0,len(password)-1)
        password = password.replace(password[replace], str(random.randint(0,9)))
    
    return password

def saveToFile(website, password):
    """Saves the password and website.

    parameters:
        website:string
        password:string
    returns:   
    """
    # opens and appends to the file
    file = open("passwords.txt", "a")
    stringToAppend = '\nWebsite: "{website}" -- Password: {password}\n'.format( website=website, password=password)
    file.write(stringToAppend)
    file.close()
    print("\n\nPassword Saved - Taking you back to the main menu...\n")
    time.sleep(2.5)

def askToSave(password):
    """Asks the user if they would like to save the password
        If yes, calls saveToFile and exits.

    parameters: 
        password:string
    returns:   
    """
    save = input("Would you like to save this password? (yes/no): ")
    if save.lower() == "yes":
        website = input("What is the name of the website that you are using this password for? ")
        saveToFile(website, password)
    else:
        print("\n\nTaking you back to the main menu...\n")
        time.sleep(2.5)

def readFile(AUTH_PASS):
    """Reads from the Passwords File

    parameters: 
        AUTH_PASS:string
    returns:   
    """
    if AUTH_PASS == "":
        print("\nYou must first create a password (option 4 on main screen)!")
        print("\n\nTaking you back to the main menu...\n")
        time.sleep(2.5)
    else:
        # count to see how many attempts were made
        attemptCount = 0
        while (attemptCount < 3):
            # must enter the correct authentication password to access the file
            entryPassword = input("\nPlease enter your authentication password: ")
            # change password here to your choice!
            if entryPassword == AUTH_PASS:
                try:
                    file = open("passwords.txt", "r")
                    print("\n----------------------------------------------\n")
                    print(file.read())
                    print("\n----------------------------------------------\n")
                    input("\nEnter any key to close > ")
                    file.close()
                    print("\n\nTaking you back to the main menu...\n")
                    time.sleep(2.5)
                    break
                except:
                    print("\nThere is no file found to read!\n")
                    print("\n\nTaking you back to the main menu...\n")
                    time.sleep(2.5)
                    break
            elif (attemptCount < 2):
                print("Incorrect, please try again ({} attempt/s remaining).".format(str(3-attemptCount-1)))
            attemptCount += 1
        # automatic quit if too many attempts are made
        if (attemptCount == 3):
            print("\n\nToo many incorrect attempts. Goodbye.\n")
            quit()

def createNewPassword():
    """Creates a brand new password

    parameters:
    returns:   
    """
    # get inputs of desired password
    lengthOfPassword, removeList, accessList = getInputs()
    # get characters that are needed for password
    specialCharacters, capitalLetters, lowercaseLetters = getAccessibleCharacters(removeList)
    # create password
    password = createPassword(lengthOfPassword, accessList, specialCharacters, capitalLetters, lowercaseLetters)
    # clear terminal window
    system('clear')
    # print result
    print('\n\nYour password: ' + password + '\n\n')
    # ask to save the result in file
    askToSave(password)

def authPassword(AUTH_PASS):
    """Sets new authentication password

    parameters: 
        AUTH_PASS:string
    returns:   
        AUTH_PASS:string
    """
    if AUTH_PASS == "":
        print("\nYou have not yet set your own authorization password yet!")
    while True:
        newAuthPass = input("Please enter your new password (or enter 'quit'): ")
        if newAuthPass == "quit":
            print("\n\nTaking you back to the main menu...\n")
            time.sleep(2.5)
            break
        confirmAuthPass = input("Please confirm your new password: ")
        if newAuthPass == confirmAuthPass:
            AUTH_PASS = newAuthPass
            print("\nPassword changed!")
            print("\n\nTaking you back to the main menu...\n")
            time.sleep(2.5)
            return AUTH_PASS
        else:
            print("\nThe two passwords don't match!\n")
    

if __name__ == "__main__":

    AUTH_PASS = ""

    # infinite loop
    while True:
        system('clear')
        # retrieve mode
        print("\n    Welcome to Sankalp's password script!    ")
        print("----------------------------------------------\n\n")
        mode = input("Enter what you would like to do:\n1. Create new password\n2. Add a password to the file\n3. View the password file\n4. Create/change the authorization password\n5. Quit application\n\n> ")
        # create new password
        if mode == "1":
            createNewPassword()
        elif mode == "2":
            # save new password
            password = input("\nPlease enter the password you would like to save: ")
            website = input("What is the name of the website that you are using this password for? ")
            saveToFile(website, password)
        elif mode == "3":
            # read file
            readFile(AUTH_PASS)
        elif mode == "4":
            AUTH_PASS = authPassword(AUTH_PASS)
        elif mode == "5":
            # exit
            print("\nGoodbye :)\n")
            break