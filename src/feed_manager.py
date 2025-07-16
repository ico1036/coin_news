# src/feed_manager.py

# Cointelegraph 주요 RSS 피드 주소 상수 정의
FEED_URLS = [
    "https://cointelegraph.com/rss",
    "https://cointelegraph.com/rss/tag/altcoin",
    "https://cointelegraph.com/rss/tag/bitcoin",
    "https://cointelegraph.com/rss/tag/blockchain",
    "https://cointelegraph.com/rss/tag/ethereum",
    "https://cointelegraph.com/rss/tag/litecoin",
    "https://cointelegraph.com/rss/tag/monero",
    "https://cointelegraph.com/rss/tag/regulation",
    "https://cointelegraph.com/rss/category/analysis",
    "https://cointelegraph.com/rss/category/market-analysis",
    "https://cointelegraph.com/rss/category/weekly-overview",
]

import feedparser

def get_feed_urls():
    """
    등록된 RSS 피드 주소 리스트를 반환합니다.
    """
    return FEED_URLS

def fetch_news_from_feed(url):
    """
    주어진 RSS 피드 URL에서 뉴스 항목 리스트를 파싱하여 반환합니다.
    각 항목은 dict(title, link, published, summary 등) 형태입니다.
    """
    feed = feedparser.parse(url)
    news_items = []
    for entry in feed.entries:
        news_items.append({
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "published": entry.get("published", ""),
            "summary": entry.get("summary", "")
        })
    return news_items
