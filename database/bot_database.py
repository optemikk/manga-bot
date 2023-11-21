from database.base_database import Database


class BotDatabase(Database):

    async def add_user(self, user_id: int):
        with self.db:
            self.c.execute("INSERT INTO users VALUES (?)", (user_id,))
            print(f'[DB] Пользователь "{user_id}" был добавлен в базу')

    async def is_user_exists(self, user_id: int) -> bool:
        with self.db:
            user = self.c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
            if len(user) > 0:
                return True
            else:
                return False


bot_db = BotDatabase()