import time

from vehicle import Vehicle
from spot_allocation_service import ParkingSpot

vehicle = Vehicle("AS0012", "Small")
parkingSpot1 = ParkingSpot(vehicle)
ticket1 = parkingSpot1.park_vehicle()
print("VEHICLE PARKED:")
print("TICKET INFO:", ticket1.__dict__)
# print(ticket1.__dict__)
print("=====================================")
vehicle = Vehicle("KA0017", "Large")
parkingSpot2 = ParkingSpot(vehicle)
ticket2 = parkingSpot2.park_vehicle()
print("VEHICLE PARKED:")
print("TICKET INFO:", ticket2.__dict__)
# print(ticket2.__dict__)
print("=====================================")
time.sleep(3)
print()
invoice = parkingSpot1.exit_parking()
print("VEHICLE RELEASED:")
print("INVOICE INFO:", invoice.__dict__)
print("=====================================")
print()
invoice = parkingSpot2.exit_parking()
print("VEHICLE RELEASED:")
print("INVOICE INFO:", invoice.__dict__)

