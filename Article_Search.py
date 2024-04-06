#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Test')


# # Import Modules

# In[47]:


# Import Modules
import requests
import spacy
import pandas as pd
from datetime import datetime, timedelta
import requests    
import os
import unittest
from unittest.mock import patch, Mock


# # Search Engine

# In[48]:


def fetch_news(topic, language):
    """
    Fetches news articles related to a specific topic and language from the past 30 days.
    
    This function queries the NewsAPI to retrieve news articles based on the given topic and language. 
    It returns a list of tuples containing the title, URL, and publication date of each article.

    Parameters:
    - topic (str): The topic of interest for fetching news articles.
    - language (str): The language of the news articles. Uses ISO 639-1 codes (e.g., "en" for English, "de" for German).

    Returns:
    - list of tuples: Each tuple contains (title, url, publishedAt) for each article.
    """

    API_KEY = os.getenv('NEWSAPI_KEY')
    if API_KEY is None:
        raise ValueError("Please set the NEWSAPI_KEY in environment variables.")
    
    # Calculate the start date for fetching articles from 30 days ago to ensure recency.
    date_from = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    
    # Construct the API request URL with parameters for topic, language, API key, sorting by publication date,
    # and filtering articles from the last 30 days for recency.
    url = (f"https://newsapi.org/v2/everything?q={topic}"
           f"&language={language}"
           f"&apiKey={API_KEY}"
           f"&sortBy=publishedAt"  # Ensures articles are sorted by publication date.
           f"&from={date_from}")    # Filters articles to those published within the last 30 days.

    # Perform the GET request to fetch the news articles.
    response = requests.get(url)
    
    # Extract the 'articles' field from the JSON response.
    articles = response.json()['articles']
    
    # Return a list of tuples containing the title, URL, and publication date for each article.
    return [(article['title'], article['url'], article['publishedAt']) for article in articles]


# In[49]:


def process_headlines(headlines):
    """
    Processes a list of news headlines to summarize and identify key entities.
    
    This function uses the spaCy NLP library to analyze each headline, extracting text and recognized entities.
    It summarizes the headlines and tallies the occurrence of each unique entity across all headlines, 
    returning a list of headlines and a sorted list of entities based on their frequency.

    Parameters:
    - headlines (list of str): A list of news headlines to be processed.

    Returns:
    - tuple of (list, list): The first list contains the original headlines. The second list contains tuples 
      of entities and their frequency, sorted in descending order of frequency.
    """

    # Load the English spaCy model. This needs to be loaded outside the function in actual usage.
    nlp = spacy.load("en_core_web_sm")

    summaries = []  # List to store the original headlines for summary
    entity_dict = {}  # Dictionary to count the occurrence of each entity

    # Process each headline to extract text and entities
    for headline in headlines:
        doc = nlp(headline)  # Analyze the headline using spaCy
        summaries.append(doc.text)  # Append the original headline text to summaries
        for ent in doc.ents:  # Loop through the identified entities in the headline
            # Increment the count for each entity found
            entity_dict[ent.text] = entity_dict.get(ent.text, 0) + 1
    
    # Sort the entities by their frequency in descending order
    sorted_entities = sorted(entity_dict.items(), key=lambda x: x[1], reverse=True)

    return summaries, sorted_entities  # Return the summaries and sorted entities


# In[50]:


def save_to_csv(articles, filename='news_articles.csv'):
    """
    Saves a list of articles to a CSV file.
    
    This function takes a list of articles, where each article is represented as a tuple or list 
    containing the title, URL, and publication date. It then creates a DataFrame from this list and 
    saves it to a CSV file with the specified filename.

    Parameters:
    - articles (list of tuple/list): The articles to save, where each article should have 
      the structure (title, URL, publication date).
    - filename (str, optional): The name of the file to save the articles to. 
      Defaults to 'news_articles.csv'.
    """

    # Create a DataFrame from the articles list with specified column names.
    df = pd.DataFrame(articles, columns=['Title', 'URL', 'PublishedAt'])
    # Save the DataFrame to a CSV file, without including the index.
    df.to_csv(filename, index=False)

def display_results(articles, summaries, entities):
    """
    Displays the results of processed articles, including the top articles, summaries, and named entities.
    
    This function prints the title, URL, and publication date of the first 15 articles, 
    followed by a summary of the first 15 headlines, and finally the named entities identified 
    in the articles, sorted by their frequency of occurrence.

    Parameters:
    - articles (list of tuple/list): Articles with their title, URL, and publication date.
    - summaries (list of str): Summaries of the articles/headlines.
    - entities (list of tuple): Named entities found in the articles, along with their frequencies, 
      sorted by frequency.
    """

    # Display the first 15 articles' titles, URLs, and publication dates.
    for article in articles[:15]:
        print(f"Title: {article[0]} \nURL: {article[1]} \nDate: {article[2]}\n")
        print('---------------------------------------------------------------------------')

    # Print summaries of the first 15 headlines/articles.
    print("\nSummary of headlines:\n")
    for summary in summaries[:15]:
        print(f'- {summary}')
    print("\nNamed Entities (sorted by frequency):\n", entities, sep='\n')


# In[52]:


def main():
    """
    Main function to drive the news articles fetching, processing, and display based on user input.
    
    This interactive script prompts the user to enter a topic and preferred language (English or German) 
    to search for relevant news articles. It utilizes the `fetch_news`, `process_headlines`, 
    `display_results`, and `save_to_csv` functions to fetch, process, display, and save news articles 
    related to the entered topic. The script runs in a loop until the user decides to exit by typing 'exit'.
    """
    
    while True:
        # Prompt user for a topic to search.
        topic = input("Enter a topic to search for (or type 'exit' to quit): ")
        if topic.lower() == 'exit':  # Exit condition check.
            break

        # Prompt for language preference with validation for English or German.
        language = input('Which language do you prefer? English or German: ').lower()
        if language not in ["english", "en", "de", "deutsch", 'german']:
            print("Invalid language selection. Please enter 'English' or 'German'.")
            continue  # Restart loop on invalid input.

        # Assigning the correct language code for the API call.
        lang_code = "en" if language in ["english", "en"] else "de"
        
        # Fetch news articles based on the topic and language.
        articles = fetch_news(topic, lang_code)
        if not articles:  # Check if the fetch_news function returned an empty list.
            print(f"No articles found for topic '{topic}' in {language.title()}.")
            continue

        # Extract headlines from articles for further processing.
        headlines = [article[0] for article in articles]
        # Process headlines to summarize and identify key entities.
        summaries, named_entities = process_headlines(headlines)
        # Display the results to the user.
        display_results(articles, summaries, named_entities)
        # Save the articles to a CSV file.
        save_to_csv(articles)

# Ensures this script block runs only if the script is executed as the main program.
if __name__ == "__main__":
    main()


# # Unit-testing of the Search Engine

# In[55]:


class TestFetchNews(unittest.TestCase):
    # Using the patch decorator to mock 'requests.get' calls within the scope of the test method.
    @patch('__main__.requests.get')
    def test_fetch_news(self, mock_get):
        # Setup a mock response object to simulate a successful API call with a JSON payload.
        # This mock response returns a predefined JSON structure when its .json() method is called.
        mock_response = Mock()
        mock_response.json.return_value = {
            'articles': [
                {'title': 'Test Article 1', 'url': 'http://testurl.com/1', 'publishedAt': '2024-04-01T00:00:00Z'},
                {'title': 'Test Article 2', 'url': 'http://testurl.com/2', 'publishedAt': '2024-04-02T00:00:00Z1'}
            ]
        }
        # Assign the mock response to the mock object that replaces 'requests.get'.
        mock_get.return_value = mock_response
        
        # Call the function under test with predefined parameters.
        topic = 'test'
        lang_code = 'en'
        articles = fetch_news(topic, lang_code)
        
        # Assertions to verify the behavior of 'fetch_news'.
        # Check if the function returns a list.
        self.assertIsInstance(articles, list)
        # Check if the returned list length matches the expected number of articles.
        self.assertEqual(len(articles), 2)
        # Verify that a specific article is present in the returned list, indicating correct parsing and handling.
        self.assertIn(('Test Article 1', 'http://testurl.com/1', '2024-04-01T00:00:00Z'), articles)

    # A second test case to simulate a scenario where the function does not behave as expected.
    @patch('__main__.requests.get')
    def test_fetch_news_failure(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            'articles': [
                {'title': 'Test Article 3', 'url': 'http://testurl.com/3', 'publishedAt': '2024-04-03T00:00:00Z'}
            ]
        }
        mock_get.return_value = mock_response
        
        # Call the function under test with the same parameters as the previous case.
        articles = fetch_news('test', 'en')
        
        # An assertion that is designed to fail based on the mock setup, to demonstrate handling of failed conditions.
        # This checks if the function returns a number of articles different from the expected, which in this setup,
        # it will, thereby causing this test to fail as designed.
        self.assertEqual(len(articles), 2, "Expected to find 2 articles")


# In[56]:


# Running the tests
def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestFetchNews))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)
run_tests()

