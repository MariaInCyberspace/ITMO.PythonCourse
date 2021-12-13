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

# TypeError: can only concatenate str (not "int") to str
# will_give_an_error = string1 + first_number
# Typecast in order to concatenate this number to the string
will_not_give_an_error = string1 + str(first_number)
print(will_not_give_an_error)



