class Address:
    def __init__(self, index, city, street, house, apartment):
        self.In = index
        self.Ci = city
        self.St = street
        self.Ho = house
        self.Ap = apartment

    def __str__(self):
        return f'{self.In}, {self.Ci}, {self.St}, {self.Ho}, {self.Ap}'
