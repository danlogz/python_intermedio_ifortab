class myPostgresSQLconn:
    def __init__(self, bd, user, password, host = '127.0.0.1'):
        self.bd = bd
        self.user = user
        self.password = password
        self.host = host
    
connection = myPostgresSQLconn(bd, user, password)