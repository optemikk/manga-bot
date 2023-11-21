import asyncio
import platform
from mangaparser import manga_parser
from telegraphposter import telegraph_poster
from database import database
from database import manga_db

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main():
    # search = await manga_parser.search('мой телохранитель')
    # html = await manga_parser.open_page(search[1][1])
    # vols = await manga_parser.get_vols(html)
    # vol = 5
    # manga = await manga_parser.get_manga(vols['vols'][-vol][0])
    # await telegraph_poster.upload_page(source_url=vols['vols'][-vol][0], title_start=vols['vols'][-vol][0], title_end=vols['vols'][-vol][1], content_list=manga)
    print(await manga_db.get_manga_info(title='2 - 5 Помада и нежности'))


if __name__ == '__main__':
    asyncio.run(main())