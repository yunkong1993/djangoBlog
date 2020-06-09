from django.test import TestCase

# Create your tests here.


import os
import lxml
from urllib.request import urlopen  # Mac
# from urllib.request import Request, urlopen # Win
from lxml import etree

hfile = urlopen('http://www.zuidazy5.com/index.php?m=vod-search').read()
tree = etree.HTML(hfile)
strs = tree.xpath("/html/body/div[5]/ul/li")
strs = strs[0]
# strs = (etree.tostring(strs)) # 不能正常显示中文
strs = (etree.tostring(strs, encoding="utf-8", pretty_print=True, method="html")).decode()  # 可以正常显示中文
print(strs)
