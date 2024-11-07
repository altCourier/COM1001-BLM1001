# Take in a value from the user to determine how many inputs will be given.
# Decide the min. value amongst all. 
# Decide the max. value amongst all. 

def InputValueTaker():
    try:
        amount = int(input("Enter the input amount:\n"))
        if amount <= 0:
            raise ValueError
        else:
            return amount
    except:
        print("Please enter an integer.")
        return InputValueTaker()
    
def valueTaker():
    myList = []
    amount = InputValueTaker()
    for _ in range(1,amount+1):
        while True:
            try:
                value = float(input(f"Please enter {_} of {amount}:\n"))
                myList.append(value)
                break
            except ValueError:
                print("Please enter a valid numeric value. ")
    return myList
            
def main():
    wantedList = valueTaker()
    print(f"Your smallest value is {min(wantedList)}")

    max_value = wantedList[0]
    for number in wantedList[1:]:
        if number > max_value:
            max_value = number

    print(f"Maximum value is {max_value}")
        
main()
