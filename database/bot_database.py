from database.base_database import Database


class BotDatabase(Database):

    async def add_user(self, user_id: int):
        with self.db:
            self.c.execute("INSERT INTO users VALUES (?)", (user_id,))
            self.c.execute("INSERT INTO users_service VALUES (?, ?, ?)", (user_id, None, None))
            self.db.commit()
            print(f'[DB] Пользователь "{user_id}" был добавлен в базу')

    async def is_user_exists(self, user_id: int) -> bool:
        with self.db:
            try:
                user = self.c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()[0][0]
                return True
            except:
                return False
            # if len(user) > 0:
            #     return True
            # else:
            #     return False

    async def get_user_message(self, user_id: int) -> int:
        with self.db:
            message_id = self.c.execute("SELECT message_id FROM users_service WHERE user_id = ?", (user_id,)).fetchall()[0][0]
        return message_id

    async def set_user_message(self, user_id: int, message_id: int) -> bool:
        try:
            with self.db:
                self.c.execute("UPDATE users_service SET message_id = (?) WHERE user_id = (?)", (message_id, user_id))
                self.db.commit()
                print(f'[DB] message_id пользователя {user_id} успешно записан')
            return True
        except Exception as e:
            print('[DB] Ошибка в записи:', e)
            return False




bot_db = BotDatabase()