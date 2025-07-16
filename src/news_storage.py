# src/news_storage.py
import datetime
from typing import List, Dict

# 뉴스 저장소 (메모리 기반, 실제 구현은 테스트 후)
NEWS_STORAGE = {}


def save_news_for_date(date: str, news_list: List[Dict]):
    NEWS_STORAGE[date] = news_list
    # 7일치만 유지
    if len(NEWS_STORAGE) > 7:
        # 오래된 날짜부터 삭제
        for old_date in sorted(NEWS_STORAGE.keys()):
            if len(NEWS_STORAGE) <= 7:
                break
            del NEWS_STORAGE[old_date]


def get_news_for_date(date: str) -> List[Dict]:
    return NEWS_STORAGE.get(date, [])
