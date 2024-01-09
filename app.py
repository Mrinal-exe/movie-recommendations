import streamlit as st
from src.data_loader import load_data, get_name_list
from src.recommendation import get_recommendation

movie_data = load_data()
movie_name_list = get_name_list()

st.header("Movie Recommendations")
selected_movie = st.selectbox('Select your favourite movie',options=movie_name_list)



if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = get_recommendation(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])