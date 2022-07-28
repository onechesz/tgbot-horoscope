import sqlite3


class Database:
    def __init__(self, path='core/data/horobot.db'):
        self.path = path

    @property
    def connection(self):
        return sqlite3.connect(self.path)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()

        connection = self.connection

        # connection.set_trace_callback(logger)

        cursor = connection.cursor()
        data = None

        cursor.execute(sql, parameters)

        if commit:
            connection.commit()

        if fetchone:
            data = cursor.fetchone()

        if fetchall:
            data = cursor.fetchall()

        connection.close()

        return data

    def create_table_users(self):
        sql = '''
        CREATE TABLE Users (
            user_id int NOT NULL,
            zodiac_sign varchar(20),
            PRIMARY KEY(user_id)
        );
        '''

        return self.execute(sql=sql, commit=True)

    def add_user(self, user_id: int, zodiac_sign: str = None):
        sql = '''
        INSERT INTO Users(user_id, zodiac_sign)
        VALUES(?, ?);
        '''
        parameters = (user_id, zodiac_sign)

        return self.execute(sql=sql, parameters=parameters, commit=True)

    def update_zodiac_sign(self, user_id: int, zodiac_sign: str):
        sql = '''
        UPDATE Users
        SET zodiac_sign = ?
        WHERE user_id = ?;
        '''

        return self.execute(sql=sql, parameters=(zodiac_sign, user_id), commit=True)

    def select_user_zodiac_sign(self, user_id: int):
        sql = '''
        SELECT zodiac_sign
        FROM Users
        WHERE user_id = ?;
        '''

        return self.execute(sql=sql, parameters=(user_id,), fetchone=True)

    def count_user(self, user_id: int):
        sql = '''
        SELECT COUNT(*)
        FROM Users
        WHERE user_id = ?; 
        '''

        return self.execute(sql=sql, parameters=(user_id,), fetchone=True)

    def all_users_data(self):
        sql = '''
        SELECT *
        FROM Users
        '''

        return self.execute(sql=sql, fetchall=True)

    def create_table_horoscope(self):
        sql = '''
        CREATE TABLE Horoscope (
            zodiac_sign varchar(20),
            horoscope varchar(1500),
            PRIMARY KEY(zodiac_sign)
        );
        '''

        return self.execute(sql=sql, commit=True)

    def insert_zodiac_signs(self):
        sql = '''
        INSERT INTO Horoscope(zodiac_sign)
        VALUES('Овен')
        '''

        return self.execute(sql=sql, commit=True)

    def update_horoscope(self, zodiac_sign, horoscope):
        sql = '''
        UPDATE Horoscope
        SET horoscope = ?
        WHERE zodiac_sign = ?
        '''

        return self.execute(sql=sql, parameters=(horoscope, zodiac_sign), commit=True)

    def select_horoscope_by_sign(self, zodiac_sign):
        sql = '''
        SELECT horoscope
        FROM Horoscope
        WHERE zodiac_sign = ?
        '''

        return self.execute(sql=sql, parameters=(zodiac_sign,), fetchone=True)

    def select_all_user_ids(self):
        sql = '''
        SELECT user_id
        FROM Users
        '''

        return self.execute(sql=sql, fetchall=True)
#
#
# def logger(statement):
#     print(f'''
# ----------------------------------------------------------------
# Executing:
# {statement}
# ----------------------------------------------------------------
# ''')
