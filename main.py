from category import Category
from database import initialize_database

def main():
    initialize_database()

    categories = {}

    while True:
        print("\n=== Budget Tracker ===")
        print("1. Create Category")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Category")
        print("6. View All Categories")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Category name: ")
            categories[name] = Category(name)
            print("Category created.")

        elif choice == "2":
            name = input("Category: ")
            amount = float(input("Amount: "))
            desc = input("Description: ")

            if name in categories:
                categories[name].deposit(amount, desc)
            else:
                print("Category not found.")

        elif choice == "3":
            name = input("Category: ")
            amount = float(input("Amount: "))
            desc = input("Description: ")

            if name in categories:
                success = categories[name].withdraw(amount, desc)
                print("Success" if success else "Insufficient funds")

        elif choice == "4":
            from_name = input("From category: ")
            to_name = input("To category: ")
            amount = float(input("Amount: "))

            if from_name in categories and to_name in categories:
                success = categories[from_name].transfer(amount, categories[to_name])
                print("Success" if success else "Failed transfer")

        elif choice == "5":
            name = input("Category: ")
            if name in categories:
                print(categories[name])
            else:
                print("Category not found.")

        elif choice == "6":
            if not categories:
                print("No categories created yet.")
            else:
                print("\n--- Categories ---")
                for name, cat in categories.items():
                    print(f"- {name}: ${cat.get_balance():.2f}")

        elif choice == "7":
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()