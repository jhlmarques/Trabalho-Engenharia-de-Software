import pyodbc

class DatabaseController:
    def __init__(self):
        self.conn = None

    def _open_connection(self):
        if self.conn is None:
            conn_str = (
                f'DSN=MentorTop;'
                f'DATABASE=MentorTop'
            )
            self.conn = pyodbc.connect(conn_str)
    
    def _get_cursor(self):
        return self.conn.cursor()

    def _close_connection(self):
        if self.conn is not None:
            self.conn.close()

    def execute_query(self, query):
        self._open_connection()
        
        cursor = self._get_cursor()
        cursor.execute(query)
        table_rows = cursor.fetchall()

        self._close_connection()
        
        return table_rows