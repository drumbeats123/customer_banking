# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account
import math

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def isint(num):
    if isfloat(num):
        new_num=math.floor(float(num))
        if float(num)-new_num==0:
            return True
        else:
            return False
    else:
        return False    


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """

    print("-" * 21)
    print((" " * 7) + "WELCOME" + (" " * 7))
    print("-" * 21)

    user_entry=True
    while user_entry:
        account_type = input("Which type of account would you like to check interest gained on? (S)avings or (C)D: ")

        match account_type.upper():
            case "S":
                # Prompt the user to set the savings balance, interest rate, and months for the savings account.
                # ADD YOUR CODE HERE
                validcheck=True
                while validcheck:
                    savings_balance = input('What is your savings account balance? ')
                    if isfloat(savings_balance):
                        validcheck=False
                        break
                    else:
                        print("Invalid input.")

                validcheck=True
                while validcheck:
                    savings_interest = input('What is the APR for the savings account? ')
                    if isfloat(savings_interest):
                        validcheck=False
                        break
                    else:
                        print("Invalid input.")

                validcheck=True
                while validcheck:
                    savings_maturity = input('How many months will the amount remain in the account? ')
                    if isint(savings_maturity):
                        validcheck=False
                        break
                    else:
                        print("Invalid input.")
                
                # Call the create_savings_account function and pass the variables from the user.
                new_savings_balance, savings_interest_earned = create_savings_account(float(savings_balance), float(savings_interest), int(savings_maturity))

                # Print out the interest earned and updated savings account balance with interest earned for the given months.
                # ADD YOUR CODE HERE

                print(f"Starting balance: ${float(savings_balance):.2f}")
                if isint(savings_interest):
                    savings_interest=int(float(savings_interest))
                else:
                    savings_interest=f"{int(float(savings_interest)):,.2f}"

                print(f"Interest Rate: {float(savings_interest)}% APR")
                print(f"Duration: {int(savings_maturity)} months\n")
                print(f"Interest Earned in {float(savings_maturity)} months: ${savings_interest_earned:,.2f}")
                print(f"New Balance: ${new_savings_balance:,.2f}")
                user_entry=False
            case "C":
                # Prompt the user to set the CD balance, interest rate, and months for the CD account.
                # ADD YOUR CODE HERE
                validcheck=True
                while validcheck:
                    cd_balance = input('What is your CD account balance? ')
                    if isfloat(cd_balance):
                        validcheck=False
                        break
                    else:
                        print("Invalid input.")

                validcheck=True
                while validcheck:
                    cd_interest = input('What is the APR for the CD account? ')
                    if isfloat(cd_interest):
                        validcheck=False
                        break
                    else:
                        print("Invalid input.")

                validcheck=True
                while validcheck:
                    cd_maturity = input('How many months before the CD account matures? ')
                    if isint(cd_maturity):
                        validcheck=False
                        break
                    else:
                        print("Invalid input.")




                # Call the create_cd_account function and pass the variables from the user.
                new_cd_balance, cd_interest_earned = create_cd_account(float(cd_balance), float(cd_interest), int(cd_maturity))

                # Print out the interest earned and updated CD account balance with interest earned for the given months.
                # ADD YOUR CODE HERE
                print(f"Starting balance: ${float(cd_balance):,.2f}")
                if isint(float(cd_interest)):
                    cd_interest=int(float(cd_interest))
                else:
                    cd_interest=f"{float(cd_interest):,.2f}"

                print(f"Interest Rate: {int(float(cd_interest))}% APR")
                print(f"Duration: {int(cd_maturity)} months\n")
                print(f"Interest Earned in {int(cd_maturity)} months: ${cd_interest_earned:,.2f}")
                print(f"New Balance: ${new_cd_balance:,.2f}")
                user_entry=False
            case _:
                print("Invalid entry.")

if __name__ == "__main__":
    # Call the main function.
    keep_checking=True
    while keep_checking:
        main()
        checking=input("Check another account (Y)es/(N)o? ")
        match checking.upper():
            case "Y":
                keep_checking=True
            case "N":
                print("Thank you for your visit! Have a nice day!")
                keep_checking=False
            case _:
                print("Invalid entry. ")
            
