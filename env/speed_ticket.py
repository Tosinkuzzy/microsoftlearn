def get_ticket(speed):
    if speed >= 80:
        return "Recklace Driving"
    elif speed > 65:
        return "Speeding"
    else:
        return "Safe"