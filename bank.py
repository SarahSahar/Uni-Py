bank = []

total = int(input("How many accounts do you want to create? "))

for i in range(1, total + 1):
    user = input(f"Owner name for account {i}: ")
    money = float(input("Initial balance: "))
    bank.append([user, money])

while True:
    print("\n--- Banking Menu ---")
    print("1) Show all accounts")
    print("2) Deposit")
    print("3) Withdraw")
    print("4) Accounts above average balance")
    print("5) Exit")

    opt = input("Choose an option: ")

    if opt == "1":
        print("\nAccounts list:")
        for acc in bank:
            print(f"{acc[0]} : {acc[1]}")

    elif opt == "2":
        user = input("Enter account name: ")
        val = float(input("Deposit amount: "))
        for acc in bank:
            if acc[0] == user:
                acc[1] += val
                print("Deposit completed.")
                break
        else:
            print("Account not found.")

    elif opt == "3":
        user = input("Enter account name: ")
        val = float(input("Withdraw amount: "))
        for acc in bank:
            if acc[0] == user:
                if acc[1] >= val:
                    acc[1] -= val
                    print("Withdrawal completed.")
                else:
                    print("Insufficient balance.")
                break
        else:
            print("Account not found.")

    elif opt == "4":
        if len(bank) == 0:
            print("No accounts available.")
        else:
            avg = sum(a[1] for a in bank) / len(bank)
            print(f"\nAverage balance: {avg}")
            print("Accounts above average:")
            for acc in bank:
                if acc[1] > avg:
                    print(f"{acc[0]} : {acc[1]}")

    elif opt == "5":
        print("Program terminated.")
        break

    else:
        print("Invalid option.")
