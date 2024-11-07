# Get an input value.
# Calculate the factorial of it.
# Despite other Lab 2 questions, this one is really nice.
# We could solve it by doing a recursive function which will help us with:
# Sequences like fibonacci sequence etc.
# Or what was intended: nestedloops.

def factorial(number):
    while number != 1:
        return factorial(number)*factorial(number-1)
        

def main():
    try:
        myNumber = int(input("Please enter your number."))
        if myNumber < 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid number.")

        if myNumber == 1 or 0:
            return "1"

        else:
            print(factorial(myNumber))

main()