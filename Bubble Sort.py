def bubble_sort_flowchart(array):
  
  n = len(array)

  for i in range(n):
    swapped = False
    
    for j in range(0, n - i - 1): 
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        swapped = True
    
    if not swapped:
      break

list_of_numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]

if __name__ == "__main__":
    bubble_sort_flowchart(list_of_numbers)

list_of_unsorted_numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]

print("The list is:", list_of_unsorted_numbers)
print("Sorted array in ascending order:")
print(list_of_numbers)