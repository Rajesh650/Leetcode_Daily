
#*********Iterative approach*******

# def factorial(num):
    
#     factorial = 1

#     for i in range(1,num+1):
#         factorial = factorial*i 

#     return factorial

# num =5
# print(factorial(num))

#####************* Recursive Approach ****

def factorial_recursive(num):

    if num == 0 :
        return 1
    
    else:
        return num*factorial_recursive(num-1)
    
num =5
print(factorial_recursive(num))