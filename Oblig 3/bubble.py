from countswaps import CountSwaps
from countcompares import CountCompares

# Input: Et array med n elementer
# Output: Et sortert array med de samme n elementene
# O(n^2) tid
def sort(array):
    for i in range(len(array) - 1):
        should_stop = True
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array.swap( j, j + 1 ) # array[j], array[j + 1] = array[j + 1], array[j]
                should_stop = False

        if should_stop:
            break
    
    return array
