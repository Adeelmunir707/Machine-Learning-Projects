# we can use flask, but we will use streamlit library for our API

import streamlit as st
import pickle
import pandas as pd
import requests


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recomended_movies = []
    recomended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id                                 # similar movie index will replace i[0]
        recomended_movies.append(movies.iloc[i[0]].title)      # now extract the movies names of these 5 indices
    # fetching poster for movies from API
        recomended_movies_poster.append(fetch(movie_id))
    return recomended_movies,recomended_movies_poster

def fetch(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


# movies file
movies_dict =  pickle.load(open('movies_dict.pkl','rb'))          # loading movies list and opeingin it in read binary
movies = pd.DataFrame(movies_dict)

# similarity file
similarity= pickle.load(open('similarity.pkl','rb'))          # loading movies list and opeingin it in read binary

st.title("Movies Recomender System")

# getting the movies list from the movie_recomender.ipynb to here,
# using pikkle library
selected_movie_name = st.selectbox(
    'Now Get What You Want',
    (movies['title'].values)
)

# button
if st.button('Recommend', 'Thanks'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])


