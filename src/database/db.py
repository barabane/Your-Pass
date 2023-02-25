import sqlite3
from aiogram.types import Message


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('your_pass.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id INT PRIMARY KEY,
            username TEXT,
            settings TEXT);
        """)
        self.conn.commit()

    def get_user(self, msg: Message):
        user = self.cursor.execute(
            f"SELECT * FROM users WHERE id={msg.from_user.id}").fetchone()

        if user:
            return user

        return 'такого пользователя не существует'

    def reg_user(self, msg: Message):
        exists = self.cursor.execute(
            f"SELECT * FROM users WHERE id={msg.from_user.id};")

        if exists.fetchone():
            return

        self.cursor.execute("INSERT INTO users VALUES(?,?,?);", (
            msg.from_user.id,
            msg.from_user.username,
            "{'length': 8,'numbers': True,'symbols': True }"
        ))
        self.conn.commit()


db = DB()
