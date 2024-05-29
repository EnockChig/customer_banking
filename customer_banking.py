# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings = float(input('Enter your savings account balance: '))
    interest_rate = float(input('Enter the interest rate for your savings account (in decimal form): '))
    months = int(input('Enter the number of months for which you want to calculate interest: '))


    # Call the create_savings_account function and pass the variables from the user.
    saving_balance, interest_earned= create_savings_account(savings,interest_rate,months)

    # Print out the intercest earned and updated savings account balance with interest earned for the sgiven months.
    print(f"Interest earned on savings balance: {interest_rate:.2f}")
    print(f"Updated savings balance with interest earned: {saving_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input('Enter your cd balance: '))
    cd_interest_rate = float(input('Enter the cd interest rate for your savings account (in decimal form): '))
    cd_months = int(input('Enter the number of months for which you want to calculate interest: '))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Interest earned on CD account: {interest_earned:.2f}")
    print(f"Updated CD account balance with interest earned: {updated_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()