import sqlite3
import json
import ast
from loguru import logger
from aiogram.types import Message


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('yourpass.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id INT PRIMARY KEY,
            username TEXT,
            settings TEXT);
        """)
        self.conn.commit()

    def get_user(self, msg: Message):
        user = self.cursor.execute(
            f"SELECT * FROM users WHERE id=?", (msg.from_user.id)).fetchone()

        if user:
            return user

        logger.error("user not exists")
        return {}

    def reg_user(self, msg: Message):
        exists = self.cursor.execute(
            f"SELECT * FROM users WHERE id={msg.from_user.id}")

        if exists.fetchone():
            logger.info("user already exists")
            return

        self.cursor.execute("INSERT INTO users VALUES(?,?,?);", (
            msg.from_user.id,
            msg.from_user.username,
            "{'length': 8,'numbers': True,'symbols': True }"
        ))
        logger.info(f"add new user {msg.from_user.id}")
        self.conn.commit()

    def get_settings(self, user_id: int):
        user_settings = self.cursor.execute(
            f"SELECT settings FROM users WHERE id={user_id}").fetchone()

        return ast.literal_eval(user_settings[0])

    def change_settings(self, user_id: int, new_settings: str):
        self.cursor.execute(
            f"UPDATE users SET settings=? WHERE id=?", (new_settings, user_id))
        logger.info(f"user({user_id}) settings updated")
        self.conn.commit()


db = DB()
