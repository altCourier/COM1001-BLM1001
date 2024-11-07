"""
xxxxx 
xxxx 
xxx 
xx 
x
"""
number = int(input())
for i in range(number,0,-1):
    print("x"*i)

# For some sensual reason you wished to write it in a nested loop.
# Maybe you love the complexity, we don't know.

for i in range(number,0,-1):
    for j in range(i):
        print("x", end="")
    print()