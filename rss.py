import feedparser
import re

# https://mikanani.me/RSS/Bangumi?bangumiId=3436

BLOCK_PREFIX = 'https://mikanani.me'
ACCESS_PREFIX = 'https://mikanime.tv'

class RSS:
    def __init__(self, rss_url, title, zmz):
        self.rss_url = rss_url
        self.title = title
        self.zmz = zmz


def parse_rss(rss_url: str):
    if rss_url.startswith(BLOCK_PREFIX):
        rss_url = rss_url.replace(BLOCK_PREFIX, ACCESS_PREFIX)

    feed = feedparser.parse(rss_url) 

    title = resolve_title(feed.feed.title)    
    if not title:
        return None

    zmz = resolve_zimuzu(feed.entries[1].title)
    if not zmz:
        return None

    return RSS(rss_url, title, zmz)


def resolve_title(title):
    match = re.search(r' - (.+)', title)
    if match:
        return match.group(1)
    else:
        return None


def resolve_zimuzu(title):
    match = re.search(r'[\[【](.*?)[\]】]', title)
    if match:
        return match.group(1)
    else:
        return None

if __name__ == '__main__':
    parse_rss('https://mikanani.me/RSS/Bangumi?bangumiId=3436')