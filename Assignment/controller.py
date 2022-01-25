import datetime

import model as m
import literals as lit
import view as v
import logging
import logging.handlers


rfh = logging.handlers.RotatingFileHandler(
        filename='view.log',
        mode='a',
        maxBytes=5 * 1024 * 1024,
        backupCount=9,
        encoding=None,
        delay=0
)

logging.basicConfig(format='%(asctime)s: %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO, datefmt="%y-%m-%d %H:%M:%S",
                    handlers=[rfh])
logger = logging.getLogger('main')


def find_max_id(purchases):
    max_p = 0
    for p in purchases:
        if int(p.p_id) > max_p:
            max_p = int(p.p_id)
    return max_p


def check_id(p_id):
    is_valid = True
    try:
        int(p_id)
    except ValueError:
        v.display_info(lit.INCORRECT_ID_MESSAGE)
        is_valid = False
    return is_valid


def check_price(price):
    is_valid = True
    try:
        float(price)
    except ValueError:
        v.display_info(lit.INCORRECT_PRICE_MESSAGE)
        is_valid = False
    return is_valid


def check_date(date_entered):
    date_str = date_entered.replace(".", "-")
    is_valid = True
    try:
        datetime.datetime.strptime(date_str, lit.DATE_FORMAT)
    except ValueError:
        is_valid = False
        v.display_info(lit.INCORRECT_DATE_MESSAGE)
    return is_valid


def convert_to_date(date_entered):
    date_str = date_entered.replace(".", "-")
    date = datetime.datetime.strptime(date_str, lit.DATE_FORMAT)
    return date


def handle_new_purchase(purchases):
    all_purch = m.read_file()
    p_id = find_max_id(all_purch) + 1
    name = input(lit.WHAT_PURCHASED_PROMPT).title()
    category = input(lit.CATEGORY_PROMPT).title()
    price_str = input(lit.COST_PROMPT).replace(",", ".")
    date_str = input(lit.DATE_PROMPT)
    if check_date(date_str) & check_price(price_str):
        date = convert_to_date(date_str)
        price = round(float(price_str), 2)
        new_purchase = m.Purchase(p_id, name, category, price, date)
        purchases.append(new_purchase)
        m.write_to_file(purchases)


def run_app():
    new_purchases = []
    command = input(lit.VIEW_LIST_PROMPT)
    while command != lit.EXIT_COMMAND:
        if command == lit.SHOW_ALL_COMMAND:
            all_purchases = m.read_file()
            how_to_proceed = input(lit.HOW_TO_ORDER_LIST_FOR_VIEWING)
            v.display_purchases(all_purchases, how_to_proceed, logger)
        if command == lit.ADD_COMMAND:
            handle_new_purchase(new_purchases)
            new_purchases = []
        if command == lit.DELETE_COMMAND:
            all_purchases = m.read_file()
            how_to_proceed = lit.SHOW_ALL_COMMAND
            v.display_purchases(all_purchases, how_to_proceed, logger)
            id_to_delete = input(lit.DELETE_PROMPT)
            if check_id(id_to_delete):
                if m.delete_purchase(id_to_delete):
                    all_purchases = m.read_file()
                    v.display_purchases(all_purchases, how_to_proceed, logger)
                else:
                    v.display_info(lit.NO_PURCHASES_WITH_THIS_ID_FOUND)
        if command == lit.FILTER_BY_CATEGORY:
            category = input(lit.FILTER_BY_CATEGORY_PROMPT)
            filtered = m.filter_by_category(category)
            if len(filtered) > 0:
                how_to_proceed = input(lit.HOW_TO_ORDER_LIST_FOR_VIEWING)
                v.display_purchases(filtered, how_to_proceed, logger)
            else:
                v.display_info(lit.CATEGORY_NOT_FOUND)
        if command == lit.FILTER_BY_DATE:
            date_entered = input(lit.FILTER_BY_DATE_PROMPT)
            if check_date(date_entered):
                date = convert_to_date(date_entered)
                filtered = m.filter_by_date(date)
                if len(filtered) > 0:
                    how_to_proceed = input(lit.HOW_TO_ORDER_LIST_FOR_VIEWING)
                    v.display_purchases(filtered, how_to_proceed, logger)
                else:
                    v.display_info(lit.PURCHASES_FOR_DATE_NOT_FOUND)
        command = input(lit.CONTINUE_PROMPT)
        print()
