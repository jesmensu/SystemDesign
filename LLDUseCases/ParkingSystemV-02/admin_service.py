from parking_lot import ParkingLot

class Admin:
    def __init__(self):
        pass

    def set_base_parking_price(self, vehicle_type, price, parkingLot:ParkingLot):
        parkingLot.payment_config["BasePayPerHour"][vehicle_type] = price
        return self

    def set_pick_hour(self, start_time, end_time, parkingLot:ParkingLot):
        parkingLot.payment_config["PickHourStartTime"] = start_time
        parkingLot.payment_config["PickHourEndTime"] = end_time
        return self

    def set_pick_hour_rate(self, rate, parkingLot:ParkingLot):
        parkingLot.payment_config["PickHourRatePercent"] = rate
        return self

    def set_weekend_rate(self, rate, parkingLot:ParkingLot):
        parkingLot.payment_config["WeekendRatePercent"] = rate
        return self

    def make_reserved_booking(self, no_of_spot, vehicle_type, parkingLot:ParkingLot):
        for no in no_of_spot:
            if parkingLot.parking_config[vehicle_type]["Available"]:
                spot_id = parkingLot.parking_config[vehicle_type]["Available"].pop(-1)
                parkingLot.parking_config[vehicle_type]["Reserved"].append(spot_id)
            else:
                print("No more spot available")
                break
        return self

    def resease_reserved_booking(self, no_of_spot, vehicle_type, parkingLot:ParkingLot):
        for no in no_of_spot:
            if parkingLot.parking_config[vehicle_type]["Reserved"]:
                spot_id = parkingLot.parking_config[vehicle_type]["Reserved"].pop(-1)
                parkingLot.parking_config[vehicle_type]["Available"].append(spot_id)
            else:
                print("No more spot reserved")
                break
        return self

