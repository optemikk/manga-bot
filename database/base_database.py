import sqlite3


class Database:

    def __init__(self):
        self.db = sqlite3.connect(database='database.sqlite')
        self.c = self.db.cursor()

        self.c.execute(f'''CREATE TABLE IF NOT EXISTS users (
                        user_id INT
                )''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS manga (
                                title TEXT,
                                path TEXT,
                                telegraph_url TEXT,
                                source_url TEXT
                        )''')

    def create_table(self, table):
        try:
            self.c.execute(f'''CREATE TABLE IF NOT EXISTS {table} (
        user_id INT,
);''')
            self.db.commit()

        except Exception as e:
            print('[!] Database error:', e)


    def add_value(self, table, values):
        try:
            self.c.execute(f"INSERT INTO {table} VALUES ({values})")
            self.db.commit()
            print(f'[*] Added value to the "{table}": {values}')
        except Exception as e:
            print('[!] Database error:', e)


    def select_value(self, table, keys, where=''):
        try:
            if where == '':
                self.c.execute(f"SELECT {keys} FROM {table}")
                show = self.c.fetchall()
                return show
            else:
                self.c.execute(f"SELECT {keys} FROM {table} WHERE {where}")
                show = self.c.fetchall()
                return show
        except Exception as e:
            print('[!] Database error:', e)


    def delete_value(self, table, where='---'):
        try:
            self.c.execute(f"DELETE FROM {table} WHERE {where}")
            self.db.commit()
            print(f'[*] Deleted "{where}" from "{table}"')
        except Exception as e:
            print('[!] Database error:', e)


    def update_value(self, table, key, where='---'):
        try:
            self.c.execute(f"UPDATE {table} SET {key} WHERE {where}")
            self.db.commit()
            print(f'[*] Updated "{where}" from "{table}": {key}')
        except Exception as e:
            print('[!] Database error:', e)

    def drop_table(self, table):
        try:
            self.c.execute(f'DROP TABLE {table}')
            self.db.commit()
            print(f'[*] Dropped "{table}"')
        except Exception as e:
            print('[!] Database error:', e)

    def close_db(self):
        self.db.close()


database = Database()

if __name__ == '__main__':
    database = Database()
    # database.drop_table(table='ad')
    # database.create_table(table='ad')
    # database.add_value(table='ad', values="ad_123, 0")
    # a = database.select_value(table='users', keys='rowid, *')
    # database.update_value(table='users', key="'1' = ''", where="user_id = 972383332")
    # a = len(database.select_value(table='ad', keys='*', where=f'number = 1'))
    a = database.select_value(table='users', keys='rowid, *', where='user_id = 972383332')
    print(a)
    # database.delete_value(table='users', where='user_id = 972383332')
    # database.select_value(table='users', keys='rowid, *', where="")
    # database.delete_value(table='ad', where='rowid = 1')
    # a = database.select_value(table='users', keys='rowid, *')
    # database.delete_value(table='users', where='rowid >= 3')