# Initial Explorations  
  
We first loaded the data from the Algolia Hacker News Search API into a local DuckDB database. We then filtered this data and ran the GPT-4 API on it and saved the results in a .csv. We finally loaded this .csv into a streamlit dashboard.

## Steps to run it locally
1. Clone this repo.
2. Set up environment and install requirements using `pip install -r requirements.txt`.
3. Run the `dlt` pipeline using `python3 algolia_hn_search_pipeline.py`.
4. This will create a local DuckDB database `algolia_hn_search.duckdb` in the directory.
5. Next run `python3 load_data.py`
6. This will create the file `dashboard_data.csv` in the directory.
7. Finally, launch the streamlit app using `streamlit run dashboard.py`. 