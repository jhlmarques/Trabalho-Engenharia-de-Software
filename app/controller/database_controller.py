import pyodbc
from app.model.login_info import LoginInfo


class DatabaseController:
    def __init__(self, dsn, database):
        self.dsn = dsn
        self.database = database
        self.conn = None

    def open_connection(self):
        if self.conn is None:
            print(f"Connecting to {self.database} database...")
            conn_str = (
                f'DSN={self.dsn};'
                f'DATABASE={self.database}'
            )
            self.conn = pyodbc.connect(conn_str)

    def get_cursor(self):
        return self.conn.cursor()

    def close_connection(self):
        if self.conn is not None:
            print("Closing connection...")
            self.conn.close()


if __name__ == "__main__":
    db_controller = DatabaseController("MentorTop", "MentorTop")
    db_controller.open_connection()

    cursor = db_controller.get_cursor()
    login_user = LoginInfo()
    login_user.get_password(cursor, "Hernandes")

    db_controller.close_connection()


