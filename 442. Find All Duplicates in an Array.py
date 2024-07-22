def find_duplicates_set(arr):

    seen = set()
    duplicates = set()

    for elem in arr:

        if elem in seen:
            duplicates.add(elem)

        else:
            seen.add(elem)

    return list(duplicates)

array = [1,2,3,4,5,2,3,1,6]
print(find_duplicates_set(array))

            
