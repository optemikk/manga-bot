import asyncio
import aiohttp
from bs4 import BeautifulSoup
from mangaparser.request_args import *
from typing import Union


class MangaParser:
    def __init__(self):
        pass

    async def get_manga(self, url: str) -> list:
        async with aiohttp.ClientSession() as session:
            url = 'https://readmanga.live' + url
            get_manga_headers['Referer'] += url
            async with session.get(url=url, headers=get_manga_headers, cookies=get_manga_cookies) as response:
                html = await response.text()

                soup = BeautifulSoup(html, "html.parser")
                data = soup.find_all('script', type="text/javascript")

                data = data[6].text.split('\n')[6].split('?')
                send = list()
                for i in data:
                    if 'auto' in i and 'xcredit' not in i and 'xhelp' not in i:
                        send.append('https://one-way.work/' + i.split('"')[-1])
                return send

    async def search(self, search: str) -> list:
        async with aiohttp.ClientSession() as session:
            search_params['query'] = search
            async with session.get(url=search_url, headers=search_headers, cookies=search_cookies, params=search_params) as response:

                json_ = await response.json()
                if json_['suggestions'][0]['value'] != 'Ничего не найдено':
                    return [[i['value'], i['link'], ' '.join(i['names']), i['thumbnail'].replace('_p.jpg', '.jpg')]
                            for i in json_['suggestions']]
                else:
                    return [None]

    async def open_page(self, url: str) -> str:
        async with aiohttp.ClientSession() as session:
            open_headers['Referer'] += url
            open_url = f'https://readmanga.live/{url}/vol1/1'
            async with session.get(url=open_url, headers=open_headers, cookies=open_cookies) as response:
                return await response.text()

    async def get_vols(self, html: str) -> dict:
        soup = BeautifulSoup(html, "html.parser")
        try:
            data = soup.find('table', class_="table table-hover").find_all('td',
                                                                           class_='item-title')  # find_all('a', class_='chapter-link cp-l manga-mtr')
        except:
            return {
                'status': False,
                'response': '(readmanga)Манга заблокирована!'
            }
        vols_urls = [(i.find('a')['href'], i.find('a').text.strip()) for i in data]
        vols = [i.text.strip().split(' - ') for i in data]
        return {
            'status': True,
            'response': '(readmanga)',
            'vols': vols_urls
        }

    async def get_request(self, url: str):
        async with aiohttp.ClientSession() as session:
            response = await session.get(url=url, cookies=get_manga_cookies)
            return response


manga_parser = MangaParser()
async def main():
    data = await manga_parser.search('монолог')
    html = await manga_parser.open_page(data[2][1])
    vols = await manga_parser.get_vols(html)
    print(vols)

if __name__ == '__main__':
    asyncio.run(main())