from vehicle import Vehicle

class ParkingSpot:
    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.allocated = False

    def get_available_spot(self, parking_config):
        vehicle_type = self.vehicle.vehicle_type
        if parking_config[self.vehicle.vehicle_type]["Available"]:
            spot_id = parking_config[vehicle_type]["Available"][-1]
            return spot_id
        else:
            raise ValueError("Spot is not available")
        
    




