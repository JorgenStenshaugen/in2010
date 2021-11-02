import random
# Input: Et array med n elementer
# Output: Et sortert array med de samme n elementene

test_array = [random.randint(0, 100) for _ in range(15)]
# O(n) * O(n) = O(n^2) tid
# Spesielt rask på 'nesten sorterte' arrayer - blant de raskeste algoritmene for små arrayer
def insertionSort(array):
    for i in range(len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1
    
    return array

print(insertionSort(test_array))
