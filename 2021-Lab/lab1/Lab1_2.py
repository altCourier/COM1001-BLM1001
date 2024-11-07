# Take in a year value from the user. 
# Print out the related animal to the input year.

myDict = {
    2000 : "Dragon",
    2001 : "Snake",
    2002 : "Horse",
    2003 : "Sheep",
    2004 : "Monkey",
    2005 : "Rooster",
    2006 : "Dog",
    2007 : "Pig",
    2008 : "Mouse",
    2009 : "Ox",
    2010 : "Tiger",
    2011 : "Bunny"
}

while True:
    try:
        yearInput = int(input("Please enter a year between 2000-2011\n"))
        if yearInput < 2000 or yearInput > 2011:
            raise ValueError ("Please enter a valid year!")
        else:
            print("Your animal is: ", myDict[yearInput])
            break
    except ValueError as Error:
        print(Error)

