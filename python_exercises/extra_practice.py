
# print(number + " " + "is a great number")

# ask user for number, say if even or odd and positive or negative

# num = int(input("Enter a number: "))
# if num % 2 == 0 and num > 0:
#     print("positive even number")
# elif num % 2 == 0 and num < 0:
#     print("negative even number")
# elif num % 2 != 0 and num > 0:
#     print("positive odd number")
# else:
#     print("negative odd number")

# enter numbers continuously until -1 chosen, add up all numbers entered
# count = 0
# while True:
#     number = int(input("Enter a number: "))
#     if number == -1:
#         break
#     count += number
# print("total:", count)

# ask user for number, print numbers 1, n that are divisble by 3 and 5

# number = int(input("Enter a number: "))
#
# for i in range(1, number):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

# function takes number and returns sum of digits
# def sum_of_digits(n):
#     sum = 0
#     for digit in str(n):
#         sum += int(digit)
#     return sum
# print(sum_of_digits(34))

# function that takes a list of numbers and returns largest number
# def find_max(lst):
#     largest = lst[0]
#
#     for num in lst:
#         if num > largest:
#             largest = num
#
#     return largestdef

# function that takes string and returns number of vowels

# def count_vowels(s):
#     count = 0
#     vowels = "aeiou"
#
#     for char in s.lower():
#         if char in vowels:
#             count += 1
#
#     return count
#
# count_vowels('hello')

# shopping_list = ['eggs', 'bread', 'bananas', 'biscuits', 'milk']
# print(shopping_list)
# print(type(shopping_list))
# print(shopping_list[0])
# print(shopping_list[-1])
# shopping_list[1] = 'rice'
# print(shopping_list[1])
# shopping_list.append('carrots')
# print(len(shopping_list))
#
# print(shopping_list[::-1])

# dictionaries
# counts how many time one thing appears in dictionary
data = ["apple", "banana", "apple", "orange", "banana", "apple"]

count_fruit = {}
for fruit in data:
    if fruit in data:
        count_fruit[fruit]= count_fruit.get(fruit, 0) + 1
print(count_fruit)

person = {"name": "Alice", "age": 25}
print(person.keys())
print(person.values())
print(person.items())