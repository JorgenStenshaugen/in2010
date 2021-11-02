from countswaps import CountSwaps
from countcompares import CountCompares

# Hjelpeprosedyre for å bygge en max-heap
# Input: En (uferdig) heap 'array' med n elementer der i er roten
# Output: En mindre uferdig heap
def bubbleDown(array, i, n):
	largest = i
	left = (2 * i) + 1
	right = (2 * i) + 2

	if left < n and array[largest] < array[left]:
		largest, left = left, largest

	if right < n and array[largest] < array[right]:
		largest, right = right, largest

	if i != largest:
		array.swap( i, largest )

		# array[i], array[largest] = array[largest], array[i]
		bubbleDown(array, largest, n)
	

# Bygge en max-heap
# Input: Et array med n elementer
# Output: array som en max-heap
def buildMaxHeap(array, n):
	for i in range(len(array) // 2, -1, -1):
		bubbleDown(array, i, n)

# Input: Et array med n elementer
# Output: Et sortert array med de samme n elementene
# Heapsort - O(n log(n)) tid
def heapSort(array):
	buildMaxHeap(array, len(array))
	i = len(array) - 1
	for i in range(len(array) -1, -1, -1):
		array.swap( 0, i )
		# array[0], array[i] = array[i], array[0]
		bubbleDown(array, 0, i)

	return array
