import asyncio
from telegraph.aio import Telegraph
import platform

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

access_token = '950168bda7a0222dc2b52b50e6dc9ed660c2a52a4f34cea6215d5a5cfafc'
auth_url = 'https://edit.telegra.ph/auth/bQ9av463ICAgD6AZkjjmM7t6hb51nliwarGFvNHcnh'
link = 'https://telegra.ph/Hey-11-20-54'
path = 'Hey-11-20-54'


async def main():
    telegraph = Telegraph(access_token=access_token)
    # await telegraph.edit_account_info(short_name='@mangaposter', author_name='@mangaposter', author_url='https://t.me/mangaposter')
    # print(await telegraph.edit_page(path='123123', title='article', content='123123', return_content=True))
    # info = await telegraph.get_account_info(fields=['short_name', 'author_name', 'author_url', 'auth_url', 'page_count'])
    # print(info)
    page_list = await telegraph.get_page_list()
    print(page_list)
    # for i in page_list['pages']:
        # await telegraph.edit_page(path=i['path'], title='@mangaposter https://t.me/mangaposter', html_content='@mangaposter https://t.me/mangaposter')
    # page_list = ['https://one-way.work/auto/24/00/55/001.jpg', 'https://one-way.work/auto/24/00/55/002.jpg', 'https://one-way.work/auto/24/00/55/003.jpg', 'https://one-way.work/auto/24/00/55/004.jpg', 'https://one-way.work/auto/24/00/55/005.jpg', 'https://one-way.work/auto/24/00/55/006.jpg', 'https://one-way.work/auto/24/00/55/007.jpg', 'https://one-way.work/auto/24/00/55/008.jpg', 'https://one-way.work/auto/24/00/55/009.jpg']
    # content = [f'<img src="{page}">' for page in page_list]
    # await telegraph.edit_page(path='test-article-11-20', title='test-article', content=None, html_content='\n'.join(content))
    # file = FilesOpener(paths=['002.png']).open_files()
    # await telegraph.upload_file(f=file)

asyncio.run(main())