import csv
import os

FILENAME = "transactions.csv"

def load_transactions():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None) #skip
        return [{"amount": float(a), "note": n} for a, n in reader]

def save_transactions(transactions):
    with open(FILENAME, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["amount", "note"])
        for t in transactions:
            writer.writerow([t["amount"], t["note"]])
    print(f"Saved to {FILENAME}")

def add_transaction(transactions):
    try:
        amount = float(input("Amount (+income, -expense): "))
        note = input("Note: ").strip()
        transactions.append({"amount": amount, "note": note})
        print("Added")
    except ValueError:
        print("Invalid amount.")

def view_transactions(transactions):
    if not transactions:
        print("No transactions.")
        return
    total = sum(t["amount"] for t in transactions)
    savings_target = total * 0.6
    spending_limit = total * 0.4

    total_spent = sum(t["amount"] for t in transactions if t["amount"] < 0)
    available_funds = spending_limit + total_spent
    
    print("\nAmount | Note")
    print("-" * 30)
    for t in transactions:
        print(f"{t['amount']:>7.2f} | {t['note']}")
    print("-" * 30)
    print(f"Total balance: ${total:.2f}")
    print(f"Savings goal (60%): ${savings_target:.2f}")
    print(f"Spending limit (40%): ${spending_limit:.2f}")
    print(f"Available to spend: ${available_funds:.2f}")

    if available_funds < 0:
        print("You’ve exceeded your 40% spending limit")


def main():
    transactions = load_transactions()
    while True:
        print("\n1. Add  2. View  3. Save  4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            save_transactions(transactions)
        elif choice == "4":
            save_transactions(transactions)
            print("Goodbye")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
