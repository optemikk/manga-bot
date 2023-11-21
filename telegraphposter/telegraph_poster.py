import asyncio
from telegraph.aio import Telegraph
from database import manga_db

access_token = '950168bda7a0222dc2b52b50e6dc9ed660c2a52a4f34cea6215d5a5cfafc'


class TelegraphPoster:
    def __init__(self, access_token: str):
        self.th = Telegraph(access_token=access_token)

    async def is_page_exists(self, path: str = None) -> bool:
        try:
            await self.th.get_page(path=path)
            return True
        except:
            return False

    async def upload_page(self, source_url: str, title_start: str, title_end: str, content_list: list):
        html_content_list = list()
        # html_content_list.append('@mangaposter https://t.me/mangaposter\n')
        [html_content_list.append(f'<img src="{img}">') for img in content_list]
        html_content_list.append('\n@mangaposter https://t.me/mangaposter')
        html_content = '\n'.join(html_content_list)
        # exists = await self.is_page_exists(path)
        exists = await manga_db.is_manga_exists(title=title_end)
        if exists:
            # response = await self.th.edit_page(path=await manga_db.get_manga_path(title=title_end), title=title_start, html_content=html_content, return_content=True)
            # await self.th.edit_page(path=response['path'], title=title_end, html_content=html_content)
            response = await manga_db.get_manga_info(title=title_end)
        else:
            response = await self.th.create_page(title=title_start, html_content=html_content, return_content=True)
            await self.th.edit_page(path=response['path'], title=title_end, html_content=html_content)
        path = response['path']
        await manga_db.add_volume(title=title_end, path=path, telegraph_url=response['url'], source_url=source_url)


telegraph_poster = TelegraphPoster(access_token)


if __name__ == '__main__':
    th = TelegraphPoster(access_token=access_token)
    title = '/podzemele_vkusnostei__A533b/vol1/0'
    page_list = ['https://one-way.work/auto/36/04/91/005.png_res.jpg', 'https://one-way.work/auto/36/04/91/006.png_res.jpg', 'https://one-way.work/auto/36/04/91/007.png_res.jpg', 'https://one-way.work/auto/36/04/91/008.png_res.jpg', 'https://one-way.work/auto/36/04/91/009.png_res.jpg', 'https://one-way.work/auto/36/04/91/010.png_res.jpg', 'https://one-way.work/auto/36/04/91/011.png_res.jpg', 'https://one-way.work/auto/36/04/91/012.png_res.jpg', 'https://one-way.work/auto/36/04/91/013.png_res.jpg', 'https://one-way.work/auto/36/04/91/014.png_res.jpg', 'https://one-way.work/auto/36/04/91/015.png_res.jpg', 'https://one-way.work/auto/36/04/91/016.png_res.jpg', 'https://one-way.work/auto/36/04/91/017.png_res.jpg', 'https://one-way.work/auto/36/04/91/018.png_res.jpg', 'https://one-way.work/auto/36/04/91/019.png_res.jpg', 'https://one-way.work/auto/36/04/91/020.png_res.jpg', 'https://one-way.work/auto/36/04/91/021.png_res.jpg', 'https://one-way.work/auto/36/04/91/022.png_res.jpg', 'https://one-way.work/auto/36/04/91/023.png_res.jpg', 'https://one-way.work/auto/36/04/91/024.png_res.jpg', 'https://one-way.work/auto/36/04/91/025.png_res.jpg', 'https://one-way.work/auto/36/04/91/026.png_res.jpg', 'https://one-way.work/auto/36/04/91/027.png_res.jpg', 'https://one-way.work/auto/36/04/91/028.png_res.jpg', 'https://one-way.work/auto/36/04/91/029.png_res.jpg', 'https://one-way.work/auto/36/04/91/030.png_res.jpg', 'https://one-way.work/auto/36/04/91/031.png_res.jpg', 'https://one-way.work/auto/36/04/91/032.png_res.jpg', 'https://one-way.work/auto/36/04/91/033.png_res.jpg', 'https://one-way.work/auto/36/04/91/034.png_res.jpg', 'https://one-way.work/auto/36/04/91/035.png_res.jpg', 'https://one-way.work/auto/36/04/91/036.png_res.jpg', 'https://one-way.work/auto/36/04/91/037.png_res.jpg', 'https://one-way.work/auto/36/04/91/038.png_res.jpg', 'https://one-way.work/auto/36/04/91/039.png_res.jpg', 'https://one-way.work/auto/36/04/91/040.png_res.jpg', 'https://one-way.work/auto/36/04/91/041.png_res.jpg', 'https://one-way.work/auto/36/04/91/042.png_res.jpg', 'https://one-way.work/auto/36/04/91/043.png']
    asyncio.run(th.upload_page(source_url=title, path='podzemele-vkusnostei-A533bvol11-11-21-4', title_start='/podzemele_vkusnostei__A533b/vol1/1', title_end='1 - 1 Горячий котелок', content_list=page_list))
    # asyncio.run(th.is_page_exists(path='test-article-11-20')) #  podzemele-vkusnostei-A533bvol10-11-20