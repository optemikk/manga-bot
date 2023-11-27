from database.base_database import Database
import asyncio


class MangaDatabase(Database):
    async def add_volume(self, title: str, path: str, telegraph_url: str, source_url: str):
        if not await self.is_manga_exists(title):
            self.c.execute("INSERT INTO manga VALUES (?, ?, ?, ?)", (title, path, telegraph_url,
                'https://readmanga.live' + source_url if 'readmanga.live' not in source_url else source_url))
            self.db.commit()

    async def is_manga_exists(self, title: str) -> bool:
        manga = self.c.execute('SELECT * FROM manga WHERE title = ?', (title,)).fetchall()
        if len(manga) > 0:
            return True
        else:
            return False

    async def get_manga_path(self, title: str) -> str:
        path = self.c.execute('SELECT path FROM manga WHERE title = ?', (title,)).fetchall()[0][0]
        return path

    async def get_manga_list(self):
        manga = self.c.execute("SELECT * FROM manga").fetchall()
        print(manga)
        return manga

    async def get_manga_info(self, title: str) -> dict:
        info = self.c.execute('SELECT * FROM manga WHERE title = ?', (title,)).fetchall()[0]
        return {
            'title': info[0],
            'path': info[1],
            'telegraph_url': info[2],
            'source_url': info[3]
        }


manga_db = MangaDatabase()