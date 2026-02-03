from smartphone import Smartphone
catalog = [Smartphone('iphone', '16ProMax', '+79031242356'),
           Smartphone('iphone', '14', '+79052547522'),
           Smartphone('iphone', '17ProMax', '+79068667454'),
           Smartphone('iphone', '15Pro', '+79047857946'),
           Smartphone('Samsung', 'GalaxyA12', '+790824578457')]
for phone in catalog:
    print(f'{phone.mark} - {phone.model}. {phone.num}')
