import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_trending_article_links():
    response = requests.get('https://montrealgazette.com/category/news/')

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get block for trending articles
        trending_block = soup.find('div', class_='top-trending')

        if trending_block:
            # Find blocks containing links
            trending_links = trending_block.find_all('a', class_='article-card__image-link', limit=5)

            full_links = []

            # Loop through the links and construct the full URLs
            for link in trending_links:
                href = link.get('href')
                full_url = urljoin('https://montrealgazette.com', href)
                full_links.append(full_url)

            return full_links
        else:
            print("No element with class 'top-trending' found.")
            return []
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []
    

def parse_article(link):
    response = requests.get(link)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get block for article header
        header_details = soup.find('div', class_='article-header__detail')

        # Title
        article_title = soup.find('h1', attrs={"class":"article-title"}).text

        # Blurb
        blurb = soup.find('p', attrs={"class":"article-subtitle"}).text

        # Author
        author = soup.find('a', attrs={"class":"published-by__author"}).text

        # Date
        date_string = soup.find('span', attrs={"class":"published-date__since"}).text
        _, date = date_string.split(' ', 1)

        info_dict = {
            "title": article_title,
            "publication_date": date,
            "author": author,
            "blurb": blurb
        }


    else:
        print(f"Failed to retrieve the article. Status code: {response.status_code}")
        return []


def get_trending_articles_info():
    article_links = get_trending_article_links()

    articles_info = [parse_article(link) for link in article_links]

    return articles_info