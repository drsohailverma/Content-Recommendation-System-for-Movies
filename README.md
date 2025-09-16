# Content Recommendation System for Movies using Item Similarity (Content Based)

This repository contains a Google Colab notebook that builds a simple content based movie recommendation system using the TMDB 5000 Movies dataset. It computes similarity between movies from their metadata and returns titles that are most similar to the selected movie.

## Files
- `Movie_Recommendation_.ipynb` — the main notebook.
- Dataset CSV files used by the notebook:
  - `tmdb_5000_movies.csv`
  - `tmdb_5000_credits.csv`
  
If your dataset files have different names, update the paths in the notebook or rename the files to match what the notebook expects.

## Quick start in Google Colab
1. Open Google Colab: https://colab.research.google.com/
2. Click **Connect** on the top right if it is not already connected to Google Compute Engine.
3. Go to **File** → **Upload notebook** and upload `Movie_Recommendation_.ipynb`. Do not run any cells yet.
4. Open the **Files** pane by clicking the **Folder** icon on the left.
5. Click **Upload to session storage** and select both dataset CSV files. You can also drag and drop the CSV files into the Files pane.
6. If a warning appears, click **OK** and wait until both CSV files finish uploading and are visible in the Files pane.
7. Click **Runtime** → **Run all** and wait for the notebook to complete execution.

## Verify output
- Scroll to **Cell 71**. By default, the code uses a title such as **Autumn in New York** and prints similar movies below it.
- Replace the movie title with **Titanic** and run **Cell 71** again. It should now show movies similar to Titanic.
- Pick any other title from `tmdb_5000_movies.csv`, update **Cell 71**, and run that cell again to see updated recommendations.

## How it works
- Loads and cleans metadata from TMDB CSV files. Typical fields include overview, genres, keywords, cast, and crew.
- Builds a combined text representation (often called a "tags" column) for each movie.
- Converts text to numeric vectors using a simple bag of words approach.
- Computes cosine similarity between movies.
- Returns the top N most similar titles for a given input movie.

## Requirements
The notebook is designed to run in Google Colab. No local setup is required. If you prefer to run locally, install the usual Python stack:
- Python 3.9 or later
- pandas, numpy, scikit-learn, nltk

You may need to download NLTK resources the first time you run locally.

## Project structure
```
.
├─ Movie_Recommendation_.ipynb
├─ tmdb_5000_movies.csv
└─ tmdb_5000_credits.csv
```
Note: in Colab, these files live in session storage and are temporary. A runtime reset clears them.

## Troubleshooting
- **FileNotFoundError**: confirm that both CSVs are uploaded to the Colab session and the filenames match those used in the notebook.
- **KeyError on movie title**: make sure the title exists in `tmdb_5000_movies.csv` and matches exactly.
- **Session reset**: if the runtime restarts, reupload the dataset files before running the notebook again.
- **Module not found**: if a dependency error appears when running locally, install the missing package and rerun the notebook.

## Acknowledgments
Data source: TMDB 5000 Movies dataset.
