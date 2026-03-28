class BMW:
    def fuel_type(self):
        print("BMW uses Diesel.")

    def max_speed(self):
        print("BMW max speed is 240 km/h.")

class Ferrari:
    def fuel_type(self):
        print("Ferrari uses Petrol.")

    def max_speed(self):
        print("Ferrari max speed is 340 km/h.")

# Creating objects
bmw_car = BMW()
ferrari_car = Ferrari()

# Polymorphism in action: treating different objects the same way
for car in (bmw_car, ferrari_car):
    car.fuel_type()
    car.max_speed()
    print("-" * 20)
