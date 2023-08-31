from requests import get
from datetime import datetime

def scrape():
    """Scrapes the website and returns all the posts in one chunk."""
    html = get("https://demo200.5mp.eu/web.php?a=demo200&o=yDaKba7PGL").text

    div = "<div style=padding:5;background:white;color:#444444;text-align:left>"
    html = html[html.find(div) + len(div):]
    html = html[:html.find('</div>')]
    return html
    
def parse(html: str, sorted: bool = False):
    """
    Parses the data do a dictionary list:
        >>> {
            author: str
            content: str
            created: datetime
            }
    If `sorted` is set to `True`, the list will be sorted in
    ascending order by creation time.
    """
    html = html.replace("<br>", "").replace("<br />", "")
    
    items = html.split("<hr>")
    items_parsed = []
    for item in items:
        head, content = item.split("</font>")
        author, created = head.split("<font color=#999999>")
        items_parsed.append({
            "author": author[author.find(">") + 1:].strip(),
            "content": content[content.find(">") + 1:].strip(),
            "created": datetime.strptime(created, r"[ %Y-%m-%d %H:%M ]")
        })
    
    if sorted:
        items_parsed.sort(key=lambda item:item["created"])
    return items_parsed