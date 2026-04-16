# Q1a: Print only the first 5 numbers in this list

x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
for num in x[:5]:
  print(num)

print("\nQ1b\n")

# Q1b: Now print only the even numbers in this list (the elements that are themselves even)

x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
for num in x:
    if num % 2 == 0:
        print(num)

print("\nQ1c\n")

# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)

x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
for num in x[:5]:
    if num % 2 == 0:
        print(num)

# -------------------------------------------------------------------------------------- #


print("\nQ2a\n")

# Q2a: from the list of names, create another list that consists of only the first letters of each first name

# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]

names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
first_names = []
for name in names:
    first_name = name.split()[0]
    first_names.append(first_name)

print(first_names)

print("\nQ2b\n")

# Q2b: from the list of names, create another list that consists of only the index of the space in the string

# HINT: use your_string.index("substring")

names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
index_space = []
for name in names:
    index = name.index(" ")
    index_space.append(index)

print(index_space)

print("\nQ2c\n")

# Q2c: from the list of names, create another list that consists of the first and last initial of each individual

names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
initials = []
for name in names:
    parts = name.split()
    first = parts[0][0]
    last = parts[1][0]
    initials.append(first + last)

print(initials)

# -------------------------------------------------------------------------------------- #


print("\nQ3a\n")

# Q3a: Here is a list of lists, print only the lists which have no duplicates

# Hint: This can be easily done by using sets as a set does not contain duplicates

list_of_lists = [[1, 5, 7, 3, 44, 4, 1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]



# A3a:
for list in list_of_lists:
    if len(list) == len(set(list)):
        print(list)


# -------------------------------------------------------------------------------------- #


print("\nQ4a\n")

# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,

# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that

# they entered


# A4a:
#while True:
#    num = int(input("Enter a number over 100: "))
#    isprime(num)
#    if num > 100:
#        break
#    else:
#        print("number is not above 100: ")

#print("you entered: ", num)

#print("\nQ4b\n")

# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise
  # [2, 3, 5, 7]

# A4b:
# def isprime(num):
 #   for i in range(1, n):
#        if n % i == 0 and i !=1 and i != n:
#            print("your numer is not prime")
#            return False

#    print("your numer is prime")
#    return True


# ask for number, print if odd or even

#num = int(input("Enter a number: "))
#if num % 2 == 0:
#    print("Number is even")
#else:
#    print("Number is odd")

# ask user for password, only accept 'Python12345'

password = input("Enter a password: ")
if password == "Python12345":
    print('Access confirmed')
else:
    print('Access denied')

