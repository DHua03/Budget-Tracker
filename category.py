from database import initialize_database, add_transaction, get_transactions, get_balance

# You should have a Category class that accepts a name as the argument.
# The Category class should have an instance attribute ledger that is a list, and contains the list of transactions.
class Category:
    def __init__(self, name):
        self.name = name

    # A deposit method that accepts an amount and an optional description. 
    # If no description is given, it should default to an empty string. 
    # The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.
    def deposit(self, amount, description = ""):
        add_transaction(
            category = self.name,
            amount = amount,
            description = description,
            transaction_type = 'deposit'
            )
    
    # A withdraw method that accepts an amount and an optional description (default to an empty string). \
    # The method should store in ledger the amount passed in as a negative number, and should return True if the withdrawal succeeded and False otherwise.
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            add_transaction(
                category = self.name,
                amount = -amount,
                description = description,
                transaction_type = 'withdraw'
                )
            return True
        return False

    # A get_balance method that returns the current category balance based on ledger.
    def get_balance(self):
        return get_balance(self.name)

    # A transfer method that accepts an amount and another Category instance, withdraws the amount with description Transfer to [Destination],
    # deposits it into the other category with description Transfer from [Source], 
    # where [Destination] and [Source] should be replaced by the name of destination and source categories. 
    # The method should return True when the transfer is successful, and False otherwise.
    def transfer(self, amount, category):
        if self.check_funds(amount):
            add_transaction(
                category = self.name,
                amount = -amount,
                description = f'Transfer to {category.name}',
                transaction_type = 'transfer'
                )

            add_transaction(
                category = category.name,
                amount = amount,
                description = f'Transfer from {self.name}',
                transaction_type = 'transfer'
                )

            return True
        return False

    # A check_funds method that accepts an amount and returns False if it exceeds the balance or True otherwise. 
    #  This method must be used by both the withdraw and transfer methods.
    def check_funds(self, amount):
        return self.get_balance() >= amount

    # Display a title line of 30 characters with the category name centered between * characters.
    # List each ledger entry with up to 23 characters of its description left-aligned and the amount right-aligned (two decimal places, max 7 characters).
    # Show a final line Total: [balance], where [balance] should be replaced by the category total.
    def __str__(self):
        transactions = get_transactions(self.name)

        title = self.name.center(30, '*') + '\n'

        items = ''
        for entry in transactions:
            description = (entry[3] or '')[:23]
            amount = '{:2f}'.format(entry[2])[:7]
            items += f'{description:<23}{amount:>7}\n'
        
        total = f'Total: {get_balance(self.name)}'
        
        return title + items + total

# Have a function outside the Category class named create_spend_chart(categories) that takes a list of categories and returns a bar-chart string.
# title Percentage spent by category.
# Calculate percentages from withdrawals only and not from deposits. 
# The percentage should be the percentage of the amount spent for each category to the total spent for all categories (rounded down to the nearest 10).
# Label the y-axis from 100 down to 0 in steps of 10.
# Use o characters for the bars.
# Include a horizontal line two spaces past the last bar.
# Write category names vertically below the bar.
def create_spend_chart(categories):
    spent = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total += -item['amount']
        spent.append(total)

    total_spent = sum(spent)

    percentages = []
    for amount in spent:
        percent = int((amount / total_spent) * 100)
        percentages.append((percent // 10) * 10)

    chart = 'Percentage spent by category\n'

    for percentage in range(100, -1, -10):
        chart += f'{percentage:>3}|'

        for category_percent in percentages:
            if category_percent >= percentage:
                chart += ' o '
            else:
                chart += '   '

        chart += ' \n'
    
    chart += '    ' + '-' * (len(categories) * 3 + 1) + '\n'

    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        chart += "     "  # 5 leading spaces

        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "

        chart += "\n"

    return chart.rstrip('\n')

# Test Case
'''food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print()'''