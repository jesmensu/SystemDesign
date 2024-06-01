import time
from parking_lot import ParkingLot
from ticketing_service import Ticket, Invoice
from vehicle import Vehicle
from parking_spot import ParkingSpot
from payment_service import Payment

class User:
    def __init__(self, parkingLot:ParkingLot):
        self.parkingLot = parkingLot

class Customer(User):
    def __init__(self, parkingLot:ParkingLot, vehicle_no, vehicle_type):
        super().__init__(parkingLot)
        self.vehicle = Vehicle(vehicle_no, vehicle_type)

    def park_vehicle(self):
        parkingSpot = ParkingSpot(self.vehicle)
        spot_id = parkingSpot.get_available_spot(self.parkingLot.parking_config)
        self.parkingLot.parking_config[self.vehicle.vehicle_type]["Available"].remove(spot_id)
        self.parkingLot.parking_config[self.vehicle.vehicle_type]["Occupied"].append(spot_id)
        ticket = Ticket(self.vehicle, spot_id)
        return ticket

    def release_vehicle(self, ticket:Ticket):
        vehicle_type = ticket.vehicle_type
        self.parkingLot.parking_config[vehicle_type]["Occupied"].remove(ticket.spot_id)
        self.parkingLot.parking_config[vehicle_type]["Available"].append(ticket.spot_id)
        invoice = self.create_invoice(ticket)
        return invoice
    
    def create_invoice(self, ticket):
        invoice = Invoice(self.vehicle, ticket.spot_id, ticket.ticket_no)
        exit_time = time.time()
        invoice.set_exit_time(exit_time)
        parking_charge = Payment.calculate_payment(ticket.park_time, exit_time, ticket.vehicle_type, self.parkingLot.payment_config)
        invoice.set_parking_charge(parking_charge)
        return invoice
    



class Admin(User):

    def set_base_parking_price(self, vehicle_type, price):
        self.parkingLot.payment_config["BasePayPerHour"][vehicle_type] = price
        return self

    def set_pick_hour(self, pick_hour_start_time, pick_hour_end_time):
        self.parkingLot.payment_config["PickHourStartTime"] = pick_hour_start_time
        self.parkingLot.payment_config["PickHourEndTime"] = pick_hour_end_time
        return self

    def set_pick_hour_rate(self, rate):
        self.parkingLot.payment_config["PickHourRatePercent"] = rate
        return self

    def set_weekend_rate(self, rate):
        self.parkingLot.payment_config["WeekendRatePercent"] = rate
        return self

    def make_reserved_booking(self, no_of_spot, vehicle_type):
        for no in no_of_spot:
            if self.parkingLot.parking_config[vehicle_type]["Available"]:
                spot_id = self.parkingLot.parking_config[vehicle_type]["Available"].pop(-1)
                self.parkingLot.parking_config[vehicle_type]["Reserved"].append(spot_id)
            else:
                print("No more spot available")
                break
        return self

    def resease_reserved_booking(self, no_of_spot, vehicle_type):
        for no in no_of_spot:
            if self.parkingLot.parking_config[vehicle_type]["Reserved"]:
                spot_id = self.parkingLot.parking_config[vehicle_type]["Reserved"].pop(-1)
                self.parkingLot.parking_config[vehicle_type]["Available"].append(spot_id)
            else:
                print("No more spot reserved")
                break
        return self

