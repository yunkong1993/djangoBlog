import urllib.request
import urllib.parse
from .models import VideoDetailItem, VideoPlayItem
from lxml import etree
import re
from .AES import AesCrypto
from django.conf import settings
from .sites_list import sites_tuple
import ssl


def get_detail(i=0, m=''):
    site = sites_tuple[int(i)]
    url = site['view'].format(m=m)
    header = {
        "User-Agent": r"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3854.3 Safari/537.36"}
    ssl._create_default_https_context = ssl._create_unverified_context
    req = urllib.request.Request(url)
    req.add_header("User-Agent", header["User-Agent"])
    response = urllib.request.urlopen(req, timeout=15).read()
    doc = etree.HTML(response)
    item = VideoDetailItem()
    try:
        if doc.xpath(site['name_xpath']):
            item.name = doc.xpath(site['name_xpath'])[0]
        if doc.xpath(site['HD_type_xpath']):
            item.HD_type = doc.xpath(site['HD_type_xpath'])[0]  # 高清，集数等
        if doc.xpath(site['alias_xpath']):
            item.alias = doc.xpath(site['alias_xpath'])[0]
        if doc.xpath(site['img_xpath']):
            item.img = doc.xpath(site['img_xpath'])[0]
        if doc.xpath(site['director_xpath']):
            item.director = doc.xpath(site['director_xpath'])[0]
        if doc.xpath(site['leading_star_xpath']):
            item.leading_star = doc.xpath(site['leading_star_xpath'])[0]
        if doc.xpath(site['type_xpath']):
            item.type = doc.xpath(site['type_xpath'])[0]
        if doc.xpath(site['area_xpath']):
            item.area = doc.xpath(site['area_xpath'])[0]
        if doc.xpath(site['language_xpath']):
            item.language = doc.xpath(site['language_xpath'])[0]
        if doc.xpath(site['video_length_xpath']):
            item.video_length = doc.xpath(site['video_length_xpath'])[0]
        if doc.xpath(site['update_time_xpath']):
            item.update_time = doc.xpath(site['update_time_xpath'])[0]
        if doc.xpath(site['story_xpath']):
            item.story = doc.xpath(site['story_xpath'])[0]
        print(item.story)
        print("***"*30)
    except IndexError:
        pass
    video_items = []
    names = doc.xpath(site['names_xpath'])
    https = doc.xpath(site['https_xpath'])
    video_name = doc.xpath(site['video_name_xpath'])
    if len(names) == 0 or len(https) == 0:
        names = doc.xpath(site['names_xpath'])
        https = doc.xpath(site['https_xpath'])
    for name, http_url in zip(names, https):
        video_play = VideoPlayItem()
        pattern = re.compile(r'^.*\$')
        video_play.name = re.match(pattern, name).group(0)[0:-1]
        my_crypt = AesCrypto(bytes(settings.AES_KEY, encoding='utf-8'))
        http_bytes = my_crypt.encrypt(http_url)
        video_play.http = str(http_bytes, encoding="utf8")
        full_name = video_name[0] + '  ' + video_play.name
        video_play.full_name = str(my_crypt.encrypt(full_name), encoding="utf8")
        video_items.append(video_play)
    return item, video_items
