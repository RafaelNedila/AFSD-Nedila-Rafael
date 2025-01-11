def visualize_selection_sort(arr):
    n = len(arr)

    def draw_array(arr, highlight_indices=[]):
        plt.clf()  
        colors = ['blue' if i not in highlight_indices else 'red' for i in range(len(arr))]
        plt.bar(range(len(arr)), arr, color=colors)
        plt.pause(0.5) 

    plt.figure(figsize=(10, 6))
    plt.title("Selection Sort Visualization")

    for i in range(n):
        min_idx = i
        draw_array(arr, highlight_indices=range(i, n))
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_array(arr, highlight_indices=[i, min_idx])  

    plt.show()
