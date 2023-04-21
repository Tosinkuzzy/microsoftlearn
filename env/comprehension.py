# Create a list from a range
# Applying for-loop inside the list
my_list = [i for i in range(10)]
my_list

# Creating a list comprehension
# Applying a traditional way would have an outside for-loop
my_list = []
for i in range(10):
    my_list.append(i)
    my_list 

# Create a list from a list using comprehension
another_list = [i*i for i in my_list]
another_list

# Traditional way
another_list
for i in my_list:
    another_list.append(i*i)
    another_list

# List Comprehension with if-statement
even_list = [i for i in my_list if i % 2 == 0]
even_list

# List comprehension with else-statement
even_list = [i if i % 2 == 0 else -i*i for i in my_list]
even_list

# Dictionary comprehension
{i: i*i for i in my_list}

