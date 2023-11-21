import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import os
import asyncio


class MangaParser():
    def __init__(self):
        pass


    def get_manga(self, url):

        cookies = {
            'JSESSIONID': '17E37D004F6D5634D86ECC22D2C1D4A6',
            '__cf_bm': 'kRU4Kg2mEygnsZKJ7M.u2rrkk0s9ACy.YrLuOJZIQ0M-1688417193-0-AcfLA6f9+bovFllzapzFRlGtFYn4YKOG9uHHH7LBV2f04Q5y1X3LFHX1Pgo+YBD9ug==',
            'sso_timeout': 'Tue^%^20Jul^%^2004^%^202023^%^2001:02:10^%^20GMT+0400^%^20(^%^D0^%^A1^%^D0^%^B0^%^D0^%^BC^%^D0^%^B0^%^D1^%^80^%^D1^%^81^%^D0^%^BA^%^D0^%^BE^%^D0^%^B5^%^20^%^D1^%^81^%^D1^%^82^%^D0^%^B0^%^D0^%^BD^%^D0^%^B4^%^D0^%^B0^%^D1^%^80^%^D1^%^82^%^D0^%^BD^%^D0^%^BE^%^D0^%^B5^%^20^%^D0^%^B2^%^D1^%^80^%^D0^%^B5^%^D0^%^BC^%^D1^%^8F)',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Referer': f'https://readmanga.live/{url}',
            'DNT': '1',
            'Connection': 'keep-alive',
            # 'Cookie': 'JSESSIONID=17E37D004F6D5634D86ECC22D2C1D4A6; __cf_bm=kRU4Kg2mEygnsZKJ7M.u2rrkk0s9ACy.YrLuOJZIQ0M-1688417193-0-AcfLA6f9+bovFllzapzFRlGtFYn4YKOG9uHHH7LBV2f04Q5y1X3LFHX1Pgo+YBD9ug==; sso_timeout=Tue^%^20Jul^%^2004^%^202023^%^2001:02:10^%^20GMT+0400^%^20(^%^D0^%^A1^%^D0^%^B0^%^D0^%^BC^%^D0^%^B0^%^D1^%^80^%^D1^%^81^%^D0^%^BA^%^D0^%^BE^%^D0^%^B5^%^20^%^D1^%^81^%^D1^%^82^%^D0^%^B0^%^D0^%^BD^%^D0^%^B4^%^D0^%^B0^%^D1^%^80^%^D1^%^82^%^D0^%^BD^%^D0^%^BE^%^D0^%^B5^%^20^%^D0^%^B2^%^D1^%^80^%^D0^%^B5^%^D0^%^BC^%^D1^%^8F)',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Sec-GPC': '1',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        response = requests.get(f'https://readmanga.live/{url}', cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        data = soup.find_all('script', type="text/javascript")

        data = data[6].text.split('\n')[6].split('?')
        send = list()
        for i in data:
            if 'auto' in i:
                send.append('https://one-way.work/' + i.split('"')[-1])

        return send


    def search(self, search):
        cookies = {
            'JSESSIONID': 'E7C2602B23B530DFB6B4BCAA685B6C7B',
            '__cf_bm': 'rtBaH8veYwih4ZNLCrmva.trf2_USTfht2qDZTf_azM-1688405313-0-Acfh/tbo9KkbyOSxz+ij5Q6YhzReJAsFgmEyOKaCKLaR9wFwSiUtuTBf7UIVQuyXLw==',
            'sso_timeout': 'Mon%20Jul%2003%202023%2021:49:04%20GMT+0400%20(%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B5%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)',
            'trSessionId': '0.2357Mon%20Jul%2003%202023%2021:54:18%20GMT+0400%20(%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B5%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://readmanga.live/',
            # 'Cookie': 'JSESSIONID=E7C2602B23B530DFB6B4BCAA685B6C7B; __cf_bm=rtBaH8veYwih4ZNLCrmva.trf2_USTfht2qDZTf_azM-1688405313-0-Acfh/tbo9KkbyOSxz+ij5Q6YhzReJAsFgmEyOKaCKLaR9wFwSiUtuTBf7UIVQuyXLw==; sso_timeout=Mon%20Jul%2003%202023%2021:49:04%20GMT+0400%20(%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B5%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F); trSessionId=0.2357Mon%20Jul%2003%202023%2021:54:18%20GMT+0400%20(%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B5%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        params = {
            'query': search,
            'types[]': [
                'CREATION',
                'FEDERATION_MANGA_SUBJECT',
            ],
        }

        response = requests.get('https://readmanga.live/search/suggestion', params=params, cookies=cookies, headers=headers).json()['suggestions']
        if response[0]['value'] != 'Ничего не найдено':
            return [[i['value'], i['link'], ' '.join(i['names']), i['thumbnail'].replace('_p.jpg', '_o.png')] for i in response]
        else:
            return None


    def open_page(self, url):

        cookies = {
            'JSESSIONID': '17E37D004F6D5634D86ECC22D2C1D4A6',
            'sso_timeout': 'Tue^%^20Jul^%^2004^%^202023^%^2003:17:41^%^20GMT+0400^%^20(^%^D0^%^A1^%^D0^%^B0^%^D0^%^BC^%^D0^%^B0^%^D1^%^80^%^D1^%^81^%^D0^%^BA^%^D0^%^BE^%^D0^%^B5^%^20^%^D1^%^81^%^D1^%^82^%^D0^%^B0^%^D0^%^BD^%^D0^%^B4^%^D0^%^B0^%^D1^%^80^%^D1^%^82^%^D0^%^BD^%^D0^%^BE^%^D0^%^B5^%^20^%^D0^%^B2^%^D1^%^80^%^D0^%^B5^%^D0^%^BC^%^D1^%^8F)',
            'remember_me': 'T0xmdk0zbVB0MEdES3RKaFhjY2tDbCUyQjVZZk5tQ3UwSnlzWVY2UlBJZXVVJTNEOmphQ0pMR2h6JTJGem1SNGJlY0FiMGs2b3dOTXozVnIwWmI5T3VrUUFvM0czUSUzRA',
            '__cf_bm': 'TOizeigHMejUjebpGfxHvG2xOfoCBbYMufKruM5DC1o-1688426481-0-AUGlKnlilt9upx6Ka4h5mAJsEhIPfd228G6sLZrUWsZOIsnIw4jFkVBLAS7mbSAnCA==',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Referer': f'https://readmanga.live/{url}',
            'DNT': '1',
            'Connection': 'keep-alive',
            # 'Cookie': 'JSESSIONID=17E37D004F6D5634D86ECC22D2C1D4A6; sso_timeout=Tue^%^20Jul^%^2004^%^202023^%^2003:17:41^%^20GMT+0400^%^20(^%^D0^%^A1^%^D0^%^B0^%^D0^%^BC^%^D0^%^B0^%^D1^%^80^%^D1^%^81^%^D0^%^BA^%^D0^%^BE^%^D0^%^B5^%^20^%^D1^%^81^%^D1^%^82^%^D0^%^B0^%^D0^%^BD^%^D0^%^B4^%^D0^%^B0^%^D1^%^80^%^D1^%^82^%^D0^%^BD^%^D0^%^BE^%^D0^%^B5^%^20^%^D0^%^B2^%^D1^%^80^%^D0^%^B5^%^D0^%^BC^%^D1^%^8F); remember_me=T0xmdk0zbVB0MEdES3RKaFhjY2tDbCUyQjVZZk5tQ3UwSnlzWVY2UlBJZXVVJTNEOmphQ0pMR2h6JTJGem1SNGJlY0FiMGs2b3dOTXozVnIwWmI5T3VrUUFvM0czUSUzRA; __cf_bm=TOizeigHMejUjebpGfxHvG2xOfoCBbYMufKruM5DC1o-1688426481-0-AUGlKnlilt9upx6Ka4h5mAJsEhIPfd228G6sLZrUWsZOIsnIw4jFkVBLAS7mbSAnCA==',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Sec-GPC': '1',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        params = {
            'mtr': 'true',
        }

        response = requests.get(f'https://readmanga.live/{url}/vol1/1', cookies=cookies,
                                headers=headers)
        return response


    def save_page(self, url, folder):
        try:
            os.mkdir(path=fr'imgs\{folder}')
        except:
            pass
        img = requests.get(f"https://one-way.work/{url}")
        with open(fr'imgs\{folder}\img_{url.split("/")[-1]}', 'wb') as file:
            file.write(img.content)


    def get_vols(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        try:
            data = soup.find('table', class_="table table-hover").find_all('td', class_='item-title')   # find_all('a', class_='chapter-link cp-l manga-mtr')
        except:
            return '(readmanga)Манга заблокирована!'
        vols_urls = [(i.find('a')['href'], i.find('a').text.strip()) for i in data]
        vols = [i.text.strip().split(' - ') for i in data]

        # for i in range(len(vols)):
        #     print(vols[i])
        #     print(vols_urls[i])

        return vols_urls


manga_parser = MangaParser()

# if __name__ == "__main__":
#     search = "мой телохранитель"
#     a = MParser()
#     response = a.search(search=search)
#     print(response)
#     req = response[0][1]
#     print(req)
#     response = a.open_page(url=req)
#     vols = a.get_vols(response=response)
#     print(vols)
#     print(a.get_manga(url=vols[-1][0]))
    # print(a.get_manga(url=vols[-1]))
    # if 'заблокирована' not in vols:
    #     for i in reversed(vols):
    #         folder = ''.join(i.split('/')[-2:])
    #         pages = a.get_manga(url=i)
    #         for k in pages:
    #             a.save_page(url=k, folder=folder)
    # else:
    #     print('Не удалось загрузить. Манга заблокирована')





# data = data[6].text.split('\n')[6].split('?')
# send = list()
# for i in data:
#     if 'auto' in i:
#         send.append(i.split('"')[-1])



# for i in send:
#     img = requests.get(f"https://one-way.work/{i}") # .png_res
#     with open(fr'imgs\{page}\img_{i.split("/")[-1]}', 'wb') as file:
#         file.write(img.content)