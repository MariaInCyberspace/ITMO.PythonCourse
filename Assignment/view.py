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
    print(f"Category{' ' * 32}Product{' ' * 18}Cost{' ' * 21}Date{' ' * 21}\n")
    for p in sorted_list:
        basic_length = 40
        values_to_alter = [str(p.category), str(p.name), str(p.price), str(p.date)]
        values_to_print = []
        for value in range(0, len(values_to_alter)):
            if len(values_to_alter[value]) < basic_length:
                if value != 0:
                    basic_length = 25
                    while len(values_to_alter[value]) < basic_length:
                        values_to_alter[value] += ' '
                else:
                    while len(values_to_alter[value]) < basic_length:
                        values_to_alter[value] += ' '
                # logger.info(f"'{values_to_alter[value]}'")
                values_to_print.append(values_to_alter[value])

        print(f"{values_to_print[0]}{values_to_print[1]}{values_to_print[2]}{values_to_print[3]}")


