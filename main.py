import csv
import os

FILENAME = "transactions.csv"

def load_transactions():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None) #skip
        return [{"amount": float(a), "category": c, "note": n} for a, c, n in reader]

def save_transactions(transactions):
    with open(FILENAME, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["amount", "category", "note"])
        for t in transactions:
            writer.writerow([t["amount"], t["category"], t["note"]])
    print(f"Saved to {FILENAME}")

def add_transaction(transactions):
    try:
        amount = float(input("Amount (+income, -expense): "))
        category = input("Category: ").strip()
        note = input("Note: ").strip()
        transactions.append({"amount": amount, "category": category, "note": note})
        print("Added")
    except ValueError:
        print("Invalid amount.")

def view_transactions(transactions):
    if not transactions:
        print("No transactions.")
        return
    total = sum(t["amount"] for t in transactions)
    print("\nAmount | Category | Note")
    print("-" * 40)
    for t in transactions:
        print(f"{t['amount']:>7.2f} | {t['category']:<8} | {t['note']}")
    print("-" * 40)
    print(f"Total balance: ${total:.2f}")

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
