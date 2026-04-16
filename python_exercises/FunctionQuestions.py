# print("\nQ1a\n")
#
# # Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
#
# # e.g. f(12) = [1, 2, 3, 4, 6, 12]
#
# # hint: range(1, n) returns a collection of the numbers from 1 to n-1
#
#
# # A1a:
# def divisors(num):
#     divisors = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             divisors.append(i)
#     return divisors
#
# print(divisors(18))
#
# print("\nQ1b\n")
#
# # Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
#
# # is a factor of the other, false otherwise
#
# # (bonus points if you call your previous function within this function
#
#
# # A1b:
# def xy_divisors(x, y):
#     if x % y == 0 or y % x == 0:
#         return True
#     else:
#         return False
#
# print(xy_divisors(18,2))
#
# # -------------------------------------------------------------------------------------- #
#
#
# print("\nQ2a\n")
#
# # Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
#
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
#
#
# # A2a:
# def alpha_index(letter):
#     if letter in alphabet:
#         return int(alphabet.index(letter)) + 1
# print(alpha_index("f"))
#
# print("\nQ2b\n")
#
# # Q2b: create a function which takes a persons name as an input string and returns an
#
# # ID number consisting of the positions of each letter in the name
#
# # e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14
#
#
# # A2b:
# def ID_name(name):
#     ID = ''
#     for char in name:
#         ID += str(alphabet.index(char.lower()))
#     return ID
#
# print(ID_name("Bob"))
#
#
#
# print("\nQ2c\n")
#
# # Q2c: Create a function which turns this ID into a password. The function should subtract
#
# # the sum of the numbers in the id that was generated from the whole number of the id.
#
# # e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)
# def password(name):
#     ID = int(ID_name(name))
#     whole_ID = 0
#     for i in str(ID):
#        whole_ID += int(i)
#     return ID - whole_ID
#
# print(password("Bob"))
# # A2c:
#
#
# # -------------------------------------------------------------------------------------- #
#
#
# print("\nQ3a\n")

# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.


# A3a:
# def is_prime(n):
#
#     if type(n) != int:
#         return "Not a number"
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, n):
#         if n % i == 0:
#             return False
#     return True
#
# print(is_prime(5))
# print("\nQ3b\n")

# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit


# A3b:
print(36**0.5)

# -------------------------------------------------------------------------------------- #