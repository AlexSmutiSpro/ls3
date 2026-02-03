class Smartphone:
    def __init__(self, mark_phone, model_phone, number):
        self.Mark = mark_phone
        self.Model = model_phone
        self.Num = number

    def PhoneMark(self):
        print('Марка телефона ', self.Mark,)

    def PhoneModel(self):
        print('Модель телефона ', self.Model,)

    def Number(self):
        print('Номер телефона', self.Num)
