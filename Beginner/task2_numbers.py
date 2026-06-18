number = 145
formatted_number = format(number, 'o')
print("Question 1")
print("Decimal Number:", number)
print("Octal Representation:", formatted_number)
print("\n-------------------\n")
pi = 3.14
radius = 84
pond_area = pi * radius * radius
water_per_square_meter = 1.4
total_water = pond_area * water_per_square_meter
print("Question 2")
print("Area of Pond:", pond_area, "square meters")
print("Total Water in Pond:", int(total_water), "liters")
print("\n-------------------\n")
distance = 490  # meters
time_minutes = 7
time_seconds = time_minutes * 60
speed = distance / time_seconds
print("Question 3")
print("Speed:", int(speed), "meters/second")