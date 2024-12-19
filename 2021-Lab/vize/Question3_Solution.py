import math
while True :
    try :
        exit = input("TYPE '-1' TO QUIT, TYPE '0' TO CONTINUE: ")
        exit.lstrip(" ")
        exit.rstrip(" ")
        if exit == "-1":
            break
        elif exit != "-1" and exit != "0":
            print("PLEASE TYPE INVALID COMMAND TO CONTINUE OR TO QUIT: ")
            continue
    except Exception:
        print("PLEASE TYPE INVALID COMMAND TO CONTINUE OR TO QUIT: ")
        continue
    while True :
        try :
            wayx = input("CHOOSE THE DIRECTION ; RIGHT, LEFT: ")
            wayy = input("CHOOSE THE DIRECTION ; UP, DOWN: ")
            wayx.lstrip(" ")
            wayx.rstrip(" ")
            wayy.lstrip(" ")
            wayy.rstrip(" ")
            if wayx.lower() != "right" and wayx.lower() != "left" :
                print("PLEASE TYPE INVALID DIRECTIONS")
                continue
            if wayy.lower() != "up" and wayy.lower() != "down" :
                print("PLEASE TYPE INVALID DIRECTIONS")
                continue
        except Exception:
            print("PLEASE TYPE INVALID DIRECTIONS")
            continue
        break 
    while True :
        try :
            numx = int(input("HOW MANY STEP DO YOU WANT TO GO IN X-AXIS(IF NONE,TYPE ZERO): "))
            numy = int(input("HOW MANY STEP DO YOU WANT TO GO IN Y-AXIS(IF NONE,TYPE ZERO): "))
            if numx < 0 or numy < 0 :
                print("PLEASE TYPE THE STEP NUMBERS GREATER THAN ZERO")
                continue
        except Exception:
            print("PLEASE TYPE INVALID STEP NUMBERS")
            continue
        break

    x = 0
    y = 0
    if wayx.lower() == "right":
        x += numx
    else :
        x -= numx
    if wayy.lower() == "up":
        y += numy
    else :
        y -= numy
    distance = math.sqrt((x**2)+(y**2))
    print(f"THE DISTANCE TO THE ORIGIN IS {distance}")

   


    


    
    
    

    

