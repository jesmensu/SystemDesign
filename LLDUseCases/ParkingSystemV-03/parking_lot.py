import time
from config.config_util import ConfigUtil


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
    

   

