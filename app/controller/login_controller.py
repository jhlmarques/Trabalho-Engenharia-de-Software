from .database_controller import DatabaseController
from typing import NamedTuple

class LoginInfo(NamedTuple):
    username : str
    realName : str
    roleName : str
    roleId : int


class LoginController:
    def __init__(self):
        self.database = DatabaseController()
    
    
    def _get_user_password(self, username):
        """
        :param username: Username do usuário
        :return: A senha do usuário, caso não haja correspondência no banco de dados ou
                 None, caso contrário
        """
        
        query = f'select Password from dbo.Employees where Username = \'{username}\''
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
        query = (
            'select Username, CompleteName, Employees.RoleId, RoleName '
            'FROM dbo.Employees '
            'JOIN dbo.Roles ON (Employees.RoleId = Roles.RoleId) '
            f'WHERE Username = \'{username}\''
        )
        table_rows = self.database.execute_query(query)
        if len(table_rows) > 0:
            return LoginInfo(table_rows[0][0], table_rows[0][1], table_rows[0][2], table_rows[0][3])
        else:
            return None

if __name__ == "__main__":
    controller = LoginController()
