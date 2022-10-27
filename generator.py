# import statements
import random
from os import system


def getInputs():
    """Gets Inputs required to create password

    parameters:
    returns: 
        lengthOfPassword:int
        removeList:list
        accessList:list    
    """
    lengthOfPassword = input("How long would you like the password to be? ")
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


if __name__ == "__main__":
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