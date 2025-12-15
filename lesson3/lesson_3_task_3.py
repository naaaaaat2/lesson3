class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

to_addr = Address("123456", "Москва", "Ленинградский проспект", "10", "15")
from_addr = Address("654321", "Санкт-Петербург", "Невский проспект", "5", "20")

shipment = Mailing(to_address=to_addr, from_address=from_addr, cost=250, track="AB123456789RU")

print(f"Отправление {shipment.track} из {shipment.from_address.index}, {shipment.from_address.city}, {shipment.from_address.street}, {shipment.from_address.house} - {shipment.from_address.apartment} "
      f"в {shipment.to_address.index}, {shipment.to_address.city}, {shipment.to_address.street}, {shipment.to_address.house} - {shipment.to_address.apartment}. "
      f"Стоимость {shipment.cost} рублей.")
