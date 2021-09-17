from heapq import heappop, heappush

import sys

array = []

def heap_to_bst( right_side ):    
    if not len( right_side ):
        return
    
    if len( right_side ) > 1:
        middle_index = len( right_side ) // 2
        
        left_side = []
        for index in range( middle_index ):
            deleted_from_right = heappop( right_side )
            heappush( left_side, deleted_from_right )

        print( heappop( right_side ) )

        heap_to_bst( right_side )
        heap_to_bst( left_side )
        
    else:
        print( heappop( right_side ) )

for linje in sys.stdin:
    try:
        user_input = int( linje.rstrip() )
        heappush( array, user_input )

    except:
        heap_to_bst( array )
        array = []
        break

if len( array ):
    heap_to_bst( array )
