# Using Dictionaries as Records
my_dict = {
    'Key 1': 'Value 1',
    'Key 2': ' Value 2'
}
car = {
    "Brand": "Tesla",
    "Model": "Elon",
    "Year": "2023"
}

#Using Dictionaries as Counters
items = ['Willow', 'Oyinda', 'Tosinkuzzy', 'Family', 'Games',]
count = {'Willow': 4, 'latifah': 3, 'Tosinkuzzy': 2, 'Family': 1}
for items in items:
    count[items] = count.get(items, 0) + 1
# Adding a new key and value to my Dictionaries
    my_dict['Key 3'] = 'Value 3'

# Iterating Over a Dictionary
for Tosinkuzzy, Value in count.items():
    print(Tosinkuzzy, Value)
