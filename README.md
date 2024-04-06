# Article Search Engine - Riswan Basha Saleem Basha
## Overview
This Python application searches for recent news articles on a user-defined topic and outputs the top-15 relevant articles. It provides summaries and named entities from the article headlines and saves all search results to a CSV file.

## Installation

1. **Clone the Repository**
   ```bash
   https://github.com/RiswanBasha/Search_Engine.git
   cd ArticleSearchEngine
   ```
2. **Set Up a Virtual Environment**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
   or
    ```
   conda create --name myenv python=3.8
   conda activate myenv
   ```
3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```
4. **Environment Variables**
   set the NEWSAPI_KEY in your environmental variables which you can find here [newsapi](https://newsapi.org/docs).
   1. Go to the link,
   2. Register your account
   3. Get API Key for free
5. **Run the Application**
   Follow the Prompts
   - Enter a search topic.
   - Choose your preferred language (English or German).
   View Results
   - Check the console for the top-15 articles' summaries and named entities.
   - Find a detailed list of all fetched articles in news_articles.csv.
