def cars(manufacturer, model, **car_details):
    """describes a car"""
    car_details['manufacturer'] = manufacturer
    car_details['model'] = model
    return car_details

car = cars('ferrari', 'laferrari', color='red', tow_package= 'wtf?')
print(car)