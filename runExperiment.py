import pprint # pretty print

# load movie DB
dbFilename = './data/comodaMoviesTXT.txt';
dbFileHandler = open(dbFilename,'r')

movie_id = [];
movie_title = [];

for line in dbFileHandler:
	words = line.split(';')
	
	movie_id.append(words[0])
	movie_title.append(words[1].strip())



# loop through the database
iMovie = 0;
while iMovie < len(movie_id):
	print('Processing movie id=',movie_id[iMovie],' (',movie_title[iMovie],')')
	
	#do what you have to do
	
	
	
	iMovie+=1
