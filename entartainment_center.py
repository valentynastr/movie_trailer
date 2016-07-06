# Import modules
import media 
import fresh_tomatoes

# The instance for "Toy Story" movie
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# The instance for "Avatar" movie
avatar = media.Movie("Avatar",
                     "Amarine on an alient planet",
                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://youtu.be/5PSNL1qE6VY")
                    

# The instance for "School of rock" movie
school_of_rock = media.Movie("School of rock",
                             "Using rock to learn a music",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

# The instance for "Ratatouille" movie
ratatouille= media.Movie("Ratatouille",
                         "A rat a chif in Paris",
                         "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                         "https://www.youtube.com/watch?v=eh62Ri60lXI")

# The instance for "Midnight in Paris" movie
midnight_in_paris = media.Movie("Midnight in Paris","Going back in the time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

# The instance for "Hunger_games" movie
hunger_games = media.Movie("Hunger_games","a really real reality show",
                           "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg",
                           "https://www.youtube.com/watch?v=Y4VIRBtVRZo")

# List of movies
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

# Openning movie web page 
fresh_tomatoes.open_movies_page(movies)


