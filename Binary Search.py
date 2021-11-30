def binary_search_flowchart(list_of_numbers, value):
    
    start = 0
    end = len(list_of_numbers) - 1
    mid = 0

    while start <= end:
        mid = (start + end) // 2
        array = list_of_numbers[mid]

        if array == value:
            return mid
        
        if array > value:
            end = mid - 1
        else:
            start = mid + 1

    return -1 

if __name__ == "__main__":  
    
    list_of_numbers = [1, 2, 4, 7, 11, 22, 38, 42, 43]
    value = 38

    index = binary_search_flowchart(list_of_numbers, value)
    print(f"Number found in list {list_of_numbers} at index {index} using binary search") 