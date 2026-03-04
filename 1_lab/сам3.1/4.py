# task 4
age = 25
experience = 5
reputation = 2
traffic = 3
car_brand = "Volkswagen Polo"
duration = 30

tariff = 0

# calculate tariff based on conditions
if car_brand == "Volkswagen Polo":
    if 20 <= age <= 27:
        tariff = 8.5
    elif 27 <= age <= 34:
        if 2 <= experience <= 9:
            tariff = 7.2
        else:
            tariff = 6.9
elif car_brand == "BMW X1":
    if 20 <= age <= 27:
        tariff = 12.0
    elif 27 <= age <= 34:
        tariff = 11.4

price = duration * tariff
print(f"Стоимость вашей поездки составит {price}")
