

ADD_COMMAND = 'add'

SHOW_ALL_COMMAND = 'show all'

EXIT_COMMAND = 'exit'

DELETE_COMMAND = 'delete'

BY_NAME = 'name'

BY_CATEGORY = 'cat'

BY_PRICE = 'price'

BY_DATE = 'date'

WHAT_PURCHASED_PROMPT = "What else have you purchased recently?\n"

CATEGORY_PROMPT = "What category would you put this item in?\n"

COST_PROMPT = "How much did it cost?\n"

DATE_PROMPT = "When did you make the purchase? (dd.mm.yyyy)\n"

CONTINUE_PROMPT = "Would you like to continue?\n\t" \
                  f"'{SHOW_ALL_COMMAND}':view differently\n\t" \
                  f"'{ADD_COMMAND}': add items\n\t" \
                  f"'{DELETE_COMMAND}': delete list\n\t" \
                  f"'{EXIT_COMMAND}': exit the program\n"

AFTER_VIEWING_PROMPT = "What is it that you'd like to do?\n\t" \
                       f"'{DELETE_COMMAND}': delete list\n\t" \
                       f"'{SHOW_ALL_COMMAND}':view differently\n\t" \
                       f"'{ADD_COMMAND}': add item\n\t" \
                       f"'{EXIT_COMMAND}': exit the program\n"

VIEW_LIST_PROMPT = f"Would you like to view the list of your purchases?\n\t" \
                   f"'{SHOW_ALL_COMMAND}': view list\n\t" \
                   f"'{ADD_COMMAND}': add purchase\n\t" \
                   f"'{EXIT_COMMAND}':exit\n"

HOW_TO_ORDER_LIST_FOR_VIEWING = "How would you like to view your list?\n\t" \
                                f"'{BY_NAME}' to view in alphabetical order\n\t" \
                                f"'{BY_CATEGORY}' to view by category\n\t" \
                                f"'{BY_PRICE}' to view by price\n\t" \
                                f"'{BY_DATE}' to view by date\n\t" \
                                f"{SHOW_ALL_COMMAND} to view raw\n"

FILENAME = "purchases.csv"

DATE_FORMAT = "%d-%m-%Y"

INCORRECT_DATE_MESSAGE = "Incorrect date"
