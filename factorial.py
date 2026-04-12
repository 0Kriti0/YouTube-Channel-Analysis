    
def factorial():
    num=int(input())
    n=num*2
    result = 1
    for i in range(1, n+ 1):
        result *= i
    return result
#n=int(input())
print(factorial())