import time
from config.config_util import ConfigUtil
from payment_service import Payment
from ticketing_service import Ticket
from vehicle import Vehicle
from parking_spot import ParkingSpot


class ParkingLot:
    __instance = None
    def __init__(self, config_folder):
        self.parking_config = ConfigUtil.get_config(config_folder + "/parking_lot_config.json")
        self.payment_config = ConfigUtil.get_config(config_folder + "/payment_config.json")

    @staticmethod 
    def getInstance(config_folder):
        # Singleton pattern used with this method
        if ParkingLot.__instance == None:
            ParkingLot.__instance = ParkingLot(config_folder)
        return ParkingLot.__instance
    

    def park_vehicle(self, vehicle_no, vehicle_type):
        vehicle = Vehicle(vehicle_no, vehicle_type)
        parkingSpot = ParkingSpot(vehicle)
        spot_id = parkingSpot.get_available_spot(self.parking_config)
        self.parking_config[vehicle_type]["Available"].remove(spot_id)
        self.parking_config[vehicle_type]["Occupied"].append(spot_id)
        ticket = Ticket(vehicle, spot_id)
        return ticket

    def release_vehicle(self, ticket:Ticket):
        vehicle_type = ticket.vehicle_type
        self.parking_config[vehicle_type]["Occupied"].remove(ticket.spot_id)
        self.parking_config[vehicle_type]["Available"].append(ticket.spot_id)
        invoice = self.create_invoice(ticket)
        return invoice
    
    def create_invoice(self, ticket):
        exit_time = time.time()
        ticket.set_exit_time(exit_time)
        parking_charge = Payment.calculate_payment(ticket.park_time, exit_time, ticket.vehicle_type, self.payment_config)
        ticket.set_parking_charge(parking_charge)
        return ticket

