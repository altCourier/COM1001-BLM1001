gamer1=input()
gamer2=input()
number1=input().split(",")
number2=input().split(",")
def game(gamer1,number2):
    alphabet=list(map(chr,range(ord("A"),ord("Z")+1)))
    number=[int(i) for i in number2]
    gamer1=list(gamer1)
    gamer=[_ for _ in gamer1]
    for i in range(10):
        x=number[i]+2
        if x>26:
            x=x-26
        a=gamer1[x]
        gamer.remove(a)
    return gamer

def puanlama(gamer1,gamer2):
    liste=[0,0]
    for i in range(len(gamer1)):
        x=ord(gamer1[i])-ord(gamer2[i])
        if x>0:
            liste[0]+=x
        else:
            liste[1]+=abs(x)
    return liste

gamer1=game(gamer1,number2)
gamer2=game(gamer2,number1)
print(puanlama(gamer1,gamer2))