# Exercise 1
### WORKING WITH STRINGS ###

# Declaration and initialization of two strings to work with below

string1 = "this is a string."
string2 = " this is another string."

# Concatenate those strings
concatenated_strings = string1 + string2
print("\nBoth strings combined: \"", concatenated_strings, "\"")

# Get length of the strings
print("\nHere's the length of the first string:", len(string1),
      "\nLength of the second string:", len(string2),
      "\nLength of both strings combined:", len(concatenated_strings))
print()

### MANIPULATE STRINGS ###

# Make first character in a string uppercase
print("\nHere are the strings with first character in each substring uppercase:\n\t", string1.title(),
      "\n\t", string2.title(),
      "\n\t", concatenated_strings.title())

# Make strings uppercase
print("\nHere's the first string in uppercase:", string1.upper(),
      "\nSecond string in uppercase:", string2.upper(),
      "\nBoth strings combined in uppercase:", concatenated_strings.upper())

# Make strings lowercase
print("\nHere are the strings in lowercase:\n\t", string1.lower(),
      "\n\t", string2.lower(),
      "\n\t", concatenated_strings.lower())

# Remove spaces at the end of the string
test_string = "remove a space here "
print("\nRemoving space at the end of the string:",
      "\n\tnot removed:", "\"" + test_string + "\"",
      "\n\tremoved:", "\"" + test_string.rstrip() + "\"")

# Remove spaces at the beginning of the string
print("\nRemoving space at the beginning of the string:",
      "\n\tnot removed:", "\"" + string2 + "\"",
      "\n\tremoved:", "\"" + string2.lstrip() + "\"")

# Remove specified symbols in the string from both ends
test_string = "0remove zeros0"
print("\nRemoving specified symbols in the string from both ends:",
      "\n\tnot removed:", "\"" + test_string + "\"",
      "\n\tremoved:", "\"" + test_string.strip('0') + "\"")

### SUBSTRINGS ###

test_string = "Dissect me"
print("\nTake a substring of this string:", "\"" + test_string + "\"",
      "\n\tThird symbol from the right is", "\"" + test_string[-2] + "\"",
      "\n\tSubstring between third character from the left and "
      "third character from the right:", "\"" + test_string[3:-3] + "\"",
      "\n\tSubstring from the second symbol:", "\"" + test_string[1:] + "\"",
      "\n\tSubstring from the top up to the sixth symbol:", "\"" + test_string[:6] + "\"",
      "\n\tAll characters:", "\"" + test_string[:] + "\"")

# Strings are immutable
# TypeError: 'str' object does not support item assignment
# test_string[3] = "i"


### WORKING WITH NUMBERS ###
first_number = 5
second_number = 2

print(f"{first_number} divided by {second_number} is {first_number / second_number}")
print(f"{first_number} multiplied by {second_number} is {first_number * second_number}")
print(f"{first_number} raised to the power of {second_number} is {first_number ** second_number}")
print(f"The remainder of {first_number} divided by {second_number} is {first_number % second_number}")
print()
# TypeError: can only concatenate str (not "int") to str
# will_give_an_error = string1 + first_number
# Typecast in order to concatenate this number to the string
will_not_give_an_error = string1 + str(first_number)
print(will_not_give_an_error)
print()

### ASKING FOR INPUT ###
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print("{:s} + {:s} = {:5.0f}".format(n1, n2, n3))

### STRING FORMATTING ###
a = 1 / 3
print("{:7.3f}".format(a))

a = 2 / 3
b = 2 / 9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))
print()

### LISTS ###
list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
print(dir(list1))

help(list1.insert)
# insert(index, object, /) method of builtins.list instance
#     Insert object before index.
help(list1.append)
# append(object, /) method of builtins.list instance
#     Append object to the end of the list.
help(list1.sort)
# sort(*, key=None, reverse=False) method of builtins.list instance
#     Sort the list in ascending order and return None.
help(list1.remove)
# remove(value, /) method of builtins.list instance
#     Remove first occurrence of value.

# Change values in the list accessing it via index
import random

for i in range(0, len(list1)):
    list1[i] = random.randint(0, 100)
print(list1)

# Append a random value to the list
value = random.randint(0, 100)
list1.append(value)
if list1.__contains__(value):
    list1.remove(value)
    print(f"{value} removed from the list")

# Remove the last value in the list
remove_me = list1[len(list1) - 1]
print("Last value in the list:", remove_me)
print("Before:", list1)
list1.remove(remove_me)
print("After:", list1)

# Sorting the list
sorted_list = sorted(list1, reverse=True)
print("Unsorted list:", list1)
print("Sorted list:", sorted_list)

new_list = []
for i in range(0, 10):
    new_list.append(random.randint(0, 100))

print("New list unsorted:", new_list)
new_list.sort(reverse=True)
print("New list sorted in reverse order:", new_list)
