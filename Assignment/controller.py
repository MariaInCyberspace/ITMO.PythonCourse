import datetime

import model as m
import literals as lit
import view as v


new_purchases = []


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
    m.write_to_file(purchases)


command = input(lit.VIEW_LIST_PROMPT)

while command != lit.EXIT_COMMAND:
    if command == lit.SHOW_ALL_COMMAND:
        all_purchases = m.read_file()
        how_to_proceed = input(lit.HOW_TO_ORDER_LIST_FOR_VIEWING)
        v.display_purchases(all_purchases, how_to_proceed)
    if command == lit.ADD_COMMAND:
        handle_new_purchase(new_purchases)
    command = input(lit.CONTINUE_PROMPT)
    print()

