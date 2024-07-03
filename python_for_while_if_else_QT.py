#qt] Print numbers from 1 to 10 using a for loop
for i in range(1, 11):
    print(i)

#qt] Calculate the sum of numbers from 1 to 10 using a for loop

total_sum=0
for i in range(1, 11):
    total_sum += i
print(total_sum)


#qt] Print the elements of a list using a for loop
list1 = [1, 2, 3, 4, 5]

for item in list1:
    print(item)


#qt] Calculate the product of elements in a list using a for loop
list2 = [1, 2, 3, 4, 5]

product = 1

for item in list2:
    product *= item

print(product)


#qt] Print even numbers from 1 to 10 using a for loop
for num in range(1, 11):
    if num % 2 == 0:
        print(num)


#qt] Print numbers in reverse from 10 to 1 using a for loop
for num1 in range(10, 0, -1):
    print(num1)

#qt] Print numbers in reverse from 10 to 1 using a for loop
for num1 in range(10, 0, -1):
    print(num1)

#qt] Print characters of a string using a for loop
str1="Python"
for char in str1:
    print(char)

#qt]Find the largest number in a list using a for loop
# Define a list
list3 = [10, 5, 20, 8, 15]

largest_number = list3[0]

for num in list3:
    if num > largest_number:
        largest_number = num
print(largest_number)


#qt] Find the average of numbers in a list using a for loop 
# Define a list of numbers
list4 = [10, 20, 30, 40, 50]

total_sum = 0
count = 0

for num in list4:
    total_sum += num  
    count += 1        

average = total_sum / count

print(average)

#qt] Print all uppercase letters in a string using a for loop
str2 = "Hello World"

for char in str2:
    if char.isupper():
        print(char)


#qt] Count the number of vowels in a string using a for loop
str3 = "Hello World"

vowel_count = 0

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

for char in str3:
    # Check if the character is a vowel
    if char in vowels:
        vowel_count += 1

print(vowel_count)


#qt] Print a pattern of stars using nested for loops
num_rows = 10

for i in range(num_rows):
    for j in range(i + 1):
        print("*", end=" ")
    print()  

#qt] Calculate factorial of a number using a while loop
num1 = 5

factorial = 1

if num1 < 0:
    print("Factorial is not defined for negative numbers.")
elif num1 == 0:
    print("The factorial of 0 is 1.")
else:
    while num1 > 0:
        factorial *= num1
        num1 -= 1

    print("The factorial of", num1, "is", factorial)


#qt] Calculate the sum of numbers from 1 to 100 using a while loop
total_sum1=0
for i in range(1, 101):
    total_sum1 += i
print(total_sum1)

#qt] Find all prime numbers between 1 and 50 using nested for and if
for num in range(1, 51):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


#qt] Print numbers divisible by 3 or 5 from 1 to 20 using a for loop
for num in range(1, 21):
    if num % 3 == 0 or num % 5 == 0:
        print(num)




#qt] Find the common elements in two lists using a for loop
list5 = [1, 2, 3, 4, 5]
list6 = [3, 4, 5, 6, 7]

common_elements = []

for element in list5:
    if element in list6:
        common_elements.append(element)

print(common_elements)

#qt] Print numbers from 1 to 5, except 3 using a for loop and continue statement
for num in range(1, 6):
    if num == 3:
        continue
    print(num)


#qt] Print numbers from 1 to 10. If a number is divisible by 4, stop the loop using a for loop and break statement
for num in range(1, 11):
    if num % 4 == 0:
        break
    print(num)

#qt] Print numbers from 1 to 10. If a number is even, skip it using a for loop and else clause
for num in range(1, 11):
    if num % 2 == 0:
        continue  
    print(num)
else:
    print("Loop completed successfully.")


#qt] Print numbers from 1 to 10. If a number is even, break the loop using a for loop and else clause
for num in range(1, 11):
    if num % 2 == 0:
        break  
    print(num)
else:
    print("Loop completed successfully.")

#qt] Print the Fibonacci sequence up to the 10th term using a while loop

#qt] Print numbers in a list until a negative number is encountered using a while loop
