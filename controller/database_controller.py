import pyodbc

class DatabaseController:
    def __init__(self):
        self.dsn = "MentorTop"
        self.database = "MentorTop"
        self.conn = None

    def open_connection(self):
        if self.conn is None:
            print(f"Connecting to {self.database} database...")
            conn_str = (
                f'DSN={self.dsn};'
                f'DATABASE={self.database}'
            )
            self.conn = pyodbc.connect(conn_str)

    def close_connection(self):
        if self.conn is not None:
            print("Closing connection...")
            self.conn.close()


db_controller = DatabaseController()

db_controller.open_connection()
db_controller.close_connection()


