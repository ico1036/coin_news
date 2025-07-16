# tests/test_feed_manager.py
import unittest
from src.feed_manager import get_feed_urls

class TestFeedManager(unittest.TestCase):
    def test_get_feed_urls_returns_list(self):
        urls = get_feed_urls()
        self.assertIsInstance(urls, list)
        self.assertGreaterEqual(len(urls), 5)
        self.assertIn("https://cointelegraph.com/rss/tag/altcoin", urls)
        self.assertIn("https://cointelegraph.com/rss", urls)

    def test_fetch_news_from_feed(self):
        from src.feed_manager import fetch_news_from_feed
        url = "https://cointelegraph.com/rss/tag/altcoin"
        news = fetch_news_from_feed(url)
        self.assertIsInstance(news, list)
        if news:  # 피드에 뉴스가 있을 경우
            self.assertIsInstance(news[0], dict)
            self.assertIn("title", news[0])
            self.assertIn("link", news[0])

if __name__ == "__main__":
    unittest.main()
