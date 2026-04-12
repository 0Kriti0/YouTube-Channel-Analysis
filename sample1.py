"""l=[int(d) for d in input().split()]
s=0
for i in range(len(l)):
    s+=i
print(s)"""

"""s="qwertyuiopasdfghjklzxcvbnm"
string=input()
for i in s:
    if i in string.lower():
        a="TRUE"
    else:
        a="FALSE"
print(a)"""

"""f1=open("gf1.txt","w")
f1.write("hello")
f1=open("gf1.txt","r+")
#data=f1.read(3)
#print(data)
print(f1.read())
print(f1.tell())
f1.seek(0)
f1.write("aaaaaaaa")
f1=open("gf1.txt","r+")
print(f1.read())
f1.write("hello to python world")
print(f1.read())"""

"""a=10
b=0
try:
    print(a/b)
    try:
        print("This is inner block")
    except Exception:
        print("General exception")
    finally:
        print("inside inner finally block")
except ZeroDivisionError:
    print("Division by 0")
finally:
    print("inside outer finally block")"""

"""def divide(a,b):
    if b==0:
        raise ValueError("Cannot be divided by zero")
    print(a/b)
try:
    result=divide(10,0)
except ValueError as e:
    print(e)"""