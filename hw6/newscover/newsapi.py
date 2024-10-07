from newsapi import NewsApiClient
from datetime import datetime, timedelta
import re



def fetch_latest_news(api_key, news_keywords, lookback_days=10):

    if not re.match(r'^[a-zA-Z\s]+$', news_keywords):
        raise ValueError("Keyword should contain only alphabetic characters")

    newsapi = NewsApiClient(api_key=api_key)

    current_time = datetime.now()

    # Calculate the date 'lookback_days' ago
    start_time = current_time - timedelta(days=lookback_days)

    # Format the dates
    current_day_str = current_time.strftime('%Y-%m-%dT%H:%M:%S')
    start_day_str = start_time.strftime('%Y-%m-%dT%H:%M:%S')

    all_articles = newsapi.get_everything(q=news_keywords,
                                      from_param=start_day_str,
                                      to=current_day_str,
                                      language='en')

    return all_articles
