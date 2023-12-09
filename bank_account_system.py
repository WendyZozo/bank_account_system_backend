"""
Project Name: Bank Account Manager
In this project, I created a program to manage bank accounts. 
The program allows users to create a new account, deposit and withdraw money from the account, and check the account balance.
"""
import random

# Use a dictionary to store the account details.
accounts = {}

def create_account(account_holder_name, password, initial_deposit):
    """
    Allow users to create a new bank account by inputting their name and an initial deposit.
    """
    # Generate a unique bank account number which will be used as the key of the account dictionary.
    account_number = random.randint(100000000000, 999999999999)
    while account_number in accounts:
        account_number = random.randint(100000000000, 999999999999)
    
    # Use dictionary to store the account details, including the account holder's name, account number, and account balance.
    accounts[account_number] = {'name': account_holder_name, 'password': password, 'balance': float(initial_deposit)}
    print("=====================================")
    print("Hello " + account_holder_name + "!")
    print("Account created successfully!")
    print("Account number: {}".format(account_number))
    print("Current Account Balance: ${}".format(initial_deposit))
    print("=====================================")


def deposit_money(account_number, amount):
    """
    Allow users to deposit money into their account.
    """
    if account_number in accounts:
        # Check if the deposit amount is numeric input
        try:
            amount = float(amount)
        except ValueError:
            print("============================================")
            print("Invalid deposit amount. Please enter number.")
            print("============================================")
            return
        # restriction: cannot enter negative numbers
        if amount <= 0:
            print("==============================================================")
            print("Invalid deposit amount. Please enter an amount greater than 0.")
            print("==============================================================")
        # add deposite amount to the account balance
        else:
            accounts[account_number]['balance'] += amount
            print("========================================")
            print("Deposit of ${} successful!".format(amount))
            print("Current Account Balance: ${}".format(accounts[account_number]['balance']))
            print("========================================")
    
    else:
        print("============================================")
        print("Invalid account. Please check and try again.")
        print("============================================")


def withdraw_money(account_number, amount):
    """
    Allow users to withdraw money from their account. 
    """
    if account_number in accounts:
        # Check if the withdraw amount is numeric input
        try:
            amount = float(amount)
        except ValueError:
            print("=============================================")
            print("Invalid withdraw amount. Please enter number.")
            print("=============================================")
            return
        
        # Check if the account balance is enough for withdraw
        if amount > 0 and amount <= accounts[account_number]['balance']:
            accounts[account_number]['balance'] -= amount
            print("========================================")
            print("Withdrawal of ${} successful!".format(amount))
            print("Current Account Balance: ${}".format(accounts[account_number]['balance']))
            print("========================================")
        elif amount > accounts[account_number]['balance']:
            print("=============================================")
            print("Sorry, you hava insufficient funds available.")
            print("=============================================")
        # restriction: cannot enter negative numbers
        else:
            print("===============================================================")
            print("Invalid withdraw amount. Please enter an amount greater than 0.")
            print("===============================================================")
    else:
        print("============================================")
        print("Invalid account. Please check and try again.")
        print("============================================")


def check_balance(account_number):
    """
    Display the current balance of the account.
    """
    if account_number in accounts:
        print("==========================================")
        print("Current Account Balance: ${}".format(accounts[account_number]['balance']))
        print("==========================================")
    else:
        print("============================================")
        print("Invalid account. Please check and try again.")
        print("============================================")


# interaction with user
def open_bank_application():
    exitCode = False
    while not exitCode:
        print("\n")
        print("================== Welcome to Jiamin's Bank ==================")
        print("1. Create a new bank account")
        print("2. Log in")
        print("3. Exit")
        option = input("Please select an option by entering a number from 1 to 3: ")

        if option == '1':
            account_holder_name = input("Please enter your name: ")
            password = input("Please enter a password for the account: ")
            initial_deposit = input("Please enter initial deposit amount: $")
            create_account(account_holder_name, password, initial_deposit)

        elif option == '2':
            account_number = input("Please enter your account number: ")
            password = input("Please enter your password: ")
            log_in(account_number, password)

        elif option == '3':
            exitCode = True

        else:
            print("==================================================")
            print("Invalid option. Please enter a number from 1 to 3.")
            print("==================================================")
    
    print("===============================================================")
    print("Thank you for using Jiamin's Bank Application. Have a good day!")
    print("===============================================================")

def log_in(account_number, password):
    try:
        account_number = float(account_number)
    except ValueError:
        print("=================================================================")
        print("Invalid account. Please enter vaild account number and try again.")
        print("=================================================================")
        return
    if account_number in accounts and password == accounts[account_number]['password']:
        user_operation(account_number)
    else:
        print("========================================================")
        print("Invalid account or password. Please check and try again.")
        print("========================================================")

def user_operation(account_number):
    exitCode = False
    while not exitCode:
        print("\n")
        print("===================== Hello {}! =====================".format(accounts[account_number]['name']))
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check current account balance")
        print("4. Exit")
        option = input("Please select an option by entering a number from 1 to 4: ")

        if option == '1':
            amount = input("Please enter deposit amount: $")
            deposit_money(account_number, amount)

        elif option == '2':
            amount = input("Please enter withdraw amount: $")
            withdraw_money(account_number, amount)

        elif option == '3':
            check_balance(account_number)

        elif option == '4':
            exitCode = True
        else:
            print("==================================================")
            print("Invalid option. Please enter a number from 1 to 4.")
            print("==================================================")
    
# Test case
open_bank_application()
        