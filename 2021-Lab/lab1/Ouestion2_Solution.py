actual = 0  #actual değeri bizim son durumdaki while True döngüsünden çıkan geçerli yılımız olacak
while True:
    last = 0
    try :
        year = int(input("Sıfırdan büyük geçerli bir yıl giriniz: "))
        last = year
    except ValueError:
        print("Lütfen geçerli bir yıl giriniz")
        continue
    if int(last) < 0 :
        print("Yıl sıfırdan küçük olmamalı")
        continue
    actual = year
    break

the_dict = {
2000 : "Ejderha",
2001 : "Yılan",
2002 : "At",
2003 : "Koyun",
2004 : "Maymun",
2005 : "Horoz",
2006 : "Köpek",
2007 : "Domuz",
2008 : "Fare",
2009 : "Öküz",
2010 : "Kaplan",
2011 : "Tavşan"
}


for i in the_dict.keys():
    if abs(i-actual)%12 == 0 :
        print(f"{actual} yılı bir {the_dict[i]} yılıdır")