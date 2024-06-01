from parking_lot import ParkingLot
from user import Admin, Customer
from ticketing_service import Ticket
import time


parkingLot = ParkingLot.getInstance("config")

customer1 = Customer(parkingLot, "AS0021", "Small")
ticket1:Ticket = customer1.park_vehicle()
print("VEHICLE PARKED")
print("TICKET INFO: ")
ticket1.print_info()

time.sleep(3)
invoice1 = customer1.release_vehicle(ticket1)
print("VEHICLE RELEASED")
print("INVOICE INFO: ")
invoice1.print_info()


customer2 = Customer(parkingLot, "KA0190", "Large")
ticket2:Ticket = customer2.park_vehicle()
print("VEHICLE PARKED")
print("TICKET INFO: ")
ticket2.print_info()

time.sleep(2)
invoice2 = customer2.release_vehicle(ticket2)
print("VEHICLE RELEASED")
print("INVOICE INFO: ")
invoice2.print_info()





admin = Admin(parkingLot)
admin.set_base_parking_price("Small",35)
admin.set_base_parking_price("Large", 65)
admin.set_weekend_rate(15)

# admin = admin.set_base_parking_price("Small",35, parkingLot).set_base_parking_price("Large", 65, parkingLot).set_weekend_rate(15, parkingLot)
print("Updated Payment Config")
print(parkingLot.payment_config)