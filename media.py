import webbrowser

class Movie():
    '''... this allows us to create multople instances of itself
       instance is like Whiplash, Gravity, Straight_Outta_Compton...etc.
    '''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        '''Constrcutor get called when you craete instances such as Whiplash...
           on entertainment_center.py
           init method inside class
           ...Things for class Movie to remember for each instance
           --tile                #Instance Variable
           --storyline           #Instance Variable
           --poster_image        #Instance Variable
           --trailer_on__youtube #Instance Variable
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        ''' Instance Methods
            This function opens a web browser with the correct ULR which plays movie trailer
        '''
        webbrowser.open(self.trailer_youtube_url)




