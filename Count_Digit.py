def count_digit(num):
    # Initialize the count of digits to 0
    count = 0
    
    # If the number is 0, return 1 as there's one digit
    if num == 0:
        return 1
    
    # Loop until num becomes 0
    while num > 0:
        # Increment count for each digit
        count += 1
        # Remove the last digit from num
        num = num // 10
    
    # Return the count of digits
    return count
    
    
num = 1000
result = count_digit(num)
print(result)  # This will print the number of digits in the number
