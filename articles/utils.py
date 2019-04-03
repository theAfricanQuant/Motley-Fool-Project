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

        matched_articles = []

        for result in data["results"]:
            for tag in result["tags"]:
                if tag["slug"] == "10-promise":
                    uuid = result["uuid"]
                    images = result["images"]
                    title = result["headline"]
                    author = result["byline"]
                    promo = result["promo"]
                    date = datetime.datetime.strptime(result["modified"], "%Y-%m-%dT%H:%M:%SZ")

                    article = {
                        "images": images,
                        "title": title,
                        "author": author,
                        "promo": promo,
                        "modified": date,
                        "uuid": uuid,
                    }

                    matched_articles.append(article)

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

            if article not in random_articles:
                random_articles.append(article)

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

            close_price = rand["ClosePrice"]["Amount"]
            price_change = rand["Change"]["Amount"]
            percentage_change = rand["PercentChange"]["Value"]

            quote = {"close": close_price, "change": price_change, "percent": percentage_change}

            if quote not in random_quotes:
                random_quotes.append(quote)
                print(quote)

        return random_quotes
