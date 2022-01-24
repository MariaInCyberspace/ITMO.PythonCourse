# This is a model of something I'd want to be saved in the database later
# It's expected that this app would help record all my expenses
# It would have to have the option to display those expenses by price and by category
# So, those two characteristics would have to be taken into account when designing this entity's structure
import datetime
import literals as lit
import csv


def read_file():
    all_purchases = []
    with open(lit.FILENAME, 'r') as purchases_csv:
        for line in purchases_csv.read().split("\n"):
            if line != "":
                elements = line.split(",")
                purchase = Purchase(elements[0], elements[1], elements[2], float(elements[3]),
                                    datetime.datetime.strptime(elements[4], lit.DATE_FORMAT_FOR_READING))
                all_purchases.append(purchase)
    return all_purchases


def write_to_file(purchases):
    with open(lit.FILENAME, 'a') as all_purchases:
        csvwriter = csv.writer(all_purchases)
        for p in purchases:
            row = [p.p_id, p.name, p.category, p.price, p.date]
            csvwriter.writerow(row)


def delete_purchase(p_id):
    all_purchases = read_file()
    for p in all_purchases:
        if p.p_id == p_id:
            all_purchases.remove(p)
    with open(lit.FILENAME, 'w') as altered_file:
        csvwriter = csv.writer(altered_file)
        for p in all_purchases:
            row = [p.p_id, p.name, p.category, p.price, p.date]
            csvwriter.writerow(row)


def filter_by_category(category):
    all_purchases = read_file()
    filtered = []
    for p in all_purchases:
        if p.category == category:
            filtered.append(p)
    return filtered


def filter_by_date(date):
    all_purchases = read_file()
    filtered = []
    for p in all_purchases:
        if p.date == date:
            filtered.append(p)
    return filtered


class Purchase:
    # maybe add a description for any 'Purchase' instance
    def __init__(self, p_id, name, category, price, date=datetime.datetime.now()):
        self.p_id = p_id
        self.name = name
        self.category = category
        self.price = price
        self.date = date
