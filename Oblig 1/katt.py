# 14 - katt pos
import sys
katt  = 0
tre = []

def finn_sti( x ) :
	print( x ) # printer ut noden katten skal gå på

	# Går gjennom nodene i treet.
	for foreldre_noder in tre:
		# Sjekker om noden vi er inkludert som foreldrenode.
		if x in foreldre_noder :
			# Dersom noden vi velger er lik den katten er på så går vi videre i løkka.
			if foreldre_noder[0] == x :
				continue

			# Dersom noden eksisterer som foreldrenode så går katten til neste node.
			prosedyre( i[0] )
			break

for linje in sys.stdin :
	user_input = linje.rstrip().split(" ")

	if len( user_input ) == 1 :
		if int( user_input[0] ) == -1:
			prosedyre( katt )
			break
		else :
			katt = int( user_input[0] )
			continue
			
	tmp = []
	for x in user_input :
		tmp.append( int( x ) )

	liste.append( tmp )
