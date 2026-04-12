"""def my_min(*args):
    result = args[0]  
    for num in args[1:]:
        if num < result:
            result = num
    return result
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
print(my_min(a,b,c,d,e))"""

"""def print_shallow_square(size):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print('* ', end='')
            else:
                print('  ', end='')
        print()
n=int(input())
print_shallow_square(n)"""

"""def print_custom_pattern(size):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print('*.', end='')
            else:
                print('.', end='')
        print()
print_custom_pattern(4)
""""""
def print_custom_pattern(size):
    for i in range(size):
        for j in range(size):
            if (i == 0 or i == size - 1) or (j % 2 == 0 and i==0 or i==size-1):
                print('*', end='.')
            if (i != 0 or i != size - 1):
                if(j==0 or j==size-1):
                    print("*",end="")
                else:
                    print(".",end="")
             #   print('*', end='.')
           # elif (j == 0 or j == size - 1) or i % 2 == 0:
            #    print('*', end='')
#            if (j == 0 or j == size - 1) or i % 2 != 0:
                print('*', end='')
            else:
                #print('.', end='')
                pass
        print()

print_custom_pattern(4)"""
"""
"""
"""list1=[1,2,3]
list2=[4,5,6]
list1+=list2
print(list1)


"""
"""d1=input("data: ")
list1=d1.split(",")
list2=list1
print("list1 is list2:",list1 is list2)
print("list2 is list1:",list2 is list1)
"""
"""def find_char(a,b):
    for i in range(len(a)):
        if a[i]==b:
            return i+1
    else:
        return "not found"
"""
"""str=input()
e=input()
#print(find_char(str,e))#for finding place values without repitition

def placevalue(a, b):
    positions = []
    for i in range(len(a)):
        if a[i] == b:
            positions.append(i + 1)
    if positions:
        for i in positions:
            print(i) 
    else:
        print("not found") #for finding all the place values

print(placevalue(str,e))"""
"""def placevalue(a, b):
    positions = ""
    for i in range(len(a)):
        if a[i] == b:
            positions += str(i + 1) + " "
    if positions:
        return positions.strip()
    else:
        return "not found"

string = input("Enter the string: ")
element = input("Enter the element to find: ")
print(placevalue(string, element))""" #in the same line

"""def input_keys_values():
    # Input keys
    keys = input("Enter keys (comma-separated): ").split(',')

    # Input values for each key
    values = {}
    for key in keys:
        value_list = list(map(int, input(f"Enter values as list of integers for {key}: ").split(',')))
        values[key.strip()] = value_list
    
    return values

def print_dictionary_table(dictionary):
    # Print the keys as headers
    keys = list(dictionary.keys())
    print("\t".join(keys))
    
    # Find the maximum length of the lists
    max_len = max(len(v) for v in dictionary.values())
    
    # Print the values in a table format
    for i in range(max_len):
        row = []
        for key in keys:
            try:
                row.append(str(dictionary[key][i]))
            except IndexError:
                row.append('')  # If the list is shorter, add an empty string
        print("\t".join(row))

# Main program
dictionary = input_keys_values()
print(dictionary)
print_dictionary_table(dictionary)
def input_keys_values():
    # Input keys
    keys = input("keys: ").split(',')
    
    # Input values for each key
    values = {}
    for key in keys:
        value_list = list(map(int, input(f"values for {key.strip()}: ").split(',')))
        values[key.strip()] = value_list
    
    return values

def print_dictionary_table(dictionary):
    # Print the dictionary
    print(dictionary)

    # Print the keys as headers
    keys = list(dictionary.keys())
    print(" ".join(keys))
    
    # Find the maximum length of the lists
    max_len = max(len(v) for v in dictionary.values())
    
    # Print the values in a table format
    for i in range(max_len):
        row = []
        for key in keys:
            try:
                row.append(str(dictionary[key][i]))
            except IndexError:
                row.append('')  # If the list is shorter, add an empty string
        print(" ".join(row))

# Main program
dictionary = input_keys_values()
print_dictionary_table(dictionary)
"""
"""def input_keys_values():
    # Input keys
    keys = input("keys: ").split(',')
    
    # Input values for the keys
    values = []
    for i in range(len(keys)):
        a=list(map(int, input("values: ").split(',')))
        values.append(a)

    # Create the dictionary
    dictionary = {keys[i].strip(): values[i] for i in range(len(keys))}
    
    return dictionary

def print_dictionary_table(dictionary):
    # Print the dictionary
    print(dictionary)
    
    # Print the keys as headers
    keys = list(dictionary.keys())
    print(" ".join(keys))
    
    # Find the maximum length of the lists
    max_len = max(len(v) for v in dictionary.values())
    
    # Print the values in a table format
    for i in range(max_len):
        row = []
        for key in keys:
            try:
                row.append(str(dictionary[key][i]))
            except IndexError:
                row.append('')  # If the list is shorter, add an empty string
        print(" ".join(row))

# Main program
dictionary = input_keys_values()
print_dictionary_table(dictionary)"""
"""n=int(input("enter: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""

'''d=int(input())
o=[int(d) for d in input().split()]
c=[int(d) for d in input().split()]
ot=o[0]+(d-o[1])*o[2]
print(ot)
ct=c[1]+d/c[0]*c[2]+d*c[3]
print(ct)
if ot>ct:
    print("Online Taxi")
else:
    print("Classic Taxi")
'''


# Using tuple unpacking (Pythonic way)
a, b = 5, 10
a, b = b, a

print("a:", a)  # Output: a: 10
print("b:", b)  # Output: b: 5