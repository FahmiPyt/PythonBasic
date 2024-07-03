#COMPREHENSION #QT
#QT 1] How can you find all the even numbers in a given list of integers using Python?
n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in n1:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

#QT 2] How can you find all the odd numbers in a given list of integers using Python?
n2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = []
for num in n2:
    if num % 2 != 0:
        odd_numbers.append(num)
print(odd_numbers)

#QT 3] How can you compress a string in Python by counting consecutive repeated characters and appending the character 
# followed by its count? (e.g., "aaabbc" ->"a3b2c1")
#Option1
def compress_string(s):
    if not s:
        return ""

    compressed = []
    count = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            compressed.append(s[i] + str(count))
            count = 1
    
    # Append the last character and its count
    compressed.append(s[-1] + str(count))

    return ''.join(compressed)

# Example usage:
original_string = "aaabbc"
compressed_string = compress_string(original_string)
print(f"Original string: {original_string}")
print(f"Compressed string: {compressed_string}")

#Option2
from itertools import groupby

def compress_string(s):
    compressed = []
    for key, group in groupby(s):
        compressed.append(f"{key}{len(list(group))}")
    return ''.join(compressed)

# Example usage:
original_string = "aaabbc"
compressed_string = compress_string(original_string)
print(f"Original string: {original_string}")
print(f"Compressed string: {compressed_string}")

#QT 4] How can you output a string in Python with the first letter capitalized?
s = "hello world"
S = s.capitalize()
print(S)

#QT 5] How can you create a list using list comprehension with a nested for loop in Python?
l = [[i * j for j in range(1, 4)] for i in range(1, 4)]

print(l)

#QT 6] How can you create a list using multiple conditionals in list comprehensions in Python?
n2 = [num for num in range(1, 21) if (num % 2 == 0 or num % 3 == 0) and not (num % 2 == 0 and num % 3 == 0)]
print(n2)


#QT 7] list1 = [1, -12, 34, -4, 25, -16, 19], write a Python program to create a new list list2 that 
#contains the string " +ve " for each positive number and " -ve " for each negative number using list comprehension with if-else
# conditionals. Print the resulting list2.

list1 = [1, -12, 34, -4, 25, -16, 19]
list2 = [" +ve " if num > 0 else " -ve " for num in list1]
print(list2)

#QT 8] string = 'AbcDeFG', write a Python program to create a new list list1 that contains each character of the 
#string converted to uppercase using list comprehension. Print the resulting list1.

string = 'AbcDeFG'
list3 = [char.upper() for char in string]
print(list3)

#QT 9] Create a dictionary using dictionary comprehension Convert the numbers squares to cubes by using dict comprehension

n3 = [1, 2, 3, 4, 5]
n4 = {num**2: num**3 for num in n3}
print(n4)

#QT 10] family_id = {'richerd': 44, 'mary': 7, 'lucy': 40, 'William': 60, 'wick': 10}

family_id = {'richerd': 44, 'mary': 7, 'lucy': 40, 'William': 60, 'wick': 10}

#QT 11]Given a dictionary family_id representing the ages of family members, write a Python program to create a new dictionary 
#voters_id that includes only those family members who are eligible to vote (i.e., age 18 and above). Use dictionary 
#comprehension to achieve this and print the resulting voters_id.

voters_id = {key: value for key, value in family_id.items() if value >= 18}
print(voters_id)

#QT 12] family_id = {'richerd': 44, 'mary': 7, 'lucy': 40, 'William': 60, 'wick': 10} Given a dictionary family_id representing 
#the ages of family members, write a Python program to create a new dictionary voters_id that includes only those family 
#members who are eligible to vote (i.e., age 18 and above) and who are senior citizens (i.e., age 60 and above). 
#Use dictionary comprehension with multiple conditionals to achieve this and print the resulting voters_id.

senior_citizens = {key: value for key, value in family_id.items() if value >= 18 and value >= 60}
print(senior_citizens)

#QT 13] Given a list list = ['java', 'python', 'pandas'], write a Python program to create a dictionary my_dict using dictionary 
#comprehension and enumerate() that maps each element of the list to its corresponding index. Print the resulting my_dict.

list4 = ['java', 'python', 'pandas']
dict1 = {value: index for index, value in enumerate(list4)}
print(dict1)

#QT 14] Given a dictionary my_squares={1:1,2:4,3:9,4:16,5:25} containing squares of numbers, write a Python program to create 
#a new dictionary my_cubes using dictionary comprehension that maps each key-value pair from my_squares to its cube. 
#Print the resulting my_cubes.

sq = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
cu = {key: value**3 for key, value in sq.items()}
print(cu)