def right_shift(arr,n):

    n = len(arr)

    temp = arr[n-1]

    for i in range(n,0):
        arr[i] = arr[i-1]

    arr[0]= temp

    return arr

arr= [10,20,30,40,50]
n = len(arr)
result = right_shift(arr,n)
print(result)


        

