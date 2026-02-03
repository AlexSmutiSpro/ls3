
class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_ad = to_address
        self.from_ad = from_address
        self.Cost = cost
        self.Track = track

    def __str__(self):
        return (f'Отправление {self.Track} из {self.from_ad}'
                f' в {self.to_ad}. Стоимость {self.Cost} рублей')
