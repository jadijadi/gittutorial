# This is selection sort algorithm


# find_min function for finding minimum item index
def find_min(list):
    min_item = list[0]
    min_index = 0
    for i in range(len(list)):
        if list[i] < min_item:
            min_item = list[i]
            min_index = i
    return min_index

result = []
def selection_sort(list):
    for _ in range(len(list)):
        smalles = find_min(list)
        result.append(list.pop(smalles))
    return result    

# calling the function
my_list = [7, 6, 5, 4, 3, 2, 1]
print(selection_sort(my_list))
print("<", '-' * 20, "Done", '-' * 20, '>', sep="")