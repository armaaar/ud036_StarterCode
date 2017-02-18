from media import movie # import Movie class
import fresh_tomatoes as template # import web template
import os, json # import necessary modules to get movies data

movies = [] # Movie objects list

# Read movies JSON files
for file_name in os.listdir("./movies_list/"):
    if file_name.lower().endswith(".json"):
        # Open file
        movie_file = open("./movies_list/"+file_name, 'r') 
        # Read file => parse JSON string to dictionary
        json_string = movie_file.read()
        print(json_string)
        movie_data = json.loads(json_string)
        # Create Movie object 
        movie_object = movie.Movie(movie_data)
        movies.append(movie_object)
        #get ready for a new loop
        del movie_object
        movie_file.close()
        
# Open web page
template.open_movies_page(movies)
