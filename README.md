# Data Acquisition, Pre-processing, and Data Analysis Pipeline

This pipeline aims to fetch information about programming language popularity on GitHub, preprocess the acquired data, load it into an SQLite database, and perform data analysis to answer questions of interest.
The pipeline is implemented using Python.

## Repository Link

Repository: [https://github.com/20006891/datapipeline](https://github.com/20006891/datapipeline)

## Requirements
- Python 3.x
- Requests library (for making HTTP requests)
- Pandas library (for data manipulation)
- Matplotlib library (for data visualization)
- SQLite (for data storage)

## Pipeline Steps

### 1. Data Acquisition

In the data acquisition step, we fetch repository information from GitHub using the GitHub REST API. 
We make HTTP requests to the API endpoints to retrieve the required data. To access the GitHub API, you need to generate a personal access token from GitHub. 

The GitHub API endpoint we use is:
https://api.github.com/search/repositories?q=stars:>0&per_page=100

- `q=stars:>0` specifies that we want to fetch repositories with at least one star.
- `per_page=100` indicates that we want to retrieve 100 repositories per page.

### 2. Data Pre-processing

After acquiring the repository data, we perform pre-processing to extract relevant features and transform the data as necessary. 
In this example, we extract the repository name, programming language, and star count. 
We use the Pandas library to store the extracted information in a dataframe.

### 3. Data Loading

Once the data is preprocessed, we load it into an SQLite database for further analysis and storage. 
We create a table called "repositories" in the database with columns for the repository name, programming language, and star count. 

### 4. Data Analysis

In the data analysis step, we utilize the preprocessed and loaded data to answer questions of interest. In this example, we answer the following questions:
- Which programming languages are most popular on GitHub?
- How many repositories exist for each language?
- What is the distribution of star counts across different languages?

We use the Pandas library to execute SQL queries on the SQLite database and retrieve the necessary data for analysis. 
Matplotlib is used to create bar charts and box plots to visualize the analysis results.

## Usage

1. Install the required libraries using pip:
   pip install requests pandas matplotlib sqlite3

2. Generate a personal access token from GitHub following the official documentation.

3. Open the Python script `main.py` and replace `'github_pat_token'` in the `fetch_repository_data` function with valid GitHub access token.

4. Run the Python script:
   python main.py

The script will execute the pipeline steps and provide the analysis results in the form of visualizations.

## Conclusion

This pipeline demonstrates a basic workflow for data acquisition, pre-processing, and data analysis using Python. 
By extending and customizing the pipeline, one can apply it to different data sources and answer various questions of interest.

