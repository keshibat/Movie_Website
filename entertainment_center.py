#calling the external function: fresh_tomates.py
import fresh_tomatoes
#calling the external function: media.py
import media

# class instantiating section:
Whiplash = media.Movie("Whiplash",
                       #For flowing long blocks of text with fewer structural restrictions
                       #(docstrings or comments), the line length should be limited to 72 characters.
                       #You can see the Python document as follows
                       #"https://www.python.org/dev/peps/pep-0008/#maximum-line-length"
                       "A promising young drummer enrolls at a cut-throat music conservatory "
                       "where his dreams of greatness are mentored by an instructor who will "
                       "stop at nothing to realize a student's potential.",
                       "https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",
                       "https://www.youtube.com/watch?v=7d_jQycdQGo")

Gravity = media.Movie("Gravity",
                      "A medical engineer and an astronaut work together to survive "
                      "after an accident leaves them adrift in space.",
                      "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg",
                      "https://www.youtube.com/watch?v=ufsrgE0BYf0")

Straight_Outta_Compton = media.Movie("Straight Outta Compton",
                                     "The group NWA emerges from the mean streets of Compton in Los Angeles, "
                                     "California, in the mid-1980s and revolutionizes Hip Hop culture "
                                     "with their music and tales about life in the hood.",
                                     "https://upload.wikimedia.org/wikipedia/en/7/7a/Straight_Outta_Compton_poster.jpg", #noqa it is more clean, practical and readable letting them "untouched", than breaking them into shorter lines(the line length should be limited to 72 characters.)
                                     "https://www.youtube.com/watch?v=Y5eg1Qu3fwo")

Good_Wil_Hunting = media.Movie("Good Will Hunting",
                               "Will Hunting, a janitor at M.I.T., has a gift for mathematics, "
                               "but needs help from a psychologist to find direction in his life.",
                               "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg", #noqa
                               "https://www.youtube.com/watch?v=ReIJ1lbL-Q8")

Night_on_Earth = media.Movie("Night on Earth",
                             "An anthology of 5 different cab drivers in 5 American and European "
                             "cities and their remarkable fares on the same eventful night.",
                             "https://upload.wikimedia.org/wikipedia/en/f/f9/Nightonearth.jpg",
                             "https://www.youtube.com/watch?v=o_ESHkySoJs")

Fightlub = media.Movie("Fightclub",
                       "An insomniac office worker, looking for a way to change his life, "
                       "crosses paths with a devil-may-care soap maker, forming "
                       "an underground fight club that evolves into something much, much more.",
                       "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                       "https://www.youtube.com/watch?v=_XgQA9Ab0Gw")
# appending movies into a list:
movies = [Whiplash, Gravity, Straight_Outta_Compton, Good_Wil_Hunting, Night_on_Earth, Fightlub]
# What fresh_tomatoes does is that takes in list of movies as a input and...
# as a output it creates and opens HTML page of website...
#that shows movie I've listed
fresh_tomatoes.open_movies_page(movies)





