import requests
from bs4 import BeautifulSoup

from adapters import (
    hackernews_adapter,
    techcrunch_adapter,
    reddit_adapter,
    dailystarnews_adapter,
)
from core.utils import save_data


def get_articles_and_save(url, adapter_class, website_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    adapter = adapter_class(soup)

    articles = adapter.get_articles()

    if articles:
        print(f"Successfully scraped {website_name} page.")
        save_data(articles, website_name)

    return articles


if __name__ == "__main__":
    for i in range(1, 50):
        hackernews_url = f"https://news.ycombinator.com/?p={i}"
        get_articles_and_save(
            hackernews_url, hackernews_adapter.HackerNews, "hackernews"
        )

    for i in range(1, 50):
        tech_crunch_url = f"https://techcrunch.com/category/startups/page/{i}"
        get_articles_and_save(
            tech_crunch_url, techcrunch_adapter.TechCrunch, "techcrunch"
        )

    for i in range(1, 50):
        daily_star_url = f"https://www.thedailystar.net/tech-startup/latest?page={i}"
        get_articles_and_save(
            daily_star_url, dailystarnews_adapter.DailyStarNews, "dailystar"
        )

    reddit_url = "https://www.reddit.com/r/technews/"
    get_articles_and_save(reddit_url, reddit_adapter.RedditNews, "redditnews")