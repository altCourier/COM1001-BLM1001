# Whilest using the series below calculate the number pi.
# pi = 4 -4/3+4/5-4/7...
total = 0
sign = 1
termNumber = int(input("Please enter the number of integers: "))
for item in range(termNumber):
    total += sign*4/((item*2)+1)
    sign *= -1
print(total)