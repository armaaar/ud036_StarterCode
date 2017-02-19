# ud036_StarterCode
Source code for a Movie Trailer website. This is for the "Movie Trailer Website" Project in Udemy. It creates an HTML webpage out of movies list in sperate .JSON files.

## Requirements
The only requirement in so have python and a web browser in your machine. python version 2.7 or higher is recommended.

## Usage
1. Add movies' data in .JSON files in JSON format to 'movies_list' directory. More info in "Add new movie" Section.
2. execute 'movie_trailer_website.py' files.

A webpage will be created in the project directory and be opened in you default web browser. Simple enough!

## Add a new movie
To add a movie, the following data is required for each movie :
- Movie Title
- Movie storyline
- Movie Poster Image URL
- Movie Trailer Youtube URL
if any of these data are missing, a default value will be assigned to the movie. 

Every single movie should be defined in a sperate .JSON file, This example shows how to write the movie .JSON file :
```
{
	"title" : "Example Movie",
	"storyline" : "A story about an example file trying to demonstrate how to use the feature correctly to a user",
	"poster_image_url" : "https://pdfimages.wondershare.com/images/tutorial/movie-poster-template.jpg",
	"trailer_youtube_url" : "https://www.youtube.com/watch?v=wsDOFF1y_uI"
}
```
Good to notice :
- The order of lines betweet curly brackets `{ ... }` can be changed as long as the last line doesn't end with a `,`.
- The extension of  .JSON file is case insensetive.
- The name of .JSON file only affects the order of the movies displayed in the web page, It's recommended to name the .JSON file as the movie title.

