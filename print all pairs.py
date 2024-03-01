# def all_pairs(arr):
#     n = len(arr)
#     pairs=[]
    
#     for i in range (0,n):
#         for j in range(i,n):
#             pairs.append((arr[i], arr[j]))
            
#     return pairs
    
# #Driver code            

# arr= [10,20,30]
# result = all_pairs(arr)
# print (result)

def Pair_sum(arr,n,x):

    for i in range(0,n):
        for j in range(i,n):

            if(arr[i] + arr[j] == x):
                print("Yes")
            else:
                print("No")
    return (arr[i],arr[j])


# Driver code
arr = {1, 4, 45, 6, 10, 8}
n = 6
x =16
result = Pair_sum(arr,n,x)
print (result)            
















