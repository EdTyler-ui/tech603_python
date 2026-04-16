import sys

# check for arguments
if len(sys.argv) > 1:
    print("You gave me an argument!")
    print(type(sys.argv[1]))
    print(sys.argv[0])
else:
    print("You gave me no argument.")