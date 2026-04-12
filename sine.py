import math
a=int(input())
b=int(input())
for i in range(a,b+1):
    sine=math.sin(i)
    print("{:.2f}".format(sine))