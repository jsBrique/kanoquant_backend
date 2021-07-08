from .userdata import AccountData



class Reader:
    def read_positions(self,username='dobriq'):
        return AccountData.query.filter(AccountData.username==username).first().position