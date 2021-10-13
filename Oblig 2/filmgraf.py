from actor import Actor
from movie import Movie

import timeit

class FilmGraf:
	def __init__( self ):
		self.actors = []
		self.movies = {}
	
	def readActorFile( self ):
		# nm-id Navn tt-ID1 tt-ID2 . . . tt-IDn
		file = open( "actors.tsv", "r" )
		for line in file:
			actorInfo = line.rstrip( "\n" ).split( "\t" )

			id        = actorInfo[0]
			name      = actorInfo[1]
			movieList = actorInfo[2:]
			movieList2 = []

			

			for movieID in movieList:
				if movieID in self.movies:
					movieList2.append( self.movies[ movieID ] )
			
			actor = Actor( id, name, movieList2 )
			for movieID in movieList:
				if movieID in self.movies:
					self.movies[ movieID ].addActor( actor )

			actor.add_edges()

			self.actors.append( actor )

		file.close()
	
	def readMoviesFile( self ):
		# tt-id Tittel Rating
		file = open( "movies.tsv", "r" )
		for line in file:
			movie = line.rstrip( "\n" ).split( "\t" )
			id     = movie[0]
			title  = movie[1]
			rating = movie[2]

			self.movies[ id ] = Movie( id, title, rating )

		file.close()
	
	def countNodesEdges( self ):
		print( "Oppgave 1:\n" )
		print( "Nodes:", len( self.actors ) )

		count = 0
		for actor in self.actors:
			for movie, edges in actor.edges.items():
				count += len( edges )
		
		print( "Edges:", count )

	
	def findShortestPath( self, graph, nmid1, nmid2): #BFS
		start = self.actors[ nmid1 ]
		end = self.actors[ nmid2 ]
		movie = None
		movie_rating = None
		
		visited = []
		queue = [[start]]
		if start == end:
			return
		while queue:
			path = queue.pop(0)
			node = path[-1]
			if node not in visited:
				neighbours = graph[node]
				for neighbour in neighbours:
					shortest_path = list(path) 
					shortest_path.append(neighbour)
					queue.append(shortest_path)
					if neighbour == end:
						print(start)
						for i in range(1, len(shortest_path)):
							print("=== [movies[i], (, self.movie.rating[i] ,) ] ===>", shortest_path[i])
						return
				visited.append(node)
				
	def findChillestPath( self ):
		movie = None
		actor = None
		print( "===[ ", movie, "(", movie.rating ,") ] ===>", actor )
	
test = FilmGraf()
start = timeit.default_timer()
test.readMoviesFile()
test.readActorFile()
test.countNodesEdges()
stop = timeit.default_timer()

print('Time: ', stop - start)

graph = None
nmid1 = "nm2255973"
nmid2 = "nm0000460"
test.findShortestPath(graph, nmid1, nmid2)
