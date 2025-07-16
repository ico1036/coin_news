# tests/test_news_storage.py
import unittest
import datetime
from src.news_storage import save_news_for_date, get_news_for_date, NEWS_STORAGE

class TestNewsStorage(unittest.TestCase):
    def setUp(self):
        NEWS_STORAGE.clear()

    def test_save_and_get_news_for_date(self):
        today = datetime.date.today().strftime("%Y-%m-%d")
        news = [{"title": "Test News", "link": "#"}]
        save_news_for_date(today, news)
        result = get_news_for_date(today)
        self.assertEqual(result, news)

    def test_rotation_keeps_only_7_days(self):
        base = datetime.date.today()
        for i in range(10):
            d = (base - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
            save_news_for_date(d, [{"title": f"News {i}"}])
        self.assertEqual(len(NEWS_STORAGE), 7)
        # 가장 오래된 날짜는 없어야 함
        oldest = (base - datetime.timedelta(days=9)).strftime("%Y-%m-%d")
        self.assertNotIn(oldest, NEWS_STORAGE)

if __name__ == "__main__":
    unittest.main()
