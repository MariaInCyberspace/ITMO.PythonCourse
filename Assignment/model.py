# This is a model of something I'd want to be saved in the database later
# It's expected that this app would help record all my expenses
# It would have to have the option to display those expenses by price and by category
# So, those two characteristics would have to be taken into account when designing this entity's structure
import datetime


class Purchase:
    # maybe add a description for any 'Expense' instance
    def __init__(self, name, category, price, date=datetime.datetime.now()):
        self.name = name
        self.category = category
        self.price = price
        self.date = date

