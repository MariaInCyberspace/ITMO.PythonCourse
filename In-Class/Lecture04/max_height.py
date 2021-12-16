def get_max_height():
    height1 = int(input("Enter your height please:\n"))
    height2 = int(input("Enter another height please:\n"))
    if height1 > height2:
        print(f"{height1} is greater than {height2}")
    elif height1 < height2:
        print(f"{height1} is less than {height2}")
    else:
        print("These people have the same height:", height2)

get_max_height()

