# Task 38 - Compulsory task 2

# This program will compare the last film watched by the user with a list of movie object descriptions.  It will
# measure word similarity and use this to return the most suitable "next watch" from the stored list of movies.

# SpaCy module imported for similarity comparison:
import spacy
nlp = spacy.load('en_core_web_md')

# Movie class created to store objects:
class Movie():

    # Object builder:
    def __init__(self, name, synopsis):
        self.name = name
        self.synopsis = synopsis

    # String representation for object:
    def __str__(self):
        return self.name


# Blank lists to store movie objects.
movie_list = []


# Function to read movie list from movies.txt file, with defensive programming used to prevent errors of file does
# not exist:
def fetch_movies():
    file = None
    try:   # Try method splits the movies by name and description, to create objects of the Movie class and store as a list:
        file = open("movies.txt", "r", encoding='utf8')
        for line in file.readlines():
            movie = line.strip("\n")
            movie2 = movie.split(" :")
            movie_list.append(Movie(movie2[0], movie2[1]))
    except FileNotFoundError:
        print("I'm sorry, the file movies.txt does not exist.")
    finally:
        if file is not None:
            file.close()
            return movie_list


# Function to compare movies, it takes in the movie list and the last movie description as variables:
def compare_movies(x, y):
    similarity_ratings = []   # New blank list created each time to store similarity values
    last_description = nlp(y)  # Previous description subjected to nlp method
    for obj in x:   # Iterates through list of objects, comparing description to last movie:
        token = nlp(obj.synopsis)
        similarity_ratings.append(last_description.similarity(token))
    max_similarity = max(similarity_ratings)   # Finds value of max similarity rating
    position = similarity_ratings.index(max_similarity)   # Finds position of max similarity rating
    next_movie = x[position] # Finds name of movie with the same position in movies_list
    return next_movie


movies = fetch_movies()

# Date relating to the last movie watched.  This could also be taken from a separate text file, or a stored object
# with a static value of "last watched = True" to provide a real-time update of movies watched.
last_movie_name = 'Planet Hulk'
last_movie_description = f'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, ' \
                   f'the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk ' \
                   f'can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into ' \
                   f'slavery and trained as a gladiator.'

# Returns the name of the next suggested movie for the user:
next_to_watch = compare_movies(movie_list, last_movie_description)

# Simple print statements remind the user of the last movie they watched then provide a suggestion for their next:
print(f"The last movie you saw was {last_movie_name}.")
print(f"If you enjoyed {last_movie_name}, you should try {next_to_watch} next!")
