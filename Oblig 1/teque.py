import sys

queue = []

def push_back( x ) :
	queue.append( x )

def push_front( x ) :
	queue.insert( 0, x )

def push_middle( x ) :
	k = len( queue )
	queue.insert( int( ( k + 1 ) / 2 ), x )

def get( i ) : 
	print( queue[ int( i ) ] )

def main() :
	teller = -1

	for linje in sys.stdin :
		user_input = linje.rstrip()

		if teller == -1:
			teller = int( user_input )
		
		if "push_back" in user_input :
			push_back( user_input.split( " " )[1] )
		
		if "push_front" in user_input :
			push_front( user_input.split( " " )[1] )

		if "push_middle" in user_input :
			push_middle( user_input.split( " " )[1] )

		if "get" in user_input :
			get( user_input.split( " " )[1] )

		if 0 == teller :
			break

		teller -= 1

main()