# Get a number from the user that decides:
# How many inputs there will be.
# Given inputs are calculated.

def amountTaker():
    while True:
        try:
            amount = int(input("Enter the amount of inputs. "))
            return amount
        except ValueError:
            print("Enter a valid number. ")

def calculator(inputAmount,total_inputs, currentInput = 1):
    if inputAmount <= 0:
        return 0
    
    try:
        value = float(input(f"Enter input {currentInput} of {total_inputs}: "))
        return value + calculator(inputAmount-1, total_inputs, currentInput + 1)
    except:
        print("Enter a valid number. ")
        return calculator(inputAmount)
    

def  main():
    amount = amountTaker()
    total = calculator(amount,amount)
    print(f"Your total is: {total}")

main()
