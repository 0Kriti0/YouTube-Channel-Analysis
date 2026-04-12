"""sum = 0
i=0
while (i<= 10):
    n= int(input())
    i+=1
    if(i<=10):
        print(n)
        continue
    
        if (n<0):

        break
        else:
        sum+=n
        print(total_sum)
"""
sum=0
inputs = []
#print("Enter exactly 10 inputs:")
for i in range(10):
    n =int(input())
    inputs.append(n)
    
    if(n<0):
        break
    else:
        sum+=n
print(sum)
#print(inputs)
 