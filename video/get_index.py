import urllib.request
import urllib.parse
from urllib.parse import quote
import string
from .models import VideoIndexItem
from lxml import etree


def get_index_list(q=''):
    # q = '人民'
    pg = 1

    url = "http://www.zuidazy5.com/index.php?m=vod-search-pg-" + str(pg) + "-wd-" + str(q) + ".html"
    url = quote(url, safe=string.printable)
    header = {}
    header[
        "User-Agent"] = r"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3854.3 Safari/537.36"
    req = urllib.request.Request(url)
    req.add_header("User-Agent", header["User-Agent"])
    response = urllib.request.urlopen(req, timeout=15).read()
    doc = etree.HTML(response)
    # total_str = (doc.xpath("//div/dl/dd/span[2]/text()"))[0].strip()
    # total = int(total_str)
    names = doc.xpath("//span[@class='xing_vb4']/a/text()")
    URLs = doc.xpath("//span[@class='xing_vb4']/a/@href")
    types = doc.xpath("//span[@class='xing_vb5']/text()")
    times = doc.xpath("//span[@class='xing_vb6']/text()")
    items = []
    for name, URL, type, time in zip(names, URLs, types, times):
        item = VideoIndexItem()
        item.name = name
        item.URL = URL
        item.type = type
        item.time = time
        items.append(item)
        print(item)
    return items
