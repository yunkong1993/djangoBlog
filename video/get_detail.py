import urllib.request
import urllib.parse
from .models import VideoDetailItem, VideoPlayItem
from lxml import etree
import re
from .AES import AesCrypto,encrypt_string
import json


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
    print(names)
    print(https)
    # pc = AesCrypto(key=b"keyskeyskeyskeyskeyskeyskeyskeys", IV=b"keyskeyskeyskeys")
    for name, http in zip(names, https):
        video_play = VideoPlayItem()
        pattern = re.compile(r'^.*\$')
        video_play.name = re.match(pattern, name).group(0)[0:-1]
        # video_play.http = pc.encrypt(http.decode())
        video_play.http = encrypt_string(json.dumps(http))
        video_items.append(video_play)
    return item, video_items
