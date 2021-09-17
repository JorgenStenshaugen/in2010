import sys

array = []

def array_to_bst( list_to_split ):
    if not len( list_to_split ):
        return
    
    if len( list_to_split ) > 1:
        middle_index = len( list_to_split ) // 2
        middle_element = list_to_split[ middle_index ]

        right_side = list_to_split[ middle_index + 1: ]
        left_side = list_to_split[ :middle_index ]

        print( middle_element )
        
        array_to_bst( right_side )
        array_to_bst( left_side )
    else:
        print( list_to_split[0] )


# User input
for linje in sys.stdin:
    try:
        user_input = int( linje.rstrip() )
        array.append( user_input )

    except:
        array_to_bst( array )
        array = []
        break

if len( array ):
    array_to_bst( array )

