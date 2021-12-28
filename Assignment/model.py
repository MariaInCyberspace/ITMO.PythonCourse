# This is a model of something I'd want to be saved in the database later
# It's expected that this app would help record all my expenses
# It would have to have the option to display those expenses by price and by category
# So, those two characteristics would have to be taken into account when designing this entity's structure
import datetime
import literals as lit
import csv


class Purchase:
    # maybe add a description for any 'Purchase' instance
    def __init__(self, name, category, price, date=datetime.datetime.now()):
        self.name = name
        self.category = category
        self.price = price
        self.date = date


def write_to_file(purchases):
    with open(lit.FILENAME, 'a') as all_purchases:
        csvwriter = csv.writer(all_purchases)
        for p in purchases:
            row = [p.name, p.category, p.price, p.date]
            csvwriter.writerow(row)


def read_file():
    all_purchases = []
    with open(lit.FILENAME, 'r') as purchases_csv:
        for line in purchases_csv.read().split("\n"):
            if line != "":
                elements = line.split(",")
                purchase = Purchase(elements[0], elements[1], float(elements[2]),
                                    datetime.datetime.strptime(elements[3], lit.DATE_FORMAT_FOR_READING))
                all_purchases.append(purchase)
    return all_purchases
