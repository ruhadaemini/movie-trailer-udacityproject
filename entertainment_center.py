# imported media file and fresh_tomatoes that helps displaying movies
import fresh_tomatoes
import media

# Created some movies that have name, story description,
# image link and youtube trailer
movie1 = media.Movie("Spider-Man",
                     "Storyline",
                     "http://bit.ly/2oN4ka7",
                     "https://www.youtube.com/watch?v=O7zvehDxttM")

movie2 = media.Movie("Logan",
                     "Storyline",
                     "http://bit.ly/2ppTK6A",
                     "https://www.youtube.com/watch?v=Div0iP65aZo")

movie3 = media.Movie("Beauty and the Beast",
                     "Storyline",
                     "http://bit.ly/2oDmiuR",
                     "https://www.youtube.com/watch?v=7pQQHnqBa2E")

movie4 = media.Movie("Mockingjay 1",
                     "Storyline",
                     "http://bit.ly/2oMXocU",
                     "https://www.youtube.com/watch?v=3PkkHsuMrho")

movie5 = media.Movie("Savages",
                     "Storyline",
                     "http://bit.ly/2oDoXoy",
                     "https://www.youtube.com/watch?v=xXNxKwAKGpw")

movie6 = media.Movie("Snowden",
                     "Storyline",
                     "http://bit.ly/2oghsRZ",
                     "https://www.youtube.com/watch?v=QlSAiI3xMh4",)

# Movies array
movies = [movie1, movie2, movie3, movie4, movie5, movie6]
# opens the page where movies are created
fresh_tomatoes.open_movies_page(movies)
