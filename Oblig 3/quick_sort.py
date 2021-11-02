import random

# Input: Et array med n elementer, low og high er indekser
# Output: Flytter elementer som er henholdsvis mindre og større til venstre og høyre enn en gitt indeks som returneres
def partition(array, low, high):
	pivot = (low + high) // 2

	array[pivot], array[high] = array[high], array[pivot]
	pivot = array[high]
	left = low
	right = high - 1

	while left <= right:
		while left <= right and array[left] <= pivot:
			left = left + 1

		while right >= left and array[right] >= pivot:
			right = right - 1

		if left < right:
			array[left], array[right] = array[right], array[left]

	array[left], array[high] = array[high], array[left]

	return left

# Beste tilfelle: O(n log(n)) tid hvor pivot er midt i mellom low og high, da halverer vi arbeidet for hvert rekursive kall
# Verste tilfelle: O(n^2) tid men dette skjer sjeldent som vil si at quicksort er som regel veldig effektivt
def quickSort(array, low, high):
	if low >= high:
		return array

	pivot = partition(array, low, high)
	quickSort(array, low, pivot - 1)
	quickSort(array, pivot + 1, high)

	return array

test_array = [random.randint(0, 100) for _ in range(15)]
lowest_index = 0
highest_index= len(test_array) - 1

print(quickSort(test_array, lowest_index, highest_index))
