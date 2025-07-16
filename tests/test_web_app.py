# tests/test_web_app.py
import unittest
import datetime
from src.web_app import app
from src.news_storage import NEWS_STORAGE

class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        NEWS_STORAGE.clear()
        today = datetime.date.today().strftime("%Y-%m-%d")
        NEWS_STORAGE[today] = [
            {"title": "Test Web News", "link": "#", "published": "", "summary": ""}
        ]

    def test_daily_feed_renders_news(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Web News", response.data)

if __name__ == "__main__":
    unittest.main()
