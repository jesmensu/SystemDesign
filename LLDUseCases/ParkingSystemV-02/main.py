from parking_lot_system import ParkingLot
from admin_service import Admin
import time


parkingLot = ParkingLot.getInstance("config")
ticket = parkingLot.park_vehicle("AS0021", "Small")
print("VEHICLE PARKED")
print("TICKET INFO: ", ticket.__dict__)

time.sleep(3)
invoice = parkingLot.release_vehicle(ticket)
print("VEHICLE RELEASED")
print("INVOICE INFO: ", invoice.__dict__)



ticket = parkingLot.park_vehicle("KA0190", "Large")
print("VEHICLE PARKED")
print("TICKET INFO: ", ticket.__dict__)

time.sleep(2)
invoice = parkingLot.release_vehicle(ticket)
print("VEHICLE RELEASED")
print("INVOICE INFO: ", invoice.__dict__)





admin = Admin()
admin.set_base_parking_price("Small",35, parkingLot)
admin.set_base_parking_price("Large", 65, parkingLot)
admin.set_weekend_rate(15, parkingLot)

# admin = admin.set_base_parking_price("Small",35, parkingLot).set_base_parking_price("Large", 65, parkingLot).set_weekend_rate(15, parkingLot)
print("Updated Payment Config")
print(parkingLot.payment_config)