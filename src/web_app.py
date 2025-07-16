# src/web_app.py
from flask import Flask, render_template_string, request, redirect, url_for
from src.news_storage import get_news_for_date
import datetime
from src.feed_manager import get_feed_urls, fetch_news_from_feed
from src.news_storage import save_news_for_date

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def daily_feed():
    today = datetime.date.today().strftime("%Y-%m-%d")
    message = None
    if request.method == "POST":
        all_news = []
        for url in get_feed_urls():
            news = fetch_news_from_feed(url)
            all_news.extend(news)
        unique_news = { (item['title'], item['link']): item for item in all_news }.values()
        save_news_for_date(today, list(unique_news))
        message = f"오늘의 뉴스를 {len(unique_news)}건 수집하여 저장했습니다."
    news_list = get_news_for_date(today)
    template = """
    <html>
    <head>
        <title>오늘의 알트코인 뉴스</title>
        <style>
            body { font-family: sans-serif; background: #f7f7fa; margin: 0; padding: 0; }
            .container { max-width: 700px; margin: 30px auto; background: #fff; border-radius: 10px; box-shadow: 0 2px 8px #0001; padding: 30px; }
            h1 { text-align: center; color: #333; }
            .news-list { list-style: none; padding: 0; }
            .news-card { background: #f2f6ff; margin-bottom: 18px; border-radius: 8px; padding: 18px 20px; box-shadow: 0 1px 3px #0001; }
            .news-title { font-size: 1.1em; font-weight: bold; color: #1a237e; margin-bottom: 6px; }
            .news-link { color: #1976d2; text-decoration: none; }
            .news-summary { color: #444; margin: 8px 0 4px 0; }
            .news-date { color: #888; font-size: 0.95em; }
            .fetch-btn { display: block; margin: 0 auto 20px auto; padding: 10px 30px; background: #1976d2; color: #fff; border: none; border-radius: 6px; font-size: 1em; cursor: pointer; transition: background 0.2s; }
            .fetch-btn:hover { background: #0d47a1; }
            .msg { text-align: center; color: #388e3c; margin-bottom: 18px; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>오늘의 알트코인 뉴스</h1>
            <form method="post">
                <button class="fetch-btn" type="submit">최신 뉴스 수집하기</button>
            </form>
            {% if message %}<div class="msg">{{ message }}</div>{% endif %}
            <ul class="news-list">
            {% for news in news_list %}
                <li class="news-card">
                    <div class="news-title"><a class="news-link" href="{{ news.link }}" target="_blank">{{ news.title }}</a></div>
                    {% if news.summary %}<div class="news-summary">{{ news.summary|safe }}</div>{% endif %}
                    {% if news.published %}<div class="news-date">🕒 {{ news.published }}</div>{% endif %}
                </li>
            {% else %}
                <li style="text-align:center; color:#888;">오늘 뉴스가 없습니다.</li>
            {% endfor %}
            </ul>
        </div>
    </body>
    </html>
    """
    return render_template_string(template, news_list=news_list, message=message)

if __name__ == "__main__":
    app.run(debug=True)
