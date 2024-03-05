#function defination
def linear_search(arr,x):

    n = len(arr)

    for i in range(n):
        if arr[i]==x:
            return i
    return -1

# Driver code

arr= [1,2,3,5,6,67,86,56]
x =56
result =linear_search(arr,x)
print ("searching element is present at index :-",result)