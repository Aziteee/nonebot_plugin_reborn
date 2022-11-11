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
        while index == 0:
            index = self.__get_random_index()
        bp_instance = DATA[index]
        self.country_cn = bp_instance['cn']
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