import time
from payment_service import Payment
from ticketing_service import Ticket
from vehicle import Vehicle
from config.config_util import Config

class ParkingSpot:
    def __init__(self, vehicle: Vehicle, spot_id = None):
        self.vehicle = vehicle
        # self.allocated = False
        self.spot_id = self.get_available_spot(vehicle.vehicle_type) if spot_id == None else spot_id

    def get_available_spot(self, vehicle_type):
        parking_config = Config.get_config("config/parking_lot_config.json")
        if parking_config[vehicle_type]["Available"]:
            spot_id = parking_config[vehicle_type]["Available"].pop(-1)
            Config.set_config("config/parking_lot_config.json", parking_config)
            return spot_id
        else:
            raise ValueError("Spot is not available")
        
    def generate_ticket(self, vehicle, spot_id):
        self.ticket = Ticket(vehicle, spot_id)
        return self.ticket
    
    def create_invoice(self, ticket):
        exit_time = time.time()
        ticket.set_exit_time(exit_time)
        parking_charge = Payment.calculate_payment(ticket.park_time, exit_time, ticket.vehicle_type)
        ticket.set_parking_charge(parking_charge)
        return ticket

    def park_vehicle(self):
        parking_config = Config.get_config("config/parking_lot_config.json")
        parking_config[self.vehicle.vehicle_type]["Occupied"].append(self.spot_id)
        Config.set_config("config/parking_lot_config.json", parking_config)
        ticket = self.generate_ticket(self.vehicle, self.spot_id)
        return self.ticket

    def exit_parking(self):
        parking_config = Config.get_config("config/parking_lot_config.json")
        vehicle_type = self.vehicle.vehicle_type
        parking_config[vehicle_type]["Occupied"].remove(self.spot_id)
        parking_config[vehicle_type]["Available"].append(self.spot_id)
        Config.set_config("config/parking_lot_config.json", parking_config)
        invoice = self.create_invoice(self.ticket)
        return invoice


