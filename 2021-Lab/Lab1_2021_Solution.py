while True : 
    a = input("Please type an integer greater than or equal to 0: ")
    if a.isdecimal() == False :
        print("Please type an valid integer ")
        continue
    else :
        sayı = 1
        for i in range(1,int(a)+1):
            sayı *= i 
        print("The factorial is",sayı)
        break
