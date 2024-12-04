def fibonacci():
    while True : 
        num1 = input("Birinci tam sayıyı girin: ")
        num2 = input("İkinci tam sayıyı girin: ")
        if num1.isdecimal() == False and num2.isdecimal() == True :
            print("Lütfen 1.sayı için geçerli bir tam sayı girin")
            continue
        elif num2.isdecimal() == False and num1.isdecimal() == True :
            print("Lütfen 2.sayı için geçerli bir tam sayı girin")
            continue
        elif num2.isdecimal() == False and num1.isdecimal() == False :
            print("Lütfen 1. ve 2.sayılar için geçerli bir sayı girin")
        else :
            while True :
                uzunluk = input("Dizinizin kaç elemandan oluşacağını yazın(2'den büyük pozitif bir tam sayı girin): ")
                if uzunluk.isdecimal() == False or int(uzunluk) == 0 or int(uzunluk) <= 2  :
                    print("Geçerli bir liste uzunluğu girin")
                    continue
                else :
                    break
            uzunluk_ = int(uzunluk)
            num1_ = int(num1)
            num2_ = int(num2)
            liste = [num1_,num2_]
            for i in range(0,uzunluk_-2):
                liste.append((liste[i]+liste[i+1]))
            print(liste)
            break
fibonacci()

                      

                
        