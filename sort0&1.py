def count_zeros_ones(arr):
    count_zero = 0
    count_one = 0

    # Count the number of 0s and 1s in the array
    for num in arr:
        if num == 0:
            count_zero += 1
        elif num == 1:
            count_one += 1

    index = 0
    # Overwrite the array with 0s followed by 1s
    while count_zero > 0:
        arr[index] = 0
        index += 1
        count_zero -= 1

    while count_one > 0:
        arr[index] = 1
        index += 1
        count_one -= 1

# Example usage:
arr = [0, 1, 0, 1, 1, 0, 0, 1]
print("Original array:", arr)
count_zeros_ones(arr)
print("Segregated array:", arr)
