import os
import json
import random
import datetime


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONTENT_API = os.path.join(BASE_DIR, "api_files/content_api.json")


def find_headline_article():
    """
    Finds all the articles in the content_api file with the tag slug='10=promise' and appends into
     a new list. The first artilc in the list is returned when the fuction is called.
    """

    with open(CONTENT_API, "r") as content:
        data = json.load(content)

        matched_articles = []

        for result in data["results"]:
            for tag in result["tags"]:
                if tag["slug"] == "10-promise":
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
                    }

                    matched_articles.append(article)

        return matched_articles[0]


def find_random_three_articles():
    """
    Returns a list of 3 random results (articles) from the provided content_api.json fle.
    """
    with open(CONTENT_API, "r") as content:
        data = json.load(content)

        random_articles = []
        articles = data["results"]

        while len(random_articles) != 3:
            rand = random.choice(articles)
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
            }

            if article not in random_articles:
                random_articles.append(article)

        return random_articles
