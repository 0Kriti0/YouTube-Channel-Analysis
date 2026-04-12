def print_hollow_square(n):
    # Top row
    print('*' * n)
    
    # Middle rows
    for _ in range(n - 2):
        print('*' + ' ' * (n - 2) + '*')
    
    # Bottom row (only if n > 1)
    if n > 1:
        print('*' * n)

# Get user input
n = int(input("Enter the side length of the square: "))
print_hollow_square(n)