import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies




movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

#movies_dict = movies_list['title'].values
st.title('Movie Recommender system')
selected_movie_name = st.selectbox(
    "Please select a movie",
    movies['title'].values,
)

st.write("You selected:", selected_movie_name)
# creating a button to recommend movies
if st.button("Recommend"):# button
    recommend= recommend(selected_movie_name)
    for i in recommend:
        st.write(i) # text to display after clicking the button