import time
import array

class Customer:
    def __init__(self, first_name, last_name, age, balance, ssn, address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.balance = balance
        self.creditcardEligible = False
        self.ssn = ssn
        self.address = address

    def setfName(self, first_name):
        self.first_name = first_name

    def getfName(self):
        return self.first_name

    def setlName(self, last_name):
        self.last_name = last_name

    def getlName(self):
        return self.last_name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setSSN(self, ssn):
        self.ssn = ssn

    def getSSN (self):
        return self.ssn

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address

    def setBalance(self, balance):
        self.balance = balance

    def getBalance(self):
        return self.balance

    def give(self, x):
        self.balance += x

    def take(self, x):
        self.balance -= x

    def changeCreditStatus(self, x):
        try:
            if x == "true":
                self.creditcardEligible = True
            elif x == "false":
                self.creditcardEligible = False
        except:
            print("Failed to change credit status.")
            print("\nType: menu() to get back to the user menu.")
            
        
    def deposit(self):
        ext = -1
        confirmDeposit = -1
        confirmDepositQuit = -1


        while(ext!=1):
            print("\nDeposit")
            print("----------------------------------------------------------------------------")
            print("How much money would you like to deposit?")
            depositString = input()
            try:
                deposit = int(str(depositString))
                while (deposit <= 0):
                    print("\nYou cannot deposit a negative balance! Please try again!")
                    depositString = input()
                    deposit = int(str(depositString))
                print("\nAre you sure you want to deposit: $" + depositString + "?\nPress 1 to confirm.")
                confirmDeposit = int(str(input()))
                if(confirmDeposit == 1):
                    self.balance += deposit
                    print("\nSuccess! Your new bank balance after depositing $" + depositString +
                          " is: $" + str(int(self.balance)) +
                          ".\nWould you like to continue?\nPress 1 to continue depositing.\nPress anything else to quit.")
                    confirmDepositQuit = input()
                    if(confirmDepositQuit == "1"):
                        ext = -1
                    else:
                        print("\nTransaction complete.")
                        print("\nType: menu() to get back to the user menu.")
                        ext = 1
                        break
                
                else:
                    print("\nTransaction canceled.")
                    print("\nType: menu() to get back to the user menu.")
                    exit = 1
                    break
                    
            except:
                print("\nException: Not a valid confirmation.")
                print("\nType: menu() to get back to the user menu.")
                break

    def withdraw(self):
        ext = -1
        confirmWithdraw = -1
        confirmWithdrawQuit = -1


        while(ext!=1):
            print("\nWithdrawal")
            print("----------------------------------------------------------------------------")
            print("How much money would you like to withdraw?")
            withdrawString = input()

            try:
                withdraw = int(str(withdrawString))
                while (withdraw <= 0):
                    print("\nYou cannot withdraw a negative balance! Please try again!")
                    withdrawString = input()
                    withdraw = int(str(withdrawString))
                print("\nAre you sure you want to withdraw: $" + withdrawString + "?\nPress 1 to confirm.")
                confirmWithdraw = int(str(input()))
                if(self.balance-withdraw < 0 and self.creditcardEligible == False):
                    print("\nYou are withdrawing more than what you already have! Apply credit card to enable overdraft! \nTransaction failed.")
                    print("\nType: menu() to get back to the user menu.")
                    break
                
                else:
                    if(confirmWithdraw == 1):
                        self.balance -= withdraw
                        print("\nSuccess! Your new bank balance after withdrawing $" + withdrawString +
                              " is: $" + str(int(self.balance)) +
                              ".\nWould you like to continue?\nPress 1 to continue withdrawing.\nPress anything else to quit.")
                        confirmWithdrawQuit = input()
                        if(confirmWithdrawQuit == "1"):
                            ext = -1
                        else:
                            print("\nTransaction complete.")
                            print("\nType: menu() to get back to the user menu.")
                            ext = 1
                            break
                    
                    else:
                        print("\nTransaction canceled.")
                        print("\nType: menu() to get back to the user menu.")
                        ext = 1
                        break
                        
            except:
                    print("\nException: Not a valid confirmation.")
                    print("\nType: menu() to get back to the user menu.")
                    break

    def scoreEval(self):
        if self.balance <= 0:
            return 0
        elif self.balance > 0 and self.balance <= 200:
            return 300
        elif self.balance > 200 and self.balance <=400:
            return 350
        elif self.balance > 400 and self.balance <=800:
            return 400
        elif self.balance > 800 and self.balance <=1500:
            return 450
        elif self.balance > 1500 and self.balance <=3000:
            return 500
        else:
            return 650 + self.balance*0.01

    def balanceNegEval(self):
        if self.balance < 0:
            return True
        else:
            return False


    def ageEval(self):
        if self.age >= 18:
            return True
        else:
            return False


        
    def apply_creditcard(self):

        qAge = self.ageEval()
        qScore = self.scoreEval()
        qNegative = self.balanceNegEval()
        qArray = array.array('i',[0,0,0])
        qString = ""
        qualified = False

        print("\nApply For Credit Card")
        print("----------------------------------------------------------------------------")
        print("According to Sammy Bank regulations, all customers who intend to apply for a credit card must be over 18, " +
              "has a virtual safety score over 650, and must not have a negative balance in their account. We will now check " +
              "if you have met these criterias. Please wait...")

        time.sleep(5)

        print("\n***EVALUATION RESULT***")

        time.sleep(3)
        if (qAge == True):
            qString = "PASSED"
            qArray[0] = 1
        else:
            qString = "FAILED"
            qArray[0] = 0

        print("AGE = " + str(int(self.age)) + " ... " + qString)

        time.sleep(3)
        if (qScore > 650):
            qString = "PASSED"
            qArray[1] = 1
        else:
            qString = "FAILED"
            qArray[1] = 0

        print("SAFETY SCORE = " + str(int(qScore)) + " ... " + qString)
        
        time.sleep(3)
        if (qNegative == False):
            qString = "PASSED"
            qArray[2] = 1
        else:
            qString = "FAILED"
            qArray[2] = 0

        print("POSITIVE BANK BALANCE = $" + str(int(self.balance)) +" ... " + qString)                

        if all(qArray) == 1:
            print("\nRESULT: CONGRATULATIONS! YOU ARE CREDIT-CARD ELIGIBLE AND CAN NOW OVERDRAFT.")
            print("\nType: menu() to get back to the user menu.")
            self.qualified = True

        else:
            print("\nRESULT: QUALIFICATION FAILED. PLEASE MAKE SURE YOU MEET THE REQUIREMENTS!")
            print("\nType: menu() to get back to the user menu.")
            self.qualified = False

    def personalInfo(self):
        print("\nInformation for Customer - " + self.first_name + " " + self.last_name + ":")
        print("----------------------------------------------------------------------------")
        print("First Name: " + self.getfName())
        print("Last Name: " + self.getlName())
        print("Age: " + str(int(self.getAge())))
        print("SSN: " + self.getSSN())
        print("Address: " + self.getAddress())
        print("Balance: $" + str(int(self.getBalance())))
        print("Credit Card Eligible?: " + str(bool(self.creditcardEligible)))
        print("\nType: menu() to get back to the user menu.")
