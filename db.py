import datetime
import sqlite3

import pytz  # pip install pytz


class BotDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def add_user(self, user_id, user_name, user_subj):
        """Добавляем юзера в базу"""
        if user_name is None:
            user_name = '-'
        self.cursor.execute("INSERT INTO `users` (`user_id`, `user_name`, `subj`) VALUES (?, ?, ?)",
                            (user_id, user_name, user_subj,))
        return self.conn.commit()

    def add_user_from_prof(self, user_id, user_name, user_prof):
        """Добавляем юзера в базу"""
        if user_name is None:
            user_name = '-'
        self.cursor.execute("INSERT INTO `users` (`user_id`, `user_name`, `random_subj`) VALUES (?, ?, ?)",
                            (user_id, user_name, user_prof,))
        return self.conn.commit()

    def user_exists(self, user_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_subj(self, user_id):
        """Достаем subj юзера в базе по его user_id"""
        result = self.cursor.execute("SELECT `subj` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def get_user_class(self, user_id):
        """Достаем class юзера в базе по его user_id"""
        result = self.cursor.execute("SELECT `class` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def get_user_level(self, user_id):
        """Достаем class юзера в базе по его user_id"""
        result = self.cursor.execute("SELECT `level` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def set_user_class(self, user_id, user_class):
        """Обновляем class юзера в базе по его user_id"""
        self.cursor.execute("UPDATE `users` SET `class` = ? WHERE `user_id` = ?", (user_class, user_id))
        self.conn.commit()
        self.cursor.execute("UPDATE `users` SET `date_time_last_change` = ? WHERE `user_id` = ?",
                            (datetime.datetime.now(pytz.utc), user_id))
        self.conn.commit()

    def set_user_subj(self, user_id, user_subj):
        """Обновляем subj юзера в базе по его user_id"""
        self.cursor.execute("UPDATE `users` SET `subj` = ? WHERE `user_id` = ?", (user_subj, user_id))
        self.conn.commit()

    def set_user_level(self, user_id, user_level):
        """Обновляем level юзера в базе по его user_id"""
        self.cursor.execute("UPDATE `users` SET `level` = ? WHERE `user_id` = ?", (user_level, user_id))
        self.conn.commit()

    def get_users_count(self):
        return list(self.cursor.execute("SELECT COUNT(`id`) from `users`"))[0][0]

    def get_users_list(self):
        return list(self.cursor.execute("SELECT * FROM `users`"))

    def add_admin_text(self, admin_id, admin_name, message_text):
        self.cursor.execute("INSERT INTO `admin_texts` (`admin_id`, `admin_name`, `message_text`) VALUES (?, ?, ?)",
                            (admin_id, admin_name, message_text,))
        return self.conn.commit()

    def set_admin_text_status(self, text_id):
        self.cursor.execute("UPDATE `admin_texts` SET `is_send` = ? WHERE `text_id` = ?", (1, text_id,))
        self.conn.commit()

    def get_last_admin_text(self):
        return list(self.cursor.execute("SELECT * FROM `admin_texts` ORDER BY `text_id` DESC LIMIT 1"))[0]

    def last_olymp_exist(self, user_id) -> bool:
        result = self.cursor.execute("SELECT `last_olymp` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_last_olymp(self, user_id):
        result = self.cursor.execute("SELECT `last_olymp` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def reset_last_olymp(self, user_id, name):
        self.cursor.execute("UPDATE `users` SET `last_olymp` = ? WHERE `user_id` = ?", (name, user_id,))
        self.conn.commit()

    def del_last_olymp(self, user_id):
        self.cursor.execute("UPDATE `users` SET `last_olymp`= NULL WHERE `user_id` = ?", (user_id,))
        self.conn.commit()

    def set_user_prof(self, user_id, user_prof):
        """Обновляем prof юзера в базе по его user_id"""
        self.cursor.execute("UPDATE `users` SET `random_subj` = ? WHERE `user_id` = ?", (user_prof, user_id))
        self.conn.commit()
        self.cursor.execute("UPDATE `users` SET `date_time_last_change` = ? WHERE `user_id` = ?",
                            (datetime.datetime.now(pytz.utc), user_id))
        self.conn.commit()

    def get_user_prof(self, user_id):
        """Достаем prof юзера в базе по его user_id"""
        result = self.cursor.execute("SELECT `random_subj` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def last_olymp_exist(self, user_id):
        result = self.cursor.execute("SELECT `subj` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchall()[0]

    def last_random_olymp_exist(self, user_id):
        result = self.cursor.execute("SELECT `random_subj` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchall()[0]

    def add_user_text(self, user_id, username, user_text):
        self.cursor.execute(
            "INSERT INTO `users_texts_to_support` (`user_id`, `username`, `user_text`) VALUES (?, ?, ?)",
            (user_id, username, user_text,))
        return self.conn.commit()

    def get_user_question_text(self, id):
        """Достаем text юзера в базе по его user_id"""
        result = self.cursor.execute("SELECT `user_text` FROM `users_texts_to_support` WHERE `id` = ?", (id,))
        return result.fetchone()[0]

    def add_admin_ans(self, id, admin_username, admin_answer):
        # self.cursor.execute("INSERT INTO `users_texts_to_support` (`id`, `admin_username`, `admin_answer`, `time_send_answer`) VALUES (?, ?, ?, ?)",
        #                     (id, admin_username, admin_answer, datetime.datetime.now(pytz.utc),))
        self.cursor.execute(
            "UPDATE `users_texts_to_support` SET (`admin_username`, `admin_answer`, `time_send_answer`) = (?, ?, ?) WHERE `id` = ?",
            (admin_username, admin_answer, datetime.datetime.now(pytz.utc), id,))
        return self.conn.commit()

    def get_user_id_from_question_id(self, id):
        result = self.cursor.execute("SELECT `user_id` FROM `users_texts_to_support` WHERE `id` = ?", (id,))
        return result.fetchone()

    def get_last_question_id(self):
        return list(self.cursor.execute("SELECT * FROM `users_texts_to_support` ORDER BY `id` DESC LIMIT 1"))[0]

    def close(self):
        """Закрываем соединение с БД"""
        self.conn.close()
