import datetime
import time

class Car:
    def __init__(self, car_number, age_of_car, seller_info):
        self.car_number = car_number
        self.age_of_car = age_of_car
        self.seller_info = seller_info

    def set_price(self, buying_price, profit):
        self.price = buying_price + profit


class User:
    def __init__(self, name, address, is_buyer=False, is_seller=False):
        self.name = name
        self.is_buyer = is_buyer
        self.is_seller = is_seller
        self.address = address
        self.last_visit = ""
        self.car_owned = []

    # def update_car_owned(self, car:Car, buy_or_sell):
    #     if buy_or_sell == "buy":
    #         self.car_owned.append(car)
    #     if buy_or_sell == "sell" and car in self.car_owned:
    #         self.car_owned.remove(car)

    def update_last_visit(self):
        self.last_visit = time.ctime()

class Buyer(User):
    def update_car_owned(self, car:Car):
            self.car_owned.append(car)

    def set_is_buyer(self):
        self.is_buyer = True


class Seller(User):
    def update_car_owned(self, car:Car):
        if car in self.car_owned:
            self.car_owned.remove(car)

    def set_is_seller(self):
        self.is_seller = True

class CarStore:
    def __init__(self, capacity, address):
        self.capacity = capacity
        self.list_of_cars = []
        self.no_of_cars = 0
        self.address = address

    def buy_car(self, car:Car, seller: Seller):
        if self.no_of_cars < self.capacity:
            self.list_of_cars.append(car)
            self.no_of_cars += 1
            seller.set_is_seller()
            seller.update_car_owned(car)
            seller.update_last_visit()
        else:
            print("Store is full")

    def sell_car(self, car:Car, buyer:Buyer):
        if self.no_of_cars > 0:
            self.list_of_cars.remove(car)
            buyer.set_is_buyer()
            buyer.update_car_owned(car)
            buyer.update_last_visit()
        else:
            print("Store is empty")

if __name__ == "__main__":
    carStore = CarStore(5, "Bangalore")
    seller = Seller("Anil", "Bangalore")
    car = Car("001", 10, seller)

    carStore.buy_car(car,seller)
    print(carStore.list_of_cars[0].car_number, carStore.no_of_cars)












    


    
