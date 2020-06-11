from django.db import models


class VideoIndexItem(models.Model):
    name = models.CharField('影片名称', max_length=70, default='')
    type = models.CharField('影片类别', max_length=30, default='')
    time = models.CharField('更新时间', max_length=30, default='')
    URL = models.CharField('链接', max_length=30, default='')


class VideoPlayItem(models.Model):
    name = models.CharField('集数', max_length=30, default='')
    full_name = models.CharField('集数', max_length=50, default='')
    http = models.CharField('影片链接', max_length=50, default='')


class VideoDetailItem(models.Model):
    name = models.CharField('影片名称', max_length=70, default='')
    HD_type = models.CharField('集数', max_length=30, default='')  # 高清，集数等
    alias = models.CharField('别名', max_length=70, default='')
    img = models.CharField('封面链接', max_length=30, default='')
    director = models.CharField('导演', max_length=70, default='')
    leading_star = models.CharField('主演', max_length=70, default='')
    type = models.CharField('类型', max_length=70, default='')
    area = models.CharField('地区', max_length=10, default='')
    language = models.CharField('语言', max_length=10, default='')
    video_length = models.CharField('片长', max_length=70, default='0')
    update_time = models.CharField('更新时间', max_length=10, default='')
    story = models.CharField('影片别名', max_length=500, default='没找到简介哦！')
