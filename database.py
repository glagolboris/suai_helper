from mysql.connector import connect
import mysql


class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect_to_bd(self):
        try:
            self.connection = connect(
                host='localhost',
                user='root',
                password='root1234567890',
                auth_plugin='mysql_native_password',
                database='Onboard_bd'
            )
        except mysql.connector.errors.ProgrammingError:
            connection = connect(
                host='localhost',
                user='root',
                password='root1234567890',
                auth_plugin='mysql_native_password',
            )
            cursor = connection.cursor()
            cursor.execute('CREATE DATABASE Onboard_bd')
            connection.commit()
            self.connect_to_bd()

    def create_tables(self) -> (mysql.connector.connection.MySQLConnection, mysql.connector.connection.MySQLCursor):
        cursor: mysql.connector.connection.MySQLCursor = self.connection.cursor(buffered=True)
        cursor.execute("DROP TABLE students")
        cursor.execute("""CREATE TABLE IF NOT EXISTS students(group_name TEXT, id INT UNSIGNED, history JSON);""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS timetable(group_name TEXT, couples JSON)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS professors(full_name JSON)""")
        self.connection.commit()

        self.cursor = cursor
        return self.connection, self.cursor

    def run_bd(self) -> (mysql.connector.connection.MySQLConnection, mysql.connector.connection.MySQLCursor):
        self.connect_to_bd()
        return self.create_tables()
