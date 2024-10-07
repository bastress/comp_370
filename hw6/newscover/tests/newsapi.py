import unittest
from datetime import datetime, timedelta

import json
import os
import importlib.util


current_dir = os.path.dirname(os.path.abspath(__file__))
newsapi_path = os.path.join(current_dir, '..', 'newsapi.py')
newsapi_path = os.path.abspath(newsapi_path)

test_secrets_path = os.path.join(current_dir, 'test_secrets.json')

spec = importlib.util.spec_from_file_location("newsapi", newsapi_path)
newsapi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(newsapi)


class FetchNewsTestCase(unittest.TestCase):
    def setUp(self):
        with open(test_secrets_path) as f:
            data = json.load(f)
            self.api_key = data['api_key']

    def test_keywords_input(self):
        with self.assertRaises(TypeError):
            newsapi.fetch_latest_news(api_key=self.api_key, lookback_days=5)

    def test_lookback_days(self):
        # Define the lookback days and keywords for the test
        lookback_days = 5
        news_keywords = 'technology'
        
        # Call the fetch_latest_news function
        result = newsapi.fetch_latest_news(api_key=self.api_key, news_keywords=news_keywords, lookback_days=lookback_days)

        # Get the current time and calculate the expected start time
        current_time = datetime.now()
        start_time = current_time - timedelta(days=lookback_days)

        # Check that each article's published date is within the time range
        for article in result['articles']:
            published_date = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            self.assertTrue(start_time <= published_date <= current_time, 
                            f"Article published on {published_date} is outside the expected time range of {start_time} to {current_time}.")

    def test_invalid_keyword(self):
        news_keywords = 'tech@2024'  # Invalid keyword with non-alphabetic characters
        lookback_days = 5

        with self.assertRaises(ValueError) as context:
            newsapi.fetch_latest_news(api_key=self.api_key, news_keywords=news_keywords, lookback_days=lookback_days)

        self.assertEqual(str(context.exception), "Keyword should contain only alphabetic characters")


if __name__=="__main__":
    unittest.main()