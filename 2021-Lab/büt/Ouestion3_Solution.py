def myfunc():
    word1 = input("Birinci kelimeyi girin: ").lower()
    word2 = input("ikinci kelimeyi girin: ").lower()
    word1 = word1.lstrip(" ")
    word2 = word2.lstrip(" ")
    word1 = word1.rstrip(" ")
    word2 = word2.rstrip(" ")
    set1 = set()
    set2 = set()
    length = len(word1)
    for char1 in word1 :
        set1.add(char1)
    for char2 in word2 :
        set2.add(char2)
    if set1 == set2 :
        num = len(word1)
        for i in range (length):
            if word1[i] == word2[i]:
                num -= 1
        print("True",num)
    else :
        print("False")

myfunc()

