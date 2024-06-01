import time
from payment_service import Payment

increamented_ticket_no = 0
class Ticket:
    def __init__(self, vehicle, spot_id, ticket_no = None):
        self.vehicle_no = vehicle.vehicle_no
        self.vehicle_type = vehicle.vehicle_type
        self.park_time = time.time()
        self.ticket_no = self.get_ticket_no() if ticket_no == None else ticket_no
        self.spot_id = spot_id

    def get_ticket_no(self):
        global increamented_ticket_no
        increamented_ticket_no += 1
        return increamented_ticket_no
    
    def set_park_time(self, park_time):
        self.park_time = park_time
    
    def print_info(self):
        print("Ticket No:", self.ticket_no)
        print("Vehicle No: ", self.vehicle_no)
        print("Vehicle Type: ", self.vehicle_type)
        print("Parking Spot No: ", self.spot_id)
        print("Parking Time: ", self.park_time)
    

class Invoice(Ticket):
    def __init__(self, vehicle, spot_id, ticket_no):
        super().__init__(vehicle, spot_id, ticket_no)

    def set_exit_time(self, exit_time):
        self.exit_time = exit_time

    def set_parking_charge(self, parking_charge):
        self.parking_charge = parking_charge



    def print_info(self):
        print("Ticket No:", self.ticket_no)
        print("Vehicle No: ", self.vehicle_no)
        print("Vehicle Type: ", self.vehicle_type)
        print("Parking Spot No: ", self.spot_id)
        print("Parking Time: ", self.park_time)
        print("Exit Time: ", self.exit_time)
        print("Parking duration: ", self.exit_time - self.park_time)
        print("Parking Charge: ", self.parking_charge)
        
