def bubble_sort(arr):

    n = len(arr)  
    for passnum in range(n - 1, 0, -1): 
        swapped = False  
        for i in range(passnum):  
            if arr[i] > arr[i + 1]: 
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:  
            break

def test_bubble_sort():

    test_cases = [
        ([], []),  
        ([5], [5]), 
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  
        ([39, 12, 18, 85, 72, 10, 2, 18], [2, 10, 12, 18, 18, 39, 72, 85]), 
        ([3, 3, 1, 2, 3], [1, 2, 3, 3, 3]), 
    ]
    
    for i, (input_list, expected) in enumerate(test_cases):
        bubble_sort(input_list)
        assert input_list == expected, f"Test case {i+1} failed: {input_list} != {expected}"
    print("All test cases passed!")


test_bubble_sort()


arr = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is:", arr)
bubble_sort(arr)
print("Sorted list is:", arr)
