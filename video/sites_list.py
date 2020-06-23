site1 = \
    {
        'key': 'zuidazy',
        'name': '最大资源网',
        'url': 'http://www.zuidazy5.com',
        'new': 'http://www.zuidazy5.com/?m=vod-index-pg-{page}.html',
        'view': 'http://www.zuidazy5.com/?m={m}',
        'search': 'http://www.zuidazy5.com/index.php?m=vod-search-pg-{page}-wd-{keywords}.html',

        'name_xpath': "//div[2]/div[1]/h2/text()",
        'HD_type_xpath': "//div[2]/div[1]/span/text()",  # 高清，集数等
        'alias_xpath': "//div[2]/div[2]/ul/li[1]/span/text()",
        'img_xpath': "//div[1]/div/div/div[1]/img/@src",
        'director_xpath': "//div[2]/div[2]/ul/li[2]/span/text()",
        'leading_star_xpath': "//div[2]/div[2]/ul/li[3]/span/text()",
        'type_xpath': "//div[2]/div[2]/ul/li[4]/span/text()",
        'area_xpath': "//div[2]/div[2]/ul/li[5]/span/text()",
        'language_xpath': "//div[2]/div[2]/ul/li[6]/span/text()",
        'video_length_xpath': "//div[2]/div[2]/ul/li[8]/span/text()",
        'update_time_xpath': "//div[2]/div[2]/ul/li[9]/span/text()",
        'story_xpath': "//div[2]/div[2]/ul/li[14]/div/span[2]/text()",

        'names_xpath': "//*[@id='down_1']/ul/li/text()",
        'https_xpath': "//*[@id='play_1']/ul/li/input/@value",
        'video_name_xpath': "//div[2]/div[1]/h2/text()",

    }

site2 = \
    {
        'key': 'okzy',
        'name': 'OK资源网',
        'url': 'https://www.okzy.co',
        'new': 'https://www.okzy.co/?m=vod-index-pg-{page}.html',
        'view': 'https://www.okzy.co/?m={m}',
        'search': 'https://www.okzy.co/index.php?m=vod-search-pg-{page}-wd-{keywords}.html',

        'name_xpath': "//div[2]/div[1]/h2/text()",
        'HD_type_xpath': "//div[2]/div[1]/span/text()",  # 高清，集数等
        'alias_xpath': "//div[2]/div[2]/ul/li[1]/span/text()",
        'img_xpath': "//div[1]/div/div/div[1]/img/@src",
        'director_xpath': "//div[2]/div[2]/ul/li[2]/span/text()",
        'leading_star_xpath': "//div[2]/div[2]/ul/li[3]/span/text()",
        'type_xpath': "//div[2]/div[2]/ul/li[4]/span/text()",
        'area_xpath': "//div[2]/div[2]/ul/li[5]/span/text()",
        'language_xpath': "//div[2]/div[2]/ul/li[6]/span/text()",
        'video_length_xpath': "//div[2]/div[2]/ul/li[8]/span/text()",
        'update_time_xpath': "//div[2]/div[2]/ul/li[9]/span/text()",
        'story_xpath': "//div[5]/div[2]/div[2]/text()",

        'names_xpath': "//*[@id='down_1']/ul/li/text()",
        'https_xpath': "//*[@id='2']/ul/li/input/@value",
        'video_name_xpath': "//div[2]/div[1]/h2/text()",
    }

site3 = \
    {
        'key': 'subo',
        'name': '速播资源站',
        'url': 'https://www.subo988.com',
        'new': 'https://www.subo988.com/?m=vod-index-pg-{page}.html',
        'view': 'https://www.subo988.com/?m={m}',
        'search': 'https://www.subo988.com/index.php?m=vod-search-pg-{page}-wd-{keywords}.html',
        'name_xpath': "//div[2]/div[1]/h2/text()",
        'HD_type_xpath': "//div[2]/div[1]/span/text()",  # 高清，集数等
        'alias_xpath': "//div[2]/div[2]/ul/li[1]/span/text()",
        'img_xpath': "//div[1]/div/div/div[1]/img/@src",
        'director_xpath': "//div[2]/div[2]/ul/li[2]/span/text()",
        'leading_star_xpath': "//div[2]/div[2]/ul/li[3]/span/text()",
        'type_xpath': "//div[2]/div[2]/ul/li[4]/span/text()",
        'area_xpath': "//div[2]/div[2]/ul/li[5]/span/text()",
        'language_xpath': "//div[2]/div[2]/ul/li[6]/span/text()",
        'video_length_xpath': "//div[2]/div[2]/ul/li[8]/span/text()",
        'update_time_xpath': "//div[2]/div[2]/ul/li[9]/span/text()",
        'story_xpath': "//div[4]/div[3]/div[2]/text()",

        'names_xpath': "//div[4]/div[2]/div/ul[1]/li/text()",
        'https_xpath': "//ul/li/input/@value",
        'video_name_xpath': "//div[2]/div[1]/h2/text()",
    }

site4 = \
    {
        'key': 'mahuazy',
        'name': '麻花资源',
        'url': 'http://www.mahuazy.com',
        'new': 'http://www.mahuazy.com/?m=vod-index-pg-{page}.html',
        'view': 'http://www.mahuazy.com/?m=v{m}',
        'search': 'http://www.mahuazy.com/?m=vod-search-pg-{page}-wd-{keywords}.html',
        'name_xpath': "//div[2]/div[1]/h2/text()",
        'HD_type_xpath': "//div[2]/div[1]/span/text()",  # 高清，集数等
        'alias_xpath': "//div[2]/div[2]/ul/li[1]/span/text()",
        'img_xpath': "//div[1]/div/div/div[1]/img/@src",
        'director_xpath': "//div[2]/div[2]/ul/li[2]/span/text()",
        'leading_star_xpath': "//div[2]/div[2]/ul/li[3]/span/text()",
        'type_xpath': "//div[2]/div[2]/ul/li[4]/span/text()",
        'area_xpath': "//div[2]/div[2]/ul/li[5]/span/text()",
        'language_xpath': "//div[2]/div[2]/ul/li[6]/span/text()",
        'video_length_xpath': "//div[2]/div[2]/ul/li[8]/span/text()",
        'update_time_xpath': "//div[2]/div[2]/ul/li[9]/span/text()",
        'story_xpath': "//div[2]/div[2]/ul/li[14]/div/span[2]/text()",

        'names_xpath': "//*[@id='down_1']/ul/li/text()",
        'https_xpath': "//*[@id='play_1']/ul/li/input/@value",
        'video_name_xpath': "//div[2]/div[1]/h2/text()",
    }

site5 = \
    {
        'key': 'zuixinzy',
        'name': '最新资源网',
        'url': 'http://www.zuixinzy.net',
        'new': 'http://www.zuixinzy.net/?m=vod-index-pg-{page}.html',
        'view': 'http://www.zuixinzy.net/?m={m}',
        'search': 'http://www.zuixinzy.net/index.php?m=vod-search-pg-{page}-wd-{keywords}.html',
        'name_xpath': "//div[2]/div[1]/h2/text()",
        'HD_type_xpath': "//div[2]/div[1]/span/text()",  # 高清，集数等
        'alias_xpath': "//div[2]/div[2]/ul/li[1]/span/text()",
        'img_xpath': "//div[1]/div/div/div[1]/img/@src",
        'director_xpath': "//div[2]/div[2]/ul/li[2]/span/text()",
        'leading_star_xpath': "//div[2]/div[2]/ul/li[3]/span/text()",
        'type_xpath': "//div[2]/div[2]/ul/li[4]/span/text()",
        'area_xpath': "//div[2]/div[2]/ul/li[5]/span/text()",
        'language_xpath': "//div[2]/div[2]/ul/li[6]/span/text()",
        'video_length_xpath': "//div[2]/div[2]/ul/li[8]/span/text()",
        'update_time_xpath': "//div[2]/div[2]/ul/li[9]/span/text()",
        'story_xpath': "//div[2]/div[2]/ul/li[14]/div/span[2]/text()",

        'names_xpath': "//div[3]/font/div/div/ul[1]/li/text()",
        'https_xpath': "//div/div/ul[2]/li/input/@value",
        'video_name_xpath': "//div[2]/div[1]/h2/text()",
    }

site6 = \
    {
        'key': '123ku',
        'name': '123资源网',
        'url': 'https://www.123ku.com',
        'new': 'https://www.123ku.com/?m=vod-index-pg-{page}.html',
        'view': 'https://www.123ku.com/?m={m}',
        'search': 'https://www.123ku.com/index.php?m=vod-search-pg-{page}-wd-{keywords}.html',
        'name_xpath': "//div[2]/div[1]/h2/text()",
        'HD_type_xpath': "//div[2]/div[1]/span/text()",  # 高清，集数等
        'alias_xpath': "//div[2]/div[2]/ul/li[1]/span/text()",
        'img_xpath': "//div[1]/div/div/div[1]/img/@src",
        'director_xpath': "//div[2]/div[2]/ul/li[2]/span/text()",
        'leading_star_xpath': "//div[2]/div[2]/ul/li[3]/span/text()",
        'type_xpath': "//div[2]/div[2]/ul/li[4]/span/text()",
        'area_xpath': "//div[2]/div[2]/ul/li[5]/span/text()",
        'language_xpath': "//div[2]/div[2]/ul/li[6]/span/text()",
        'video_length_xpath': "//div[2]/div[2]/ul/li[8]/span/text()",
        'update_time_xpath': "//div[2]/div[2]/ul/li[9]/span/text()",
        'story_xpath': "//div[2]/div[2]/ul/li[14]/div/span[2]/text()",

        'names_xpath': "//*[@id='down_1']/ul/li/text()",
        'https_xpath': "//*[@id='play_1']/ul/li/input/@value",
        'video_name_xpath': "//div[2]/div[1]/h2/text()",
    }

site7 = \
    {
        'key': '209zy',
        'name': '209资源网',
        'url': 'http://www.209zy.com',
        'new': 'http://www.209zy.com/?m=vod-index-pg-{page}.html',
        'view': 'http://www.209zy.com/?m={m}',
        'search': 'http://www.209zy.com/index.php?m=vod-search-pg-{page}-wd-{keywords}.html',
        'name_xpath': "//div[2]/div[1]/h2/text()",
        'HD_type_xpath': "//div[2]/div[1]/span/text()",  # 高清，集数等
        'alias_xpath': "//div[2]/div[2]/ul/li[1]/span/text()",
        'img_xpath': "//div[1]/div/div/div[1]/img/@src",
        'director_xpath': "//div[2]/div[2]/ul/li[2]/span/text()",
        'leading_star_xpath': "//div[2]/div[2]/ul/li[3]/span/text()",
        'type_xpath': "//div[2]/div[2]/ul/li[4]/span/text()",
        'area_xpath': "//div[2]/div[2]/ul/li[5]/span/text()",
        'language_xpath': "//div[2]/div[2]/ul/li[6]/span/text()",
        'video_length_xpath': "//div[2]/div[2]/ul/li[8]/span/text()",
        'update_time_xpath': "//div[2]/div[2]/ul/li[9]/span/text()",
        'story_xpath': "//div[2]/div[2]/ul/li[14]/div/span[2]/text()",

        'names_xpath': "//*[@id='down_1']/ul/li/text()",
        'https_xpath': "//*[@id='play_1']/ul/li/input/@value",
        'video_name_xpath': "//div[2]/div[1]/h2/text()",
    }

sites_tuple = (0, site1, site2, site3, site4, site5, site6, site7,)
