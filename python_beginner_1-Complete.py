#qt 1] print your name in python
print('Farhan')

#qt 2] Calculate the multiplication and sum,division, of two numbers
print(10*20)
print(10+20)
print(20-10)
print(50/5)

a=50
b=10

print(a*b)
print(a+b)
print(a-b)
print(a/b)

#qt 3] Print characters from a string that are present at an even index number
#       str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

str = "pynative"
for i in range(0, len(str), 2):
    print(str[i])


#qt 4] Write a program to find how many times substring "Emma" appears in the given string.
#     str_x = "Emma is good developer. Emma is a writer"

str_x = "Emma is good developer. Emma is a writer"
count = str_x.count("Emma")
print("Number of times 'Emma' appears in the given string:", count)


#qt 5] Create a  list take any example
list1 = [1, 2, 3, 4, 5]
print(list1)


#qt 6] ex=[7,5,3,6] reverse list o/p=[6,3,5,7]
ex = [7, 5, 3, 6]
list2 = ex[::-1]

print(list2)


#qt 7] l=[1,2,'a','b',7,9] find length of list 
l = [1, 2, 'a', 'b', 7, 9]

list3 = len(l)
print("Length of the list:", list3)


#qt 8] l=[1,2,'a','b',7,9] remove 'a'
l1 = [1, 2, 'a', 'b', 7, 9]

l1.remove('a')
print(l1)


#qt 9] l=[1,2,100,300,'abc',90]  add 100

l2=[1,2,100,300,'abc',90]
l2.append(100)
print(l2)

#qt 10] Reverse words in given string 
#                  str="python" 
#                 output ="nohtyp"
str1="python"
str2=str1[::-1]
print(str2)

#qt 11] find length of string     
#             str="python language"

str3="python language"
length=len(str3)
print(length)

#qt 12] find size of tuple 
#             tp=('a','b','c','d','k')

tp = ('a', 'b', 'c', 'd', 'k')
size=len(tp)
print(size)

#qt 13]  d={'name':'john','age':21,'city':'London'} find only keys  and find values of Dictionary 

d={'name':'john','age':21,'city':'London'}
keys=d.keys()
values=d.values()

print(keys)
print(values)


#qt 14] d={'name':'john','age':21,'city':'London'} 
#            output= 'john'
output=d['name']
print(output)

#qt 15] create empty Dictionaries and add two keys with values pairs
#             output= {'a':1,'b':3}
dict1={}
dict1['a']=1
dict1["b"]=3
print(dict1)

#qt 16] find length of Dictionary 
#                ex 
#                 thisdict = {
#                    "brand": "Ford",
#                    "electric": False,
#                    "year": 1964,
#                    }

thisdict = {
                    "brand": "Ford",
                    "electric": False,
                    "year": 1964,
                    }
length1=len(thisdict)
print(length1)

#qt 17] Removing Items from Dictionary
#   ex  
#                thisdict = {
#                     "brand": "Ford",
#                     "model": "Mustang",
#                     "year": 1964
#                   }

thisdict1= {
                     "brand": "Ford",
                     "model": "Mustang",
                     "year": 1964
                   }
del thisdict1['model']
print(thisdict1)

#qt 18] compare two values using Comparison operators,Logical operators,Identity operators ?
#            x=80
#            y=40

# Comparison Operators
x = 80
y = 40

print("\nComparison Operators:")
print(x > y)
print(x < y)
print(x == y)
print(x >= y)
print(x <= y)

# Logical Operators
print("\nLogical Operators:")
print(x > 50 and y > 50)
print(x > 50 or y > 50)
print(not(x > 50))

# Identity Operators
print("\nIdentity Operators:")
print(x is y)
print(x is not y)


#qt 19] how to comments work in python use single line comment,Multiline Comments comments
# Single can be commented by #
# Multiline can be commented be '''before the comment and '''after the comment.

#qt 20] take any example check its type, example should be(use list,numbers,float,string,bool,NoneType
#           dict,set,tuple)

list_example = [1, 2, 3, 4, 5]
print(type(list_example))

int_example = 10
print(type(int_example))

float_example = 3.14
print(type(float_example))

str_example = 'Hello, World!'
print(type(str_example))

bool_example = True
print(type(bool_example))

none_example = None
print(type(none_example))

dict_example = {'a': 1, 'b': 2}
print(type(dict_example))

set_example = {1, 2, 3, 4, 5}
print(type(set_example))

tuple_example = (1, 2, 3, 4, 5)
print(type(tuple_example))



#qt 21] li=[4,5,6,7,8,9,10,11,12,13] use slicing 
#                 o/p=[4, 6, 8, 10, 12]
li21=[4,5,6,7,8,9,10,11,12,13]
output21=li21[::2]
print(output21)

#qt 22 ] li=[4,5,6,7,8,9,10,11,12,13] use slicing
#                o/p=[5, 7, 9, 11, 13]
li22=[4,5,6,7,8,9,10,11,12,13]
output22=li22[1::2]
print(output22)

#qt 23] str= "Python Tutorial" convert str into list
#                o/p=['python','Tuorial']

str23= "Python Tutorial"
print(str23.split())






 

