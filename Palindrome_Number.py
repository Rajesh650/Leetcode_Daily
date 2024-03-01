def palindrome_number(num):

    reversed_number =0
    Original_number =0

    while num>0:
        digit = num%10
        reversed_number = reversed_number*10+digit
        num = num//10

    return reversed_number == Original_number

#Driver code
number = 787
result = palindrome_number(number)
print(result)
