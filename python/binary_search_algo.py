# This is a binary search algorithm
# At : 23/6/1402(probably)


def binary_search(arr, item):
    # Variables #
    low = 0
    high = len(arr) - 1
    duration = 0

    # Binary Searching
    while low <= high:
        duration += 1
        mid = (low+high) // 2
        
        # Checking differences between target value("item") and middle of array("mid")
        if arr[mid] == item:
            return f"\n||| I found {item} at the {mid} index of the array |||\n# Duration : {duration}"
        elif arr[mid] > item:
            high = mid - 1
            print(f"its lower than {arr[mid]}!")
        else:
            low = mid + 1
            print(f"its bigger than {arr[mid]}!")


# run the function
print("\n\n<-------------Binary Searching------------->\n")

numbers_array = range(1, 10000)
print(binary_search(numbers_array, 250))

print("\n<------------------Done------------------->\n")
