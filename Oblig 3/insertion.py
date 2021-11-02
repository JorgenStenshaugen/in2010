from countswaps import CountSwaps
from countcompares import CountCompares
# Input: Et array med n elementer
# Output: Et sortert array med de samme n elementene

# O(n) * O(n) = O(n^2) tid
# Spesielt rask på 'nesten sorterte' arrayer - blant de raskeste algoritmene for små arrayer
def sort(array):
    for i in range(len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array.swap( j - 1, j ) # array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1
    
    return array
