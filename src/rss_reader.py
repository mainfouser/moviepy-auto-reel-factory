"""
MARF RSS Reader
Reads articles from RSS feeds.
"""

from __future__ import annotations

import feedparser

from src.config import RSS


class RSSReader:
    def __init__(self):
        self.feed_url = RSS.get("url", "")

    def fetch(self):
        """
        Fetch RSS feed.
        """
        if not self.feed_url:
            raise ValueError("RSS feed URL is empty.")

        feed = feedparser.parse(self.feed_url)

        if feed.bozo:
            raise RuntimeError("Invalid RSS feed.")

        return feed.entries

    def latest(self):
        """
        Return latest article.
        """
        entries = self.fetch()

        if not entries:
            return None

        item = entries[0]

        return {
            "title": item.get("title", ""),
            "link": item.get("link", ""),
            "summary": item.get("summary", ""),
            "published": item.get("published", ""),
        }


if __name__ == "__main__":
    reader = RSSReader()
    article = reader.latest()

    if article:
        print("Latest Article")
        print(article["title"])
        print(article["link"])
    else:
        print("No articles found.")
