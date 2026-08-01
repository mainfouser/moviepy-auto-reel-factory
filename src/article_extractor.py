
"""
MARF Article Extractor
"""

from __future__ import annotations


class ArticleExtractor:
    """
    Extract and normalize article data.
    """

    def extract(self, article: dict) -> dict:
        return {
            "title": article.get("title", ""),
            "link": article.get("link", ""),
            "summary": article.get("summary", ""),
            "published": article.get("published", ""),
        }
