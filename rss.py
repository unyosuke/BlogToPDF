# -*- coding:utf-8 -*-

import feedparser
import requests

RSS_URL = 'http://blog.nogizaka46.com/minami.umezawa/atom.xml'

headers = []
web_page = requests.get(RSS_URL, headers=headers, allow_redirects=True)
content = web_page.content.strip()  # drop the first newline (if any)
feed = feedparser.parse(content)
#print(feed)
for entry in feed.entries:
    print(entry.title)
    print(entry.links[0].href)