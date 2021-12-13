# Exercise 1
from turtle import title


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


# Manipulate strings

# Make first character in string uppercase

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
      "\n\tnot removed:", test_string,
      "\n\tremoved:", test_string.rstrip())
