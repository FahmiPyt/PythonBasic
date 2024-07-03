#Python Function QT
#1] Write a Python function that accepts a string and counts the number of upper and lower case letters.

def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return upper_count, lower_count

input_string = "Hello World! How ARE you?"
upper_count, lower_count = count_upper_lower(input_string)
print(f"Uppercase count: {upper_count}")
print(f"Lowercase count: {lower_count}")

#2] Write a Python function that takes a list and returns a new list with distinct elements from the first list.
#input_list = [1, 2, 2, 3, 4, 4, 5]
#output_list: [1, 2, 3, 4, 5]

def get_unique_elements(input_list):
    output_list = []
    
    [output_list.append(item) for item in input_list if item not in output_list]
    
    return output_list

input_list = [1, 2, 2, 3, 4, 4, 5]
output_list = get_unique_elements(input_list)
print("Input List:", input_list)
print("Output List (Unique Elements):", output_list)

#3] Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True  

    if number % 2 == 0 or number % 3 == 0:
        return False  

    i = 7
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

num = 21  
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

#4] Write a Python function that takes a list of numbers and prints the even numbers from the list.

def print_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers in the list:")
print_even_numbers(num_list)

#5] Write a Python function that checks whether a passed string is a palindrome or not.

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]

input_string = "A man a plan a canal Panama"
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")

#6] Write a Python function that takes a string containing Python code and executes it.

def execute_python_code(code_str):
    try:
        exec(code_str)
    except Exception as e:
        print(f"Error executing Python code: {e}")

python_code = """
def greet(name):
    print(f"Hello, {name}!")

greet('Alice')
"""
execute_python_code(python_code)


#7] Write a Python function that takes a list and two indices, and swaps the elements at those indices.

def swap_elements(lst, idx1, idx2):
    if 0 <= idx1 < len(lst) and 0 <= idx2 < len(lst):
        lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
    else:
        print("Error: Index out of bounds")

my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

swap_elements(my_list, 1, 3)
print("List after swapping indices 1 and 3:", my_list)

swap_elements(my_list, 0, 4)
print("List after swapping indices 0 and 4:", my_list)

swap_elements(my_list, 5, 2)

#8] Write a Python function that calculates the length of a given list

def calculate_list_length(lst):
    return len(lst)

my_list = [1, 2, 3, 4, 5]
length = calculate_list_length(my_list)
print(f"The length of the list {my_list} is: {length}")

#9] Write a Python function that takes two numbers as parameters and returns the maximum of the two.

def find_maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

a = 15
b = 8
max_num = find_maximum(a, b)
print(f"The maximum between {a} and {b} is: {max_num}")

#10] Write a Python function that takes two numbers as parameters and returns the minimum of the two.
def find_minimum(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

a = 15
b = 8
min_num = find_minimum(a, b)
print(f"The minimum between {a} and {b} is: {min_num}")

#11] Write a Python function that takes a string as input, splits the string into words, reverses the order of words, 
#and returns the reversed string.

def reverse_words(input_string):
    words = input_string.split()

    reversed_words = words[::-1]

    reversed_string = ' '.join(reversed_words)

    return reversed_string

input_str = "Hello world, how are you?"
reversed_str = reverse_words(input_str)
print("Original string:", input_str)
print("Reversed string:", reversed_str)
