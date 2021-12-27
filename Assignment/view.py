import literals as lit


def display_info(info):
    print(info)


def display_purchases(purchases, how_to_proceed):
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
    print("Category\t\t\tProduct\t\t\tCost\t\t\tDate\t\t\t")
    result = "Category\t\t\tProduct\t\t\tCost\t\t\tDate\t\t\t"
    for p in sorted_list:
        print(f"{p.category}\t\t\t{p.name}\t\t\t{p.price}\t\t\t{p.date}")
        result += f"{p.category}\t\t\t{p.name}\t\t\t{p.price}\t\t\t{p.date}"

    return result
