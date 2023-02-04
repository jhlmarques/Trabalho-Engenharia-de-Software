from controller.database_controller import DatabaseController
from model.models import LoginInfo
from controller.queries_sql import Queries

class LoginController:
    def __init__(self):
        self.database = DatabaseController()

    def _get_user_password(self, username):
        """
        :param username: Username do usuário
        :return: A senha do usuário, caso não haja correspondência no banco de dados ou
                 None, caso contrário
        """
        query = Queries.query_get_user_password
        table_rows = self.database.execute_query(query)
        if len(table_rows) > 0:
            return table_rows[0][0]
        else:
            return None
    
    def authenticate_user(self, username, password):
        db_password = self._get_user_password(username)

        if db_password is not None:
            return db_password == password
        else: 
            return False

    def getLoginInfo(self, username):
        query = Queries.query_getLoginInfo(username)
        table_rows = self.database.execute_query(query)
        if len(table_rows) > 0:
            return LoginInfo(*table_rows[0])
        else:
            return None

if __name__ == "__main__":
    controller = LoginController()
