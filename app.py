import streamlit as st
import random
from src.data_loader import load_data, get_name_list
from src.recommendation import get_recommendation

movie_data = load_data()
movie_name_list = get_name_list()

st.header("Movie Recommendations")
st.subheader('Search a movie to get recommendations.')
selected_movie = st.selectbox('Select your favourite movie',options=movie_name_list)

if st.button('Suggest Random'):
    selected_movie = movie_name_list[random.randint(0, len(movie_name_list))]

recommended_movie_names,recommended_movie_posters = get_recommendation(selected_movie)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image(recommended_movie_posters[0], caption=recommended_movie_names[0])
with col2:
    st.image(recommended_movie_posters[1], caption=recommended_movie_names[1])
with col3:
    st.image(recommended_movie_posters[2], caption=recommended_movie_names[2])
with col4:
    st.image(recommended_movie_posters[3], caption=recommended_movie_names[3])


col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image(recommended_movie_posters[4], caption=recommended_movie_names[4])
with col2:
    st.image(recommended_movie_posters[5], caption=recommended_movie_names[5])
with col3:
    st.image(recommended_movie_posters[6], caption=recommended_movie_names[6])
with col4:
    st.image(recommended_movie_posters[7], caption=recommended_movie_names[7])

