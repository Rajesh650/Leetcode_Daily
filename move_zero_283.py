def move_zeros(arr):
    c=0
    for i in range(0,len(arr)):

        if arr[i] !=0:

            arr[c],arr[i] =arr[i],arr[c]
            c = c+1
    return arr
            
#driver code

arr1 =[1,3,0,1]
result = move_zeros(arr1)
print(result)


