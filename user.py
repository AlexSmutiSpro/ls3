class User:
    def __init__(self, first_name, last_name):
        self.FN = first_name
        self.LN = last_name

    def MyName(self):
        print('Меня зовут', self.FN)

    def MyLastName(self):
        print('Моя фамилия', self.LN)

    def MyFNandMyLN(self):
        print(self.FN, self.LN)


user = User('Alex', 'Li')

user.MyName()
user.MyLastName()
user.MyFNandMyLN()
