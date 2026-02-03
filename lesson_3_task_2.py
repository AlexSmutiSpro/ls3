from smartphone import Smartphone
catalog = [Smartphone('IPHONE', '16ProMax', '+7903*******'),
           Smartphone('IPHONE', '14', '+7905******'),
           Smartphone('IPHONE', '17ProMax', '+7906*******'),
           Smartphone('IPHONE', '15Pro', '+7904******'),
           Smartphone('Samsung', 'GalaxyA12', '+7908******')]
for phone in catalog:
    print(f'{phone.Mark} - {phone.Model}. {phone.Num})')
