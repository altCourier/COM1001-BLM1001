def myfunc(sm,big,all):
    bigs = big*5 
    smalls = sm*2
    if bigs + smalls == all :
        print(f"{sm} tane küçük çikolata gerekli")
    elif bigs + smalls < all :
        print("-1, yeterli çikolata yok")
    else :
        while True :
            smalls -= 2
            needed = sm-1 
            if smalls + bigs == all :
                print(f"{needed} tane küçük çikolata {all} gram çikolata üretmek için yeterli olur")
                break


myfunc(4,1,13)
myfunc(4,1,14) 
myfunc(2,1,7)
