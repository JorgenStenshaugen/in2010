import random

# O(n) tid
def merge(left, right, array):
	i = 0
	j = 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			array[i + j] = left[i]
			i = i + 1
		else:
			array[i + j] = right[j]
			j = j + 1

	while i < len(left):
		array[i + j] = left[i]
		i = i + 1

	while j < len(right):
		array[i + j] = right[j]
		j = j + 1

	return array

# O(n log (n)) tid
def mergeSort(array):
	if len(array) <= 1:
		return array
	
	i = len(array) // 2
	left = mergeSort(array[:i]) # array[0..i-1]
	right = mergeSort(array[i:]) # array[i..n-1]

	return merge(left, right, array)