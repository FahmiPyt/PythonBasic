#Question 1: Create an empty dictionary.
l1=[]
print(type(l1))

#Question 2: Create a dictionary with key-value pairs for a person's name and age.
D1={'name':'Fahmi', 'Age':24}

#Question 3: Access the value associated with the key "age" in the person dictionary.
print(D1.get('Age'))

#Question 4: Check if a key exists in the person dictionary.
print(D1.keys())

#Question 5: Add a new key-value pair "city" with the value "New York" to the person dictionary.
D1['City']='New York'
print (D1)

#Question 6: Remove the key-value pair with the key "age" from the person dictionary.
D1.pop('Age')
print(D1)

#Question 7: Iterate through the keys in the person dictionary.
for keys in D1.keys():
	print(keys)

#Question 8: Iterate through the values in the person dictionary.
for values in D1.values():
	print(values)

#Question 9: Iterate through both keys and values in the person dictionary.
for keys, values in D1.items():
	print(D1)

#Question 10: Create a dictionary with default values using the dict.fromkeys() method.
default_dict = dict.fromkeys(['key1', 'key2', 'key3'], 'default_value')

print(default_dict)

#Question 11: Get the value associated with a key using the dict.get() method with a default value.
Dict1={'k1': 10, 'k2': 20, 'k3': 30}
value=Dict1.get('k3',0)
print(value)

#Question 12: Count the number of occurrences of each character in a string using a dictionary.
I1 = "Excellance"

char_count = {}

for char in I1:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print the character counts
for char, count in char_count.items():
    print(f"'{char}' occurs {count} times")

#Question 13: Merge two dictionaries.
dict3 = {'a': 1, 'b': 2}
dict4 = {'b': 3, 'c': 4}

dict3.update(dict4)
print(dict3)

#another way

dict5 = {'a': 5, 'b': 7}
dict6 = {'b': 6, 'c': 7}

merged_dict = {**dict5, **dict6}
print(merged_dict)

#Question 14: Create a dictionary where the values are squares of the keys.
dict7 = {x: x**2 for x in range(1, 11)}
print(dict7)

#Question 15: Find the key with the maximum value in a dictionary.
dict8 = {'a': 10, 'b': 20, 'c': 30, 'd': 15}

max_key = max(dict8, key=dict8.get)

print(max_key)


#Question 16: Sort a dictionary by its keys.
my_dict = {'b': 2, 'a': 1, 'd': 4, 'c': 3}

sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)

#Question 17: Check if two dictionaries are equal.
# Two dictionaries to compare
dict11 = {'a': 1, 'b': 2, 'c': 3}
dict12 = {'a': 1, 'b': 2, 'c': 3}
dict13 = {'a': 1, 'b': 3, 'c': 5}


if dict11 == dict12:
    print("Dictionaries are equal")
else:
    print("Dictionaries are not equal")

if dict11 == dict13:
    print("Dictionaries are equal")
else:
    print("Dictionaries are not equal")

#Question 18: Remove all elements from a dictionary.
dict14 = {'a': 1, 'b': 2, 'c': 3}

# Remove all elements from the dictionary
dict14.clear()

# Print the empty dictionary
print(dict14)

#Question 19: Create a nested dictionary.
nested_dict = {
    'outer_key1': {
        'inner_key1': 'value1',
        'inner_key2': 'value2'
    },
    'outer_key2': {
        'inner_key3': 'value3',
        'inner_key4': 'value4'
    }
}

print(nested_dict)

#Question 20: Get a list of all keys in a dictionary.
dict19 = {'a': 1, 'b': 2, 'c': 3}

keys_list = list(dict19.keys())
print(keys_list)

#Question 21: Get a list of all values in a dictionary.
dict20 = {'a': 1, 'b': 2, 'c': 3}

values_list = list(dict20.values())
print(values_list)

#Question 22: Update values in a dictionary using another dictionary.
dict21 = {'a': 1, 'b': 2, 'c': 3}

dict22 = {'b': 20, 'd': 4}

dict21.update(dict22)
print(dict21)


#Question 23: Remove a key from a dictionary using the pop() method.
dict23 = {'a': 1, 'b': 2, 'c': 3}

dict24 = dict23.pop('b')
print(dict23)


#Question 24: Get a list of tuples containing key-value pairs from a dictionary.
dict25 = {'a': 1, 'b': 2, 'c': 3}

tuple_list = list(dict25.items())
print(tuple_list)


#Question 25: Convert a list of tuples into a dictionary.
tuple_list = [('a', 1), ('b', 2), ('c', 3)]

dict26 = dict(tuple_list)

# Print the dictionary
print(dict26)

