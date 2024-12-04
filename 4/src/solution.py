from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Movie
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def get_all_movies(session):

    movies = session.execute(select(Movie)).scalars().all()

    return [
        f"{movie.title} by {movie.director}, released on {movie.release_date}, duration: {movie.duration} min, genre: {movie.genre}, rating: {movie.rating}"
        for movie in movies
    ]

def get_movies_by_director(session, director_name):

    movies = session.execute(select(Movie).where(Movie.director == director_name).order_by(Movie.release_date)).scalars().all()

    return [
        f"{movie.title} by {movie.director}, released on {movie.release_date}, duration: {movie.duration} min, genre: {movie.genre}, rating: {movie.rating}"
        for movie in movies
    ]

def get_top_rated_movies(session, n):

    movies = session.execute(select(Movie).order_by(Movie.rating.desc())).scalars().all()[:n]

    return [
        f"{movie.title} by {movie.director}, released on {movie.release_date}, duration: {movie.duration} min, genre: {movie.genre}, rating: {movie.rating}"
        for movie in movies
    ]
# END
