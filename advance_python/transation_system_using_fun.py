users = {}
password = "1234"

def create_user(account_number, initial_balance):
    if account_number in users:
        print("Account already exists.")
    else:
        users[account_number] = {
            "balance": initial_balance,
            "transactions": []
        }
        print(f"Account {account_number} created successfully.")

def deposit(account_number, amount):
    if amount > 0:
        users[account_number]["balance"] += amount
        users[account_number]["transactions"].append(f"Deposited: {amount}")
        print(f"{amount} deposited successfully.")
    else:
        print("Invalid amount.")

def withdraw(account_number, amount):
    if 0 < amount <= users[account_number]["balance"]:
        users[account_number]["balance"] -= amount
        users[account_number]["transactions"].append(f"Withdrawn: {amount}")
        print(f"{amount} withdrawn successfully.")
    else:
        print("Invalid amount or insufficient balance.")

def view_transactions(account_number):
    transactions = users[account_number]["transactions"]
    if transactions:
        print("Transaction History:")
        for t in transactions:
            print(t)
    else:
        print("No transactions yet.")

def check_balance(account_number):
    print(f"Current Balance: {users[account_number]['balance']}")

def view_users():
    if users:
        print("Users:")
        for account_no, details in users.items():
            print(f"Account Number: {account_no}, Balance: {details['balance']}")
    else:
        print("No users found.")



while True:
    print("\n1. Create Account")
    print("2. Login")
    print("3. Exit")

    user_ip = int(input("Enter the choice: "))

    if user_ip == 1:
        acc = int(input("Enter account number: "))
        initial_bal = float(input("Enter initial balance: "))
        create_user(acc, initial_bal)

    elif user_ip == 2:
        acc = int(input("Enter the account number: "))

        if acc in users:
            passw = input("Enter the password: ")

            if passw == password:
                print("Login successful")

                while True:
                    print("\nMenu:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. View Transactions")
                    print("5. View Users")
                    print("6. exit")

                    choice = input("Choose an option (1-6): ")

                    if choice == '1':
                        amount = float(input("Enter deposit amount: "))
                        deposit(acc, amount)

                    elif choice == '2':
                        amount = float(input("Enter withdraw amount: "))
                        withdraw(acc, amount)

                    elif choice == '3':
                        check_balance(acc)

                    elif choice == '4':
                        view_transactions(acc)

                    elif choice == '5':
                        view_users()

                    elif choice == '6':
                        print("Log out")
                        break

                    else:
                        print("Invalid option.")
            else:
                print("Invalid password.")
        else:
            print("Account does not exist.")

    elif user_ip == 3:
        print("Exit")
        break

    else:
        print("Invalid choice.")