def bank():
    while True:
        balance = 0
        history = []
        max_balance = 10000
        max_withdraw = 400
        print("Start of a New Session ---")
        print("Welcome to our Bank! Type deposit, withdraw, balance, history, or exit.")
        while True:
            action = input("Enter action (deposit/withdraw/balance/history/exit): ").lower().strip()
            
            if action == "exit":
                print("Closing current Session ---")
                break
            
            elif action == "history":
                print(f"Final balance: {balance}")
                print(f"Action History: {history}")
                print("Thank you for using our Bank services!")

            elif action == "deposit":
                try:
                    amount_str = input("Enter the amount to deposit: ")
                    amount = int(amount_str)
                    if amount > 0:
                        if balance + amount > max_balance:
                            print(f"Maximum balance ({max_balance}) exceeded! Deposit rejected.")
                        else:
                            balance += amount
                            history.append(f"Deposited: {amount}")
                            print(f"Action completed perfectly.")
                    else:
                        print("You cannot deposit a negative amount or zero.")
                except:
                    print("Invalid amount! Please enter a number.")
            elif action == "withdraw":
                try:
                    amount_str = input("Enter the amount to withdraw: ")
                    amount = int(amount_str)

                    if amount > 0:
                        if amount > max_withdraw:
                            print(f"You cannot withdraw more than {max_withdraw} at once.")
                        elif amount > balance:
                            print("Insufficient funds! You cannot withdraw more than you have.")
                        else:
                            balance -= amount
                            history.append(f"Withdrew: {amount}")
                            print(f"Action completed perfectly.")
                    else:
                        print("You cannot withdraw a negative amount or zero.")
                except:
                    print("Invalid amount! Please enter a number.")

            elif action == "balance":
                print(f"Your current balance: {balance}")

            else:
                print("Invalid action. Please try again.")
bank()