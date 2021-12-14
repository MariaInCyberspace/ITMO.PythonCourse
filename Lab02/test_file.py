# Isolated work on dictionaries
# Nested data

record = {
    'name': {'first_name': 'Sylvia', 'last_name': 'Stern'},
    'job': ['dev', 'mgr'],
    'age': 34
}

print(f"\nFull name: \"{record['name'].get('first_name')} {record['name'].get('last_name')}\""
      f"\nJob: {record['job'][0]}, {record['job'][1]}"
      f"\nAge: {record['age']}")
record['job'].append('Janitor')


print('\nFull name: "{0[name][first_name]} {0[name][last_name]}"'.format(record),
      '\nJob: {0[0]}, {0[1]}'.format(record['job']),
      f"\nAge: {record['age']}")

record['job'].append('Janitor')
print(record['job'])
