import hashlib

users = {}

def register():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password for security

    users[username] = hashed_password
    print(f"User {username} registered successfully!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the entered password

    if username in users and users[username] == hashed_password:
        print(f"Welcome back, {username}!")
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False

user_balance = 0  # Starting balance for the user

def deposit():
    global user_balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        user_balance += amount
        print(f"Deposited {amount}. New balance: {user_balance}")
    else:
        print("Amount should be positive.")

def withdraw():
    global user_balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > 0 and amount <= user_balance:

        user_balance -= amount
        print(f"Withdrew {amount}. New balance: {user_balance}")
    else:
        print("Insufficient funds or invalid amount.")

transactions = []  # List to store transaction details

def add_transaction(type, amount):
    transactions.append(f"{type}: {amount}")
    print(f"Transaction {type} of {amount} recorded.")

def view_transactions():
    print("\nTransaction History:")
    for transaction in transactions:
        print(transaction)


def main():
    while True:
        print("\n--- Bank System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            if login():
                # If login is successful, show options for deposit, withdrawal, etc.
                while True:
                    print("\n--- Welcome to Your Bank Account ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. View Transactions")
                    print("4. Logout")
                    user_choice = input("Select an option: ")

                    if user_choice == "1":
                        deposit()
                        add_transaction("Deposit", user_balance)
                    elif user_choice == "2":
                        withdraw()
                        add_transaction("Withdraw", user_balance)
                    elif user_choice == "3":
                        view_transactions()
                    elif user_choice == "4":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice, please try again.")

            elif choice == "3":
                print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


main()