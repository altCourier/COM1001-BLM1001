# Take in 3 inputs that represents sides of a triangle.
# Write a program that decides on whether it is a equilateral, isosceles, scalene

def decider(sideOne, sideTwo, sideThree):
    if sideOne <= 0 or sideTwo <= 0 or sideThree <= 0:
        return "Sides must be greater than zero."
    elif sideOne == sideTwo == sideThree:
        return "Equilateral"
    elif sideOne != sideTwo != sideThree:
        return "Scalene"
    else:
        return "Isosceles"
    
def main():
    print("Please enter the sides of your triangle.")
    try:
        side_one = int(input("1:\n"))
        side_two = int(input("2:\n"))
        side_three = int(input("3:\n"))
        result = decider(side_one, side_two, side_three)
        print(f"The triangle is: {result}")
    except ValueError:
        print("Please enter valid integers for the sides.")

main()