class User:
    def __init__(self, first_name, last_name):
        self.FN = first_name
        self.LN = last_name

    def my_name(self):
        print('Меня зовут', self.FN)

    def my_last_name(self):
        print('Моя фамилия', self.LN)

    def my_fn_and_my_ln(self):
        print(self.FN, self.LN)


user = User('Alex', 'Li')

user.my_name()
user.my_last_name()
user.my_fn_and_my_ln()
