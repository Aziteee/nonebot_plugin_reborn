#!/usr/bin/env python
# coding=utf-8
import random

from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment

from nonebot_plugin_htmlrender import get_new_page

from .chart import get_chart_html
from .data import DATA

RATE = []
for item in DATA:
    birth_rate = item['birth_rate']
    RATE.append(birth_rate)

COUNTRY_REPLACE = {
    'Antigua and Barbuda': 'Antigua and Barb.',
    'Cabo Verde': 'Cape Verde',
    'Bosnia and Herzegovina': 'Bosnia and Herz.',
    'Brunei Darussalam': 'Brunei',
    'Bahamas The': 'Bahamas',
    'Cayman Islands': 'Cayman Is.',
    'Central African Republic': 'Central African Rep.',
    'Congo Rep.': 'Congo',
    'Congo Dem. Rep.': 'Dem. Rep. Congo',
    'Czechia': 'Czech Rep.',
    'Cote d\'Ivoire': 'Côte d\'Ivoire',
    'Dominican Republic': 'Dominican Rep.',
    'Egypt Arab Rep.': 'Egypt',
    'Gambia The': 'Gambia',
    'Kyrgyz Republic': 'Kyrgyzstan',
    'Korea Dem. People\'s Rep.': 'Dem. Rep. Korea',
    'Korea Rep.': 'Korea',
    'Iran Islamic Rep.': 'Iran',
    'St. Lucia': 'Saint Lucia',
    'Northern Mariana Islands': 'N. Mariana Is',
    'French Polynesia': 'Fr. Polynesia',
    'Russian Federation': 'Russia',
    'Solomon Islands': 'Solomon Is.',
    'Slovak Republic': 'Slovakia',
    'Sao Tome and Principe': 'São Tomé and Principe',
    'Syrian Arab Republic': 'Syria',
    'Turkiye': 'Turkey',
    'Venezuela RB': 'Venezuela',
    'Yemen Rep.': 'Yemen',
    'Micronesia Fed. Sts.': 'Micronesia',
    'North Macedonia': 'Macedonia',
    'Sudan': 'S. Sudan',

}

COUNTRY_IGNORE = [
    'Aruba',
    'Channel Islands',
    'Faroe Islands',
    'Hong Kong SAR China',
    'Monaco',
    'Macao SAR China',
    'St. Martin (French part)',
    'Maldives',
    'San Marino',
    'Eswatini',
    'Kosovo',
    'St. Kitts and Nevis',
    'St. Vincent and the Grenadines',
    'U.S. Virgin Is.'
]

CONTINENT_DICT = {
    'AF': '非洲',
    'EU': '欧洲',
    'AS': '亚洲',
    'OA': '大洋洲',
    'NA': '北美洲',
    'SA': '南美洲',
    'AN': '南极洲'
}

class Reborn:
    country_cn = ''
    country_en = ''
    continent_en = ''
    continent_cn = ''
    position = []
    birth_rate = 0

    def __init__(self):
        index = 0
        while index == 0 or DATA[index]['en'] in COUNTRY_IGNORE: # 去除map.js中不存在的国家
            index = self.__get_random_index()
        bp_instance = DATA[index]
        self.country_cn = bp_instance['cn']

        # 将原国家英文名替换为map.js中的，避免出现空地图
        if bp_instance['en'] in COUNTRY_REPLACE:
            self.country_en = COUNTRY_REPLACE[bp_instance['en']]
        else:
            self.country_en = bp_instance['en']

        self.continent_en = bp_instance['continent']
        self.continent_cn = CONTINENT_DICT[self.continent_en]
        self.position = bp_instance['position']
        self.birth_rate = bp_instance['birth_rate']

    def __get_random_index(self):
        start = 0
        index = 0
        randnum = random.randint(1, sum(RATE))
        for index, scope in enumerate(RATE):
            start += scope
            if randnum <= start:
                break
        return index

reborn_event = on_command('重生', aliases={'投胎', 'reborn'}, block=True)
@reborn_event.handle()
async def _():
    rb = Reborn()
    chart_html = get_chart_html(name_en=rb.country_en, longtitude=rb.position[0], latitude=rb.position[1], zoom=3)
    
    async with get_new_page(viewport={"width": 720, "height": 480}) as page:
        await page.set_content(chart_html)
        chart = await page.screenshot(full_page=True)
    
    await reborn_event.finish(MessageSegment.image(chart) + MessageSegment.text(f'你重生到了{rb.country_cn}！\n所在洲：{rb.continent_cn}'))