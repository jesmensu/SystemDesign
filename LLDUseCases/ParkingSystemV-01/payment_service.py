import json
from config.config_util import Config


class Payment:

    @staticmethod
    def calculate_payment(park_time, exit_time, vehicle_type):
        payment_config = Config.get_config("config/payment_config.json")
        duration = exit_time - park_time
        duration = round(duration)
        base_pay = payment_config["BasePayPerHour"][vehicle_type]
        parking_charge = base_pay * duration
        return parking_charge

# class CardPayment(Payment):
#     def calculate_payment(park_time, exit_time, vehicle_type):
#         pass
    
# class CashPayment(Payment):
#     def calculate_payment(park_time, exit_time, vehicle_type):
#         pass