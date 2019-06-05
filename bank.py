from customer import *
import time
import sys
import random
import string
import re


def checkSSN(x):
    pattern=re.compile(r'^\d{3}-\d{2}-\d{4}$')
    
    return bool(re.match(pattern, x))


age = 0
deposit = 0

try:
    print("Welcome to Sammy Bank! \nLet's get you registered.")
    print("\nFirst, what's your first name?")
    first_name = input()
    print("\nAnd your last name?")
    last_name = input()
    print("\nThanks! " + first_name + " " + last_name + "! Now, how old are you?")
    try:
        raw_age = input()
        age = int(str(raw_age))
    except:
        print("\nNot a number.")
        raise SystemExit
    
    print("\nGreat! We need your SSN for identification purposes. Please enter your valid social security card number now.")
    ssn = input()
    if checkSSN(ssn) == True:
        print("\nGotcha. And what's your address?")
        address = input()
    else:
        print("\nInvalid SSN.")
        raise SystemExit
    
    print("\nWonderful! Lastly, all customers must deposit a security deposit greater than $500 for first time use, " +
          "How much would you like to deposit?")
    raw_deposit = input()
    deposit = int(str(raw_deposit))
        
    if deposit < 500:
        print("\nInsuffucient Deposit.")
        raise SystemExit
        
    else:
        me = Customer(first_name, last_name, age, deposit, ssn, address)
        print("\nSuccessfully registered!")
            
except:
    print("\nFailed to register. For more information, contact customer service.")
    raise SystemExit



def verification():

    dList = ', '.join((random.choice(string.ascii_letters + string.digits)) for x in range(10))
    
    print("\n!!!\nTo ensure security measures, we need you to perform a human verification. \nFollow the prompt carefully.")
    promptA = "\nType out all numbers in this list in order" + "\n" + dList + "\nIf there is no such element, just hit enter."
    promptB = "\nType out all letters (case-sensative) in this list in order" + "\n" + dList + "\nIf there is no such element, just hit enter."
    realPrompt = [promptA, promptB]
    myChoice = random.choice(realPrompt)
    print(myChoice)

    if myChoice == promptA:
        answer1 = ", ".join([x for x in dList if x.isdigit()])
        answer2 = ",".join([x for x in dList if x.isdigit()])
        answer3 = "".join([x for x in dList if x.isdigit()])
        userAnswer = input()
        if userAnswer == answer1 or userAnswer == answer2 or userAnswer == answer3:
            print("\nVerification success!")
            return True
        else:
            return False

    elif myChoice == promptB:
        answer1 = ", ".join([x for x in dList if x.isalpha()])
        answer2 = ",".join([x for x in dList if x.isalpha()])
        answer3 = "".join([x for x in dList if x.isalpha()])
        userAnswer = input()
        if userAnswer == answer1 or userAnswer == answer2 or userAnswer == answer3:
            print("\nVerification success!")
            return True
        
        else:
            return False

def departmentExtension():
    dictionary = {'Banking': 100, 'Investing':200, 'Customer Service':888, 'Risk Management':999}
    print("\nBank Roster")
    print("----------------------------------------------------------------------------")
    print("Departments extension available for contacting:")
    print("1. Banking Department")
    print("2. Investing Department")
    print("3. Customer Service Department")
    print("4. Risk Management")
    print("\nType any of the number or phrase to see their respective extension.")
    print("\nIf you want to see all departments that have an extension less than 300... \nPleasetype '<300'")
    print("\nIf you want to see all departments that have an extension greater than 300... \nPlease type '>300'")

    decision = input()

    try:
        if decision == "banking" or decision == "banking department" or decision == "1":
            print ("The extension for BANKING DEPARTMENT is :", dictionary['Banking'])
            print("\nType: menu() to get back to the user menu.")

        elif decision == "investing" or decision == "investing department" or decision == "2":
            print ("The extension for INVESTING DEPARTMENT is :", dictionary['Investing'])
            print("\nType: menu() to get back to the user menu.")

        elif decision == "customer service" or decision == "customer service department" or decision == "customer" or decision == "customer support" or decision == "3":
            print ("The extension for CUSTOMER SUPPORT DEPARTMENT is :", dictionary['Customer Service'])
            print("\nType: menu() to get back to the user menu.")

        elif decision == "risk" or decision == "risk management department" or decision == "risk management" or decision == "4":
            print ("The extension for INVESTING DEPARTMENT is :", dictionary['Risk Management'])
            print("\nType: menu() to get back to the user menu.")

        elif decision == "<300":
            y = {x: dictionary[x] for x in dictionary if dictionary[x] < 300}
            print(y)
            print("\nType: menu() to get back to the user menu.")

        elif decision == ">300":
            y = {x: dictionary[x] for x in dictionary if dictionary[x] > 300}
            print(y)
            print("\nType: menu() to get back to the user menu.")
            
    except:
        print("\nInvalid Request.")
        print("\nType: menu() to get back to the user menu.")

def menu():
    print()
    print("\nMAIN [menu()] MENU (Press the corresponding number or phrase to use.) " + "\n==========================================================================")
    print("1. Personal Information")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Apply for Credit Card")
    print("5. Department Roster")

    decision = input()

    try:
        if decision == "info" or decision == "personal info" or decision == "personal information" or decision == "1" :
            if verification() == True:
                me.personalInfo()
            else:
                print("\nVerification failed.")
                print("\nType: menu() to get back to the user menu.")
        elif decision == "deposit" or decision == "2" :
            if verification() == True:
                me.deposit()
            else:
                print("\nVerification failed.")
                print("\nType: menu() to get back to the user menu.")
        elif decision == "withdraw" or decision == "3":
            if verification() == True:
                me.withdraw()
            else:
                print("\nVerification failed.")
                print("\nType: menu() to get back to the user menu.")
        elif decision == "apply" or decision == "apply for credit card" or decision == "apply credit card" or decision == "credit card" or decision == "credit" or decision == "4":
            me.apply_creditcard()
        elif decision == "department roster" or decision == "roster" or decision == "departments" or decision == "5":
            departmentExtension()
    except:
        print("Unknown error. Please try again.")
        print("\nType: menu() to get back to the user menu.")
        menu()


    
if __name__ == "__main__":
    menu()
    
