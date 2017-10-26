# imported webbrowser to open a page on browser
import webbrowser
# created class Movie with initialized variables
# and functions (init and show trailer)


class Movie(): 
    # init method initializes space in memory for new instance
    # init is a reserved word in python
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Display url using the browser
        webbrowser.open(self.trailer_youtube_url)
