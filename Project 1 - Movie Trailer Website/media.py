#Things this class should store:
    # Title, Storyline, Poster Image, Youtube Trailer
import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        
# Things this class should do:
    # Show Trailer
        
    def show_trailer(self):        
        webbrowser.open_new(self.trailer_youtube_url)
