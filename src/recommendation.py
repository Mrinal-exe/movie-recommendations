from src.data_loader import load_data, get_name_list
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movie_data = load_data()
name_list = get_name_list()


cv = CountVectorizer(max_features=5000,stop_words='english')
    
vector = cv.fit_transform(movie_data['Tags']).toarray()
similarity = cosine_similarity(vector)



def get_recommendation(user_input):
    data_index = movie_data.index[movie_data['Title'] == user_input].to_list()[0]
    similarity_score = list(enumerate(similarity[data_index]))
    similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in similar_movies[1:6]:
        # fetch the movie poster
        recommended_movie_posters.append(movie_data.iloc[i[0]].Poster_Url)
        recommended_movie_names.append(movie_data.iloc[i[0]].Title)

    return recommended_movie_names,recommended_movie_posters



