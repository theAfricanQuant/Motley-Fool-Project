import os
import json
import random
import datetime


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONTENT_API = os.path.join(BASE_DIR, "api_files/content_api.json")
QUOTES_API = os.path.join(BASE_DIR, "api_files/quotes_api.json")


def find_headline_article():
    """
    Finds all the articles in the content_api file with the tag slug='10=promise' and appends into
     a new list. The first artilc in the list is returned when the fuction is called.
    """

    with open(CONTENT_API, "r", encoding="utf8") as content:
        data = json.load(content)

        # Empty list for articles with slug=10-promise to be stored
        matched_articles = []

        # Loop through the articles in the content_api file
        for result in data["results"]:
            # Search thorugh articles that have multiple tags
            for tag in result["tags"]:
                # Find matching slug
                if tag["slug"] == "msn":
                    uuid = result["uuid"]
                    images = result["images"]
                    title = result["headline"]
                    author = result["byline"]
                    promo = result["promo"]
                    date = datetime.datetime.strptime(result["modified"], "%Y-%m-%dT%H:%M:%SZ")

                    # Add the useful properties for each article into a dictionary
                    article = {
                        "images": images,
                        "title": title,
                        "author": author,
                        "promo": promo,
                        "modified": date,
                        "uuid": uuid,
                    }

                    # Append the created dictionary into the list declared above
                    matched_articles.append(article)

        # Returns the first item of the list only
        return matched_articles[0]


def find_random_three_articles():
    """
    Returns a list of 3 random results (articles) from the provided content_api.json fle.
    """
    with open(CONTENT_API, "r", encoding="utf8") as content:
        data = json.load(content)

        random_articles = []
        articles = data["results"]

        while len(random_articles) != 3:
            rand = random.choice(articles)

            uuid = rand["uuid"]
            images = rand["images"]
            title = rand["headline"]
            author = rand["byline"]
            promo = rand["promo"]
            date = datetime.datetime.strptime(rand["modified"], "%Y-%m-%dT%H:%M:%SZ")

            article = {
                "images": images,
                "title": title,
                "author": author,
                "promo": promo,
                "modified": date,
                "uuid": uuid,
            }

            # Check to make sure the article isn't alredy in the list
            if article not in random_articles:
                random_articles.append(article)

        # Returns the list of 3 articles
        return random_articles


def fetch_single_article(uuid):
    """
    Fetches a single article from the content_api by UUID
    """
    with open(CONTENT_API, "r", encoding="utf8") as content:
        data = json.load(content)

        for article in data["results"]:
            if article["uuid"] == uuid:
                return article


def find_three_random_quotes():
    """
    Returns a list of 3 random results (quotes) from the provided quotes_api.json fle and exracts
    the three metrics needed for display on the site. Each quote is returned as a dictionary.
    """
    with open(QUOTES_API, "r", encoding="utf8") as quotes:
        data = json.load(quotes)

        random_quotes = []

        while len(random_quotes) != 3:
            rand = random.choice(data)

            name = rand["CompanyName"]
            exchange = rand["ExchangeName"]
            close_price = rand["ClosePrice"]["Amount"]
            price_change = rand["Change"]["Amount"]
            percentage_change = rand["PercentChange"]["Value"]
            description = rand["Description"]

            # Create a dictionary of needed values per quote
            quote = {
                "close": close_price,
                "change": price_change,
                "percent": percentage_change,
                "name": name,
                "exchange": exchange,
                "description": description
            }

            # Check to make sure the quote isn't alredy in the list
            if quote not in random_quotes:
                random_quotes.append(quote)

        # Returns 3 random quotes in a list
        return random_quotes
