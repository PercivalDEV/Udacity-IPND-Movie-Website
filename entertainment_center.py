"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media

def main():
    """Six Movie objects, initialising these objects with title, storyline,
    poster image link, video trailer and a release date."""
    jfk = media.Movie("JFK",
                          "Shots heard round the world",
                          "https://upload.wikimedia.org/wikipedia/en/8/84/JFK-poster.png",
                          "https://www.youtube.com/watch?v=w16bYZ-4nmE",
                          "December 20, 1991")

    event_hor = media.Movie("Event Horizon",
                          "Astronauts sent on a rescue mission after a missing space ship",
                          "https://upload.wikimedia.org/wikipedia/en/8/8c/Event_horizon_ver1.jpg",
                          "https://www.youtube.com/watch?v=OVlnER8SxfQ",
                          "August 15, 1997")

    res_evil = media.Movie("Resident Evil",
                           "Zombie-causing virus escapes from the lab",
                           "https://upload.wikimedia.org/wikipedia/en/a/a1/Resident_evil_ver4.jpg",
                           "https://www.youtube.com/watch?v=u6uDnd_v5Bw",
                           "March 15, 2002")

    matrix = media.Movie("The Matrix",
                         "The world is a simulation",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8",
                         "March 31, 1999")

    aliens = media.Movie("Aliens",
                           "Marines encounter xenos and end up the hunted",
                           "https://upload.wikimedia.org/wikipedia/en/f/fb/Aliens_poster.jpg",
                           "https://www.youtube.com/watch?v=XKSQmYUaIyE",
                           "May 22, 1992")

    the_aven = media.Movie("The Avengers",
                          "A group of heroes form to defend our world",
                          "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                          "https://www.youtube.com/watch?v=eOrNdBpGMv8",
                          "May 4, 2012")

    # Store the Movie objects in a list.
    movies = [jfk, event_hor, res_evil, matrix, aliens, the_aven]

    # Open the movie website in the user's browser, featuring the movies above.
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
