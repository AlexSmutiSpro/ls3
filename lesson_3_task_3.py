from address import Address
from mailing import Mailing

to_address = Address(650000, 'Кемерово', 'ул.Московская', 'Д 27', 'Кв 12')
from_address = Address(652345, 'Москва', 'ул.Ленинградская', 'Д 5', 'Кв 70')
track = 57839851
cost = 2500

mailing = Mailing(to_address, from_address, cost, track)

print(mailing)
