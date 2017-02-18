
class Movie() :
    """This class is used to create readable movie objects to be used in `fresh_tomatoes.py` script"""

    def __init__(self, args) :
        """Class Constructor. Used to define object variables.

        Args:
            args (dict): contains variable names and their values.
                         used instead of seperate parameters to enhance readability.      
        """
        # Create object variables
        if isinstance(args, dict) : # Check if args is a dictionary
            if "title" in args :
                self.title = args["title"]
            else :
                self.__fallback_definition(["title"])

            if "storyline" in args :
                self.title = args["storyline"]
            else :
                self.__fallback_definition(["storyline"])

            if "poster_image_url" in args :
                self.title = args["poster_image_url"]
            else :
                self.__fallback_definition(["poster_image_url"])

            if "trailer_youtube_url" in args :
                self.title = args["trailer_youtube_url"]
            else :
                self.__fallback_definition(["trailer_youtube_url"])
                
        else : # if args is not a dictionary : fallback
            self.__fallback_definition(["title", "storyline",
                                        "poster_image_url",
                                        "trailer_youtube_url"])

    def __fallback_definition(self, variable_names_list) :
        """Assigns default values to main object variables if they don't exist

        Args:
            variable_names_list (list): list of strings containing variables' names.

        Supported Variables :
            title, storyline, poster_image_url, trailer_youtube_url.
            
        Returns:
            Always returns True.

        """
        
        # Check if variable_names are a list
        if not isinstance(variable_names_list, basestring) :
            # If not, make it a list
            variable_names_list = [variable_names_list]
        
        for name in variable_names_list :
            if name == "title" :
                self.title = None
            elif name == "storyline" :
                self.storyline = None
            elif name == "poster_image_url" :
                self.poster_image_url = None
            elif name == "trailer_youtube_url" :
                self.trailer_youtube_url = None
        return True
