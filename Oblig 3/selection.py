from countswaps import CountSwaps
from countcompares import CountCompares
# List comprehension med 15 vilkårlige elementer hvor hvert element er et tall mellom 0-100
# test_array = [random.randint(0, 100) for _ in range(15)]

# Input: Et array med n elementer
# Output: Et sortert array med de samme n elementene
# O(n) * O(n) = O(n^2) tid
def sort(array):
    for i in range(len(array)):
        k = i
        for j in range(i + 1, len(array)):
            if array[j] < array[k]:
                k = j
        if i != k:
            array.swap( i, k ) # array[i], array[k] = array[k], array[i]

    return array
