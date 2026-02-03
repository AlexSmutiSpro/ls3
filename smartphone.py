class Smartphone:
    def __init__(self, mark_phone, model_phone, number):
        self.mark = mark_phone
        self.model = model_phone
        self.num = number

    def phone_mark(self):
        print('Марка телефона ', self.mark,)

    def phone_model(self):
        print('Модель телефона ', self.model,)

    def number(self):
        print('Номер телефона', self.num)
