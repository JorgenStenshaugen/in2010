from heapq import heappop, heappush

import sys

array = []

def array_to_bst(right_side):    
    if not len(right_side):
        return
    
    if len(right_side) > 1:
        middle_index = len(right_side) // 2
        
        left_side = []
        for e in range(middle_index):
            right = heappop(right_side)
            heappush(left_side, right)

        print(heappop(right_side))

        array_to_bst(right_side)
        array_to_bst(left_side)
        
    else:
        print(heappop(right_side))

for linje in sys.stdin:
    try:
        user_input = int(linje.rstrip())
        heappush(array, user_input)

    except:
        array_to_bst(array)
        array = []

array_to_bst(array)
