def fibonacci():
    while True : 
        try :
            num1 = int(input("Lütfen birinci tam sayıyı giriniz: "))
            num2 = int(input("Lütfen ikinci tam sayıyı giriniz: "))
        except ValueError :
            print("Lütfen geçerli bir tam sayı girin")
            continue
        break
    while True :
        uzunluk = input("Dizinizin kaç elemandan oluşacağını yazın(2'den büyük pozitif bir tam sayı girin): ")
        if uzunluk.isdecimal() == False or int(uzunluk) == 0 or int(uzunluk) <= 2  :
            print("Geçerli bir liste uzunluğu girin")
            continue
        break
    uzunluk_ = int(uzunluk)
    liste = [num1,num2]
    for i in range(0,uzunluk_-2):
        liste.append((liste[i]+liste[i+1]))
    print(liste)
fibonacci()
                      

                
        
