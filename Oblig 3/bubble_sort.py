import random

test_array = [random.randint(0, 100) for _ in range(15)]

# Input: Et array med n elementer
# Output: Et sortert array med de samme n elementene
# O(n^2) tid
def bubbleSort(array):
    for i in range(len(array) - 1):
        should_stop = True
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                should_stop = False

        if should_stop:
            break
    
    return array

print(bubbleSort(test_array))
