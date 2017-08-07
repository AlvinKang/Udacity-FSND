import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
						"A story of a boy and his toys that came to life",
						"https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

inception = media.Movie("Inception",
						"A man and his team goes into others' dreams",
						"http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-4.jpg",
						"https://www.youtube.com/watch?v=YoHD9XEInc0")

zootopia = media.Movie("Zootopia",
					   "A bunny and fox team up to solve the myster of Zootopia",
					   "https://s-media-cache-ak0.pinimg.com/originals/5a/29/d7/5a29d758e586fa4c44ef0e9065b4651c.jpg",
					   "https://www.youtube.com/watch?v=CzvH6_e2a-U")

wall_e = media.Movie("Wall-E",
					 "A robot couple brings humanity back to Earth",
					 "https://img.yescdn.ru/2015/09/15/poster/WALL-E_1.jpg",
					 "https://www.youtube.com/watch?v=ZAWIIlXNGwY")

forrest_gump = media.Movie("Forrest Gump",
						   "Autistic man lives through numerous historical events",
						   "http://www.impawards.com/1994/posters/forrest_gump_xlg.jpg",
						   "https://www.youtube.com/watch?v=bLvqoHBptjg")

movies = [toy_story, avatar, inception, zootopia, wall_e, forrest_gump]
fresh_tomatoes.open_movies_page(movies)



