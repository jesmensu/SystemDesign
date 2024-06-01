
class Payment:
    @staticmethod
    def calculate_payment(park_time, exit_time, vehicle_type, payment_config):
        duration = exit_time - park_time
        duration = round(duration)
        base_pay = payment_config["BasePayPerHour"][vehicle_type]
        parking_charge = base_pay * duration
        return parking_charge
    
    @staticmethod
    def calculate_pick_hour_payment(park_time, exit_time, vehicle_type, payment_config):
        base_charge = Payment.calculate_payment(park_time, exit_time, vehicle_type, payment_config)
        pick_hour_percent = payment_config["PickHourRatePercent"]
        pick_hour_charge = base_charge + base_charge*pick_hour_percent*0.01
        return pick_hour_charge
    
    @staticmethod
    def calculate_weekend_payment(park_time, exit_time, vehicle_type, payment_config):
        base_charge = Payment.calculate_payment(park_time, exit_time, vehicle_type, payment_config)
        weekend_rate_percent = payment_config["WeekendRatePercent"]
        weekend_charge = base_charge + base_charge*weekend_rate_percent*0.01
        return weekend_charge
