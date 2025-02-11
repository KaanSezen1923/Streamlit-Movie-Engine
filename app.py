import os 
import requests
import streamlit as st
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"
HEADERS = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkNGQ4OTlmNDY4MGQ4ZGZmZmExODk3MmEwZWNhYTcyOCIsIm5iZiI6MTY4NzI4MDMwMC45NDEsInN1YiI6IjY0OTFkYWFjMjYzNDYyMDE0ZTU5YzZlZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bzAjIfieM-JBQSCDG3JQzn56-BMq40Y8NF6TJjPO1lg"
}


genre_response = requests.get(f"{BASE_URL}/genre/movie/list?language=en", headers=HEADERS)
genres_data = genre_response.json().get('genres', [])
genre_dict = {genre['name']: genre['id'] for genre in genres_data}


def parse_year(year_selection):
    if not year_selection:
        return {}
    
    if year_selection.startswith('between'):
        start, end = [int(y) for y in year_selection.split() if y.isdigit()]
        return {
            'primary_release_date.gte': f"{start}-01-01",
            'primary_release_date.lte': f"{end}-12-31"
        }
    elif year_selection == "before 2000":
        return {'primary_release_date.lte': '1999-12-31'}
    else:
        return {'primary_release_year': int(year_selection)}

def parse_imdb(imdb_selection):
    if not imdb_selection:
        return {}
    value = int(imdb_selection.split()[0])
    return {'vote_average.gte': value, 'vote_count.gte': 100}

def get_video(movie_id):
    try:
        response = requests.get(
            f"{BASE_URL}/movie/{movie_id}/videos",
            headers=HEADERS,
            params={'language': 'en-US'}
        )
        videos = response.json().get('results', [])
        for video in videos:
            if video['site'] == 'YouTube' and video['type'] == 'Trailer':
                return video['key']
        return None
    except Exception as e:
        print(f"Video error: {e}")
        return None

st.set_page_config(page_icon="🎬" ,page_title="Movie Engine")
st.title("🎬 Movie Engine")

selected_genre = st.selectbox("Genre", options=[''] + list(genre_dict.keys()), index=0)
years = [''] + ["2025","2024","2023","2022","between 2015 to 2020",
              "between 2010 to 2015","between 2000 to 2010","before 2000"]
selected_year = st.selectbox("Release Year", options=years, index=0)
imdb_options = [''] + ["9 and higher","8 and higher","7 and higher","6 and higher","5 and lower"]
selected_imdb = st.selectbox("Minimum Rating", options=imdb_options, index=0)

if st.button("Show Movies"):
    params = {
        'api_key': API_KEY,
        'sort_by': 'vote_average.desc',
        'include_adult': False
    }
    
    
    if selected_genre:
        params['with_genres'] = genre_dict[selected_genre]
    
    params.update(parse_year(selected_year))
    params.update(parse_imdb(selected_imdb))
    
    
    response = requests.get(f"{BASE_URL}/discover/movie", params=params)
    
    if response.status_code == 200:
        
        movies = response.json().get('results', [])
        
        if not movies:
            st.warning("No movies found with the selected criteria!")
        else:
            st.subheader(f"Found {len(movies)} Movies")
            
            for movie in movies[:10]:  
                col1, col2 = st.columns([1, 4])
                poster_url = f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}" if movie.get('poster_path') else None
                video_key=get_video(movie.get("id")) 
                
                
                with col1:
                    if poster_url:
                        st.image(poster_url, width=150)
                       
                    else:
                        st.write("No poster available")
                        
                    if video_key:
                        youtube_url = f"https://www.youtube.com/watch?v={video_key}"
                        st.markdown(f"[▶ Watch Trailer]({youtube_url})")
                
                with col2:
                    st.markdown(f"**{movie.get('title')}** ({movie.get('release_date')[:4] if movie.get('release_date') else 'N/A'})")
                    st.markdown(f"**Rating:** ⭐ {movie.get('vote_average', 'N/A')}")
                    st.markdown(f"**Overview:** {movie.get('overview', 'No description available')}")
                    st.markdown("---")
    else:
        st.error("Error fetching movies. Please try again later.")






