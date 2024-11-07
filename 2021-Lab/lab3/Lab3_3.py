# Find all pythagorean triples 
# that are individually smaller than 500
# and print how many there are, what they are.
# Take in a interval from the user.

def intervalTaker():
    try:
        firstNum, secondNum = int(input("Enter the first.")), int(input("Enter the second."))
        if firstNum < 0 or secondNum < 0:
            raise ValueError
        else:
            return firstNum, secondNum
    except ValueError:
        print("Please enter valid numbers.")
        intervalTaker()

def main():
    firstInt, secondInt = intervalTaker()
    count = 0
    triples = []
    for a in range(firstInt, secondInt):
        for b in range(a, secondInt):
            c = (a**2 + b**2) ** 0.5
            if isinstance(c,int) and c < 500:
                triples.append((a,b,int(c)))
                count += 1
    
    for triple in triples:
        print(triple)

    print(count)

main()

