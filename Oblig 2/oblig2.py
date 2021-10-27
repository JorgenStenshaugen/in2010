from filmgraf import FilmGraf
import timeit

if __name__ == "__main__":
	start = timeit.default_timer()
	graf = FilmGraf()
	graf.readMoviesFile()
	graf.readActorFile()

	print( "\n Oppgave 1 \n" )
	graf.countNodesEdges()

	print( "\n Oppgave 2" )
	graf.findShortestPath( "nm2255973", "nm0000460" )
	graf.findShortestPath( "nm0424060", "nm0000243" )
	graf.findShortestPath( "nm4689420", "nm0000365" )
	graf.findShortestPath( "nm0000288", "nm0001401" )
	graf.findShortestPath( "nm0031483", "nm0931324" )

	print( "\n Oppgave 3" )
	graf.findChillestPath( "nm2255973", "nm0000460" )
	graf.findChillestPath( "nm0424060", "nm0000243" )
	graf.findChillestPath( "nm4689420", "nm0000365" )
	graf.findChillestPath( "nm0000288", "nm0001401" )
	graf.findChillestPath( "nm0031483", "nm0931324" )
	
	print( "\n Oppgave 4" )

	graf.count_components()

	stop = timeit.default_timer()
	print( "Kjøretid: ", stop - start )