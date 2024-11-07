number = int(input())

for i in range(0,number+1):
    print(" "*i, end="")
    print("*"*abs(number-i), end="")
    print()

# SOLUTION W NESTED LOOP STRUCTURE

for i in range(number):
    for j in range(i):
        print(" ", end="")
    
    for k in range(number-i):
        print("*", end="")

    print()

