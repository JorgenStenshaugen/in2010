import sys

array = []

def balanced_binary_search_tree(list):
    if len(list) == 1:
        print(list[0])
    
    if len(list) > 1:
        middle_index = len(list) // 2
        middle_element = list[middle_index]
        right_side = list[middle_index + 1:]
        left_side = list[:middle_index]

        print(middle_element)
        
        balanced_binary_search_tree(right_side)
        balanced_binary_search_tree(left_side)


for linje in sys.stdin:

    try:
        user_input = int(linje.rstrip())
        array.append(user_input)

    except:
        balanced_binary_search_tree(array)
        array = []

balanced_binary_search_tree(array)

