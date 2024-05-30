from admin_service import Admin

admin = Admin()
new_config = admin.set_parking_price("Car",35).set_parking_price("Bus", 65).set_weekend_rate(15)
        
