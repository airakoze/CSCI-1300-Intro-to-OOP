##################################################################
# Student contributions to the interest calculator
#
# You are free to add additional utility functions as you see fit,
# but you must implement each of the following functions while
# adhering to the specifications given in the project description
##################################################################

#---------------------------------------------------------------------------------


def greeting():
    print("This interest calculator will ask you to select an interest rate,\nfollowed by a principal value. It will then calculate and display the principal, interest rate, and balance after one year. You will then\n be invited to execute the process again or terminate.")
    print()

#---------------------------------------------------------------------------------

def getRate(choices):
    interestRate = choices
    rateChoices = ["A", "B", "C", "D", "E", "F"]
    done = False
    while not done:
        print("Please select an interest rate:")
        
        # Displaying the choices
        for k in range(len(interestRate)):
            print(rateChoices[k] + ") " + f'{str(interestRate[k]):>2}' + "%")
        
        # Entering a choice
        choice = input(f'Enter A-{rateChoices[(len(interestRate)-1)]}: ')
        if choice.upper() in rateChoices[:(len(interestRate))]:
            done = True
            return interestRate[rateChoices.index(choice.upper())]/100
        else:
            print("That is not a valid selecion.")
        print()
#---------------------------------------------------------------------------------

def getPrincipal(limit):
    done = False
    while not done:
        try:
            principal = input(f'Enter the principal (limit {limit}): ')
            if principal[0] == "$":
                principal = float(principal[1:])
            if principal[1] == "$":
                principal = float(principal[:1] + principal[2:])
            else:
                principal = float(principal)
        except ValueError:
             print("Please enter a number")
             continue
        
        # Checking if the principal fulfills the conditions
        if principal < 0:
            print("You must enter a positive amount.")
        elif principal > limit:
            print(f'The principal can be at most {limit}.')
        elif '.' in str(principal):
            if str(principal)[-3] == "." or str(principal)[-2] == ".":
                return float(principal)
            else:
                print("The principal must be specified in dollars and cents.")
        else:
            done = True
            return float(principal)
#---------------------------------------------------------------------------------

def computeBalance(principal, rate):
    return principal + (principal * rate)

#---------------------------------------------------------------------------------

def displayTable(principal, rate, balance):
    header = "Initial Principal   Interest Rate   End of Year Balance"
    print(header)
    print(f'{"="*len(header)}')
    principal = f'{principal:.2f}'
    balance = f'{balance:.2f}'
    print(f'{("$"+principal):20}{rate:<16}{("$"+balance)}')
    print()

#---------------------------------------------------------------------------------

def askYesNo(prompt):
    done = False
    while not done:
        choice = input(prompt)
        choice = choice.strip() # Removing the leading and trailing whitespaces
        if choice[0] in ["y", "Y"]:
            done = True
            return True
        elif choice[0] in ["n", "N"]:
            done = True
            return False
        else:
            print("That is not a valid selection.")
    

#---------------------------------------------------------------------------------

# For Extra Credit 

def displayExtendedTable(principal, rate, balance):
    months = ["Jan","Feb", "Mar", "Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    header = "Month   Starting Balance    APR     Ending Balance"
    
    print(header)
    print(f'{"="*len(header)}')
    
    # Monthly values
    monthlyRate = pow(1+rate, 1.0/12) - 1
    startingBalance = [f'{principal:.2f}']
    endingBalance = []
    startingValue = principal
    for k in range(len(months)):
        monthlyValue = (monthlyRate * startingValue) + startingValue
        startingBalance.append(f'{monthlyValue:.2f}')
        endingBalance.append(f'{monthlyValue:.2f}')
        startingValue = monthlyValue
        
    # Printing values as a table
    w = max([len(k) for k in endingBalance])
    for l in range(len(months)):
        startingBalance[l] = f'{startingBalance[l]:>{w}}'
        endingBalance[l] = f'{endingBalance[l]:>{w}}'
        result = f"{months[l]:8}{('$'+startingBalance[l]):20}{rate:<8}{('$'+endingBalance[l])}"
        print(result)

