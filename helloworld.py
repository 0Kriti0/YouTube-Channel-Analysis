total_sum = 0
count = 0

while count < 10:
    try:
        num = int(input(f"Enter integer {count + 1}: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if num < 0:
        break

    total_sum += num
    count += 1

print(f"The sum of the entered positive integers is: {total_sum}")