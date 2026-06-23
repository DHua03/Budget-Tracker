from category import Category
from database import initialize_database, get_transactions, get_balance

# reset / ensure DB exists
initialize_database()

'''
# create categories
food = Category("Food")
clothing = Category("Clothing")

print("\n--- TEST: DEPOSIT ---")
food.deposit(1000, "initial deposit")

print("Food transactions:", get_transactions("Food"))
print("Food balance:", food.get_balance())

print("\n--- TEST: WITHDRAW ---")
food.withdraw(50, "groceries")

print("Food transactions:", get_transactions("Food"))
print("Food balance:", food.get_balance())

print("\n--- TEST: TRANSFER ---")
food.transfer(100, clothing)

print("Food transactions:", get_transactions("Food"))
print("Clothing transactions:", get_transactions("Clothing"))

print("\n--- FINAL BALANCES ---")
print("Food balance:", food.get_balance())
print("Clothing balance:", clothing.get_balance())
'''

food = Category("Food")
print(food)
food.deposit(1000, "initial deposit")
food.withdraw(20, "groceries")
print(food)