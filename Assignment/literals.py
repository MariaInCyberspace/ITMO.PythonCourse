ADD_COMMAND = 'add'

SHOW_ALL_COMMAND = 'show all'

EXIT_COMMAND = 'exit'

DELETE_COMMAND = 'delete'

BY_NAME = 'name'

BY_NAME_DESC = '-name'

BY_CATEGORY = 'cat'

BY_CATEGORY_DESC = '-cat'

BY_PRICE = 'price'

BY_PRICE_DESC = '-price'

BY_DATE = 'date'

BY_DATE_DESC = '-date'

FILTER_BY_CATEGORY = 'filter-cat'

FILTER_BY_DATE = 'filter-date'

CATEGORY_NOT_FOUND = 'No such category. Please try again'

PURCHASES_FOR_DATE_NOT_FOUND = 'No purchases for this date. Please try again'

WHAT_PURCHASED_PROMPT = "What else have you purchased recently?\n"

CATEGORY_PROMPT = "What category would you put this item in?\n"

COST_PROMPT = "How much did it cost?\n"

DATE_PROMPT = "When did you make the purchase? (dd.mm.yyyy)\n"

CONTINUE_PROMPT = "\nWould you like to continue?\n\t" \
                  f"'{SHOW_ALL_COMMAND}':view list\n\t" \
                  f"'{FILTER_BY_CATEGORY}': filter by specified category / '{FILTER_BY_DATE}': filter by specified date\n\t" \
                  f"'{ADD_COMMAND}': add items\n\t" \
                  f"'{DELETE_COMMAND}': delete item\n\t" \
                  f"'{EXIT_COMMAND}': exit the program\n"

VIEW_LIST_PROMPT = f"\nWhat would you like to do?\n\t" \
                   f"'{SHOW_ALL_COMMAND}': view list\n\t" \
                   f"'{FILTER_BY_CATEGORY}': filter by specified category / '{FILTER_BY_DATE}': filter by specified date\n\t" \
                   f"'{ADD_COMMAND}': add purchase\n\t" \
                   f"'{DELETE_COMMAND}': delete item\n\t" \
                   f"'{EXIT_COMMAND}':exit\n"

HOW_TO_ORDER_LIST_FOR_VIEWING = "How would you like to view your list?\n\t" \
                                f"'{BY_NAME}' to view in alphabetical order / '{BY_NAME_DESC}' - descending\n\t" \
                                f"'{BY_CATEGORY}' to view by category / '{BY_CATEGORY_DESC}' - descending \n\t" \
                                f"'{BY_PRICE}' to view by price / '{BY_PRICE_DESC}' - descending \n\t" \
                                f"'{BY_DATE}' to view by date / '{BY_DATE_DESC}' - descending \n\t" \
                                f"'{SHOW_ALL_COMMAND}' to view raw\n"

DELETE_PROMPT = "Enter ID of a purchase you would like to delete:\n"

FILTER_BY_CATEGORY_PROMPT = "Enter category:\n"

FILTER_BY_DATE_PROMPT = "Enter date (dd.mm.yyyy):\n"

FILENAME = "purchases.csv"

DATE_FORMAT = "%d-%m-%Y"

DATE_FORMAT_FOR_READING = '%Y-%m-%d %H:%M:%S'

INCORRECT_DATE_MESSAGE = "Incorrect date"
