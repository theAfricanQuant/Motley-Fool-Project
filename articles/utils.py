import os
import json
import random


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
                    matched_articles.append(result)

        return matched_articles[0]


def find_random_three_articles():
    """
    Returns a list of 3 random results (articles) from the provided content_api.json fle.
    """
    with open(CONTENT_API, "r") as content:
        data = json.load(content)

        random_articles = []
        articles = data['results']

        while len(random_articles) != 3:
            rand = random.choice(articles)
            if rand not in random_articles:
                random_articles.append(rand)

        return random_articles

