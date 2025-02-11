```markdown
# 🎬 Movie Engine

A Streamlit web application that helps you discover movies based on genre, release year, and IMDb rating using the TMDB API.

![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)

## Features

- **Genre Filtering**: Choose from 20+ movie genres (Action, Comedy, Horror, etc.)
- **Release Year Range**: Filter by specific year or custom ranges like "2015-2020"
- **IMDb-style Ratings**: Find movies rated 5⭐ to 9⭐ and above
- **Rich Movie Details**:
  - Movie posters
  - YouTube trailers
  - Ratings
  - Release years
  - Plot summaries
- **Responsive Design**: Mobile-friendly interface

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KaanSezen1923/movie-engine.git
   cd movie-engine
   ```

2. Create & activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Get a free [TMDB API Key](https://www.themoviedb.org/settings/api)
2. Create `.env` file in root directory:
   ```env
   TMDB_API_KEY=your_api_key_here
   ```

## Usage

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Use the interactive filters:
   - Select your preferred genre
   - Choose release year range
   - Set minimum rating threshold

3. Click "Show Movies" to see results:
   - View movie posters
   - Watch trailers directly
   - See ratings and plot summaries

## Technologies

- Python 3
- Streamlit (Frontend)
- TMDB API (Movie Data)
- Requests (API Calls)
- Python-dotenv (Environment Management)

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- Movie data provided by [The Movie Database (TMDB)](https://www.themoviedb.org/)
- Streamlit for interactive web components
```

This README features:
- Clear installation instructions with code blocks
- Visual badges for Streamlit
- Organized sections for easy navigation
- Mobile-friendly design notation
- API credit requirements compliance
- Environment setup guidance
- License and attribution details

Would you like me to add any specific sections or modify any existing content?
