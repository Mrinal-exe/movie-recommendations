
import pandas as pd 

def load_data():
    try:
        data = pd.read_csv('data/movies.csv')
        return data
    except Exception as e:
        print('Error loading Data!')
        raise e

def get_name_list():
    movie_data = load_data()
    try:
        list_of_all_movies = movie_data['Title'].tolist()
        return list_of_all_movies
    except Exception as e:
        print("Error Getting movie Titles!")
        raise e
