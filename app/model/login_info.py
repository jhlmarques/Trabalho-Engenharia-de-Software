class LoginInfo:
    def get_password(self, cursor, username):
        '''
        :param cursor: Cursor da conexão enviado pelo controller
        :param username: Username do usuário
        :return: A senha do usuário, caso haja correspondência no banco de dados ou
                 None, caso contrário
        '''
        cursor.execute('select Password from dbo.Employees where Username = ?', username)
        row = cursor.fetchmany()
        print(row)
        if row is not None:
            password = row[0][0] # pega o primeiro e único elemento - a senha
        return password
