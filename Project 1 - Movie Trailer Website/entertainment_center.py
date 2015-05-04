import media
import fresh_tomatoes

# filename.Classname
# creating an instance of the Class Movie, saved in file media, called toy_story
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "http://ecx.images-amazon.com/images/I/51NpxQ0ma8L.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
    
# Creating an instance of the Class Movie,  called avatar
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Creating an instance of the Class Movie,  called iron_man
iron_man = media.Movie("Iron Man",
                       "A crazy innovator",
                       "http://www.firstshowing.net/img/final-ironman-poster2-big.jpg",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

# Creating an instance of the Class Movie,  called monte_cristo
monte_cristo = media.Movie("The Count of Monte Cristo",
                       "A man who loses it all before deciding to take it all back",
                       "http://manilovefilms.com/wp-content/uploads/2013/06/montecristo-poster.jpg",
                       "https://www.youtube.com/watch?v=JG7FDivQLac")


#print (avatar.storyline)

#toy_story.show(trailer()
               
#avatar.show_trailer()

#iron_man.show_trailer()


# Creating a List with all the movies (all the instances of class Movie)
movies = [toy_story, avatar, iron_man, monte_cristo]

# Running the list through the fresh tomatoes script to generate an html page 
fresh_tomatoes.open_movies_page(movies)
