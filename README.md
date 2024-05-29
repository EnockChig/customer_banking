CD Account Interest Calculator - README
This code provides functions to calculate interest earned on savings and CD accounts.

Files:

cd_account.py: Contains the create_cd_account function.
savings_account.py (assumed): Likely contains the create_savings_account function (not provided).
Account.py (assumed): Contains the Account class definition (not provided).
create_cd_account Function:

This function calculates the interest earned on a CD account for a specified period.

Arguments:
balance: The initial balance of the CD account (float).
interest_rate: The annual interest rate (APR) of the CD account (float in decimal form).
months: The number of months for which the interest is calculated (integer).
Returns:
A tuple containing two elements:
The updated CD account balance after adding the interest earned (float).
The interest earned on the CD account for the specified period (float).
How it Works:

Imports: The function imports the Account class from a separate file (Account.py).
Account Creation: It creates an instance of the Account class, passing the initial balance (balance) and an initial interest rate of 0 (0).
Interest Calculation: It calculates the interest earned using the formula: interest_earned = balance * (interest_rate / 100) * (months / 12).
Balance Update: It updates the account balance by adding the interest earned: updated_balance = balance + interest_earned.
Setting Interest and Balance: It assumes the Account class has methods set_balance and set_interest. It uses these methods to update the account's balance and interest rate within the instance (likely for record-keeping purposes).
Return Values: The function returns the updated balance and the interest earned as a tuple.
