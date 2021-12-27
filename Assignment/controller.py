import datetime
import csv

import model as m
import literals as lit
import view as v


new_expenses = []


def write_to_file(purchases):
    with open(lit.FILENAME, 'a') as all_purchases:
        csvwriter = csv.writer(all_purchases)
        for p in purchases:
            row = [p.name, p.category, p.price, p.date]
            csvwriter.writerow(row)


def read_file(purchases):
    all_purchases = purchases[:]
    with open(lit.FILENAME, 'r') as purchases_csv:
        for line in purchases_csv.read().split("\n"):
            if line != "":
                elements = line.split(",")
                purchase = m.Purchase(elements[0], elements[1], elements[2], elements[3])
                all_purchases.append(purchase)
    return all_purchases



def handle_new_purchase(purchases):
    name = input(lit.WHAT_PURCHASED_PROMPT).title()
    category = input(lit.CATEGORY_PROMPT).title()
    price = round(float(input(lit.COST_PROMPT).replace(",", ".")), 2)
    date_str = input(lit.DATE_PROMPT).replace(".", "-")
    try:
        if bool(datetime.datetime.strptime(date_str, lit.DATE_FORMAT)):
            date = datetime.datetime.strptime(date_str, lit.DATE_FORMAT)
            new_purchase = m.Purchase(name, category, price, date)
            purchases.append(new_purchase)
    except ValueError:
        v.display_info(lit.INCORRECT_DATE_MESSAGE)


command = input(lit.VIEW_LIST_PROMPT)

while command != lit.EXIT_COMMAND:
    if command == lit.SHOW_ALL_COMMAND:
        all_purchases = read_file(new_expenses)
        how_to_proceed = input(lit.HOW_TO_ORDER_LIST_FOR_VIEWING)
        v.display_purchases(all_purchases, how_to_proceed)
    if command == lit.ADD_COMMAND:
        handle_new_purchase(new_expenses)
    command = input(lit.CONTINUE_PROMPT)
    print()
if command == lit.EXIT_COMMAND:
    write_to_file(new_expenses)
    all_purchases = read_file(new_expenses)
    how_to_proceed = input(lit.HOW_TO_ORDER_LIST_FOR_VIEWING)
    v.display_purchases(all_purchases, how_to_proceed)
