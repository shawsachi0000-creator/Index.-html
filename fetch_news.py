import json, hashlib, html, re
from datetime import datetime, timezone
import feedparser

FEEDS = {
"Bengal":"https://news.google.com/rss/search?q=Bengal+West+Bengal+India&hl=en-IN&gl=IN&ceid=IN:en",
"India":"https://news.google.com/rss/search?q=India+news&hl=en-IN&gl=IN&ceid=IN:en",
"Politics":"https://news.google.com/rss/search?q=India+politics&hl=en-IN&gl=IN&ceid=IN:en",
"World":"https://news.google.com/rss/search?q=World+news&hl=en-IN&gl=IN&ceid=IN:en",
"Business":"https://news.google.com/rss/search?q=India+business&hl=en-IN&gl=IN&ceid=IN:en",
"Sports":"https://news.google.com/rss/search?q=India+sports&hl=en-IN&gl=IN&ceid=IN:en",
"Education":"https://news.google.com/rss/search?q=India+education&hl=en-IN&gl=IN&ceid=IN:en",
"Technology":"https://news.google.com/rss/search?q=India+technology&hl=en-IN&gl=IN&ceid=IN:en",
"Entertainment":"https://news.google.com/rss/search?q=India+entertainment&hl=en-IN&gl=IN&ceid=IN:en"
}
DEFAULT_IMAGE="https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&w=1200&q=80"

def clean(v):
    return re.sub(r"<[^>]+>"," ",html.unescape(v or "")).strip()

items=[]
for category,url in FEEDS.items():
    feed=feedparser.parse(url)
    for e in feed.entries[:20]:
        title=clean(e.get("title","Latest News"))
        if not title: continue
        link=e.get("link","#")
        date=e.get("published",e.get("updated",""))
        try:
            dt=datetime(*e.published_parsed[:6],tzinfo=timezone.utc).isoformat()
        except Exception:
            dt=datetime.now(timezone.utc).isoformat()
        desc=clean(e.get("summary",""))[:400]
        source=clean(e.get("source",{}).get("title","News")) if isinstance(e.get("source"),dict) else "News"
        ident=hashlib.sha1((category+"|"+title+"|"+link).encode()).hexdigest()[:16]
        items.append({"id":ident,"title":title,"description":desc,"link":link,"date":dt,"source":source,"category":category,"image":DEFAULT_IMAGE})
items.sort(key=lambda x:x["date"],reverse=True)
json.dump({"updated_at":datetime.now(timezone.utc).isoformat(),"items":items[:120]},open("news.json","w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("Wrote",len(items[:120]),"news items")

