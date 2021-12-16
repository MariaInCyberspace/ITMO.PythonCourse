
# A function that returns a list of random integers
def get_list_of_random_integers(size):
    import random
    list_of_numbers = []
    for i in range(0, size):
        list_of_numbers.append(random.randint(0, 100))
    return list_of_numbers