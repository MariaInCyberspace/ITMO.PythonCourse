import literals as lit


def display_info(info):
    print(info)


def display_purchases(purchases, how_to_proceed, logger):
    sorted_list = purchases[:]
    if how_to_proceed == lit.BY_NAME:
        sorted_list = sorted(purchases, key=lambda e: e.name)
    elif how_to_proceed == lit.BY_CATEGORY:
        sorted_list = sorted(purchases, key=lambda e: e.category)
    elif how_to_proceed == lit.BY_PRICE:
        sorted_list = sorted(purchases, key=lambda e: e.price)
    elif how_to_proceed == lit.BY_DATE:
        sorted_list = sorted(purchases, key=lambda e: e.date)
    else:
        pass
    print(f"Category{' ' * 12}Product{' ' * 23}Cost{' ' * 16}Date{' ' * 16}\n")
    for p in sorted_list:
        basic_length = 30
        values_to_alter = [str(p.category), str(p.name), str(p.price), str(p.date)]
        values_to_print = []
        for value in range(0, len(values_to_alter)):
            if len(values_to_alter[value]) < basic_length:
                if value != 1:
                    basic_length = 20
                    while len(values_to_alter[value]) < basic_length:
                        values_to_alter[value] += ' '
                else:
                    basic_length = 30
                    while len(values_to_alter[value]) < basic_length:
                        values_to_alter[value] += ' '
                # logger.info(f"'{values_to_alter[value]}'")
                values_to_print.append(values_to_alter[value])

        print(f"{values_to_print[0]}{values_to_print[1]}{values_to_print[2]}{values_to_print[3]}")


