import urllib.request
import urllib.parse
from .models import VideoDetailItem, VideoPlayItem
from lxml import etree
import re
from .AES import AesCrypto
from django.conf import settings


def get_detail(url=''):
    url1 = "http://www.zuidazy5.com/?m=" + url
    header = {}
    header[
        "User-Agent"] = r"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3854.3 Safari/537.36"
    req = urllib.request.Request(url1)
    req.add_header("User-Agent", header["User-Agent"])
    response = urllib.request.urlopen(req, timeout=15).read()
    doc = etree.HTML(response)
    item = VideoDetailItem()
    try:
        if doc.xpath("//div[2]/div[1]/h2/text()"):
            item.name = doc.xpath("//div[2]/div[1]/h2/text()")[0]
        if doc.xpath("//div[2]/div[1]/span/text()"):
            item.HD_type = doc.xpath("//div[2]/div[1]/span/text()")[0]  # 高清，集数等
        if doc.xpath("//div[2]/div[2]/ul/li[1]/span/text()"):
            item.alias = doc.xpath("//div[2]/div[2]/ul/li[1]/span/text()")[0]
        if doc.xpath("//div[1]/div/div/div[1]/img/@src"):
            item.img = doc.xpath("//div[1]/div/div/div[1]/img/@src")[0]
        if doc.xpath("//div[2]/div[2]/ul/li[2]/span/text()"):
            item.director = doc.xpath("//div[2]/div[2]/ul/li[2]/span/text()")[0]
        if doc.xpath("//div[2]/div[2]/ul/li[3]/span/text()"):
            item.leading_star = doc.xpath("//div[2]/div[2]/ul/li[3]/span/text()")[0]
        if doc.xpath("//div[2]/div[2]/ul/li[4]/span/text()"):
            item.type = doc.xpath("//div[2]/div[2]/ul/li[4]/span/text()")[0]
        if doc.xpath("//div[2]/div[2]/ul/li[5]/span/text()"):
            item.area = doc.xpath("//div[2]/div[2]/ul/li[5]/span/text()")[0]
        if doc.xpath("//div[2]/div[2]/ul/li[6]/span/text()"):
            item.language = doc.xpath("//div[2]/div[2]/ul/li[6]/span/text()")[0]
        if doc.xpath("//div[2]/div[2]/ul/li[8]/span/text()"):
            item.video_length = doc.xpath("//div[2]/div[2]/ul/li[8]/span/text()")[0]
        if doc.xpath("//div[2]/div[2]/ul/li[9]/span/text()"):
            item.update_time = doc.xpath("//div[2]/div[2]/ul/li[9]/span/text()")[0]
        if doc.xpath("//div[2]/div[2]/ul/li[14]/div/span[2]/text()"):
            item.story = doc.xpath("//div[2]/div[2]/ul/li[14]/div/span[2]/text()")[0]
    except IndexError:
        pass
    video_items = []
    names = doc.xpath("//*[@id='down_1']/ul/li/text()")
    https = doc.xpath("//*[@id='down_1']/ul/li/input/@value")
    if len(names) == 0 or len(https) == 0:
        names = doc.xpath("//*[@id='play_1']/ul/li/text()")
        https = doc.xpath("//*[@id='play_1']/ul/li/input/@value")
    for name, http_url in zip(names, https):
        video_play = VideoPlayItem()
        pattern = re.compile(r'^.*\$')
        video_play.name = re.match(pattern, name).group(0)[0:-1]
        my_crypt = AesCrypto(bytes(settings.AES_KEY, encoding='utf-8'))
        http_bytes = my_crypt.encrypt(http_url)
        video_play.http = str(http_bytes, encoding="utf8")
        video_items.append(video_play)
    return item, video_items