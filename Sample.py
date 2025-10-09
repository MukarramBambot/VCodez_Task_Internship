# Task 16 - Multiple & Multilevel Inheritance in Python (User Input Version)

print("### MULTIPLE & MULTILEVEL INHERITANCE ###\n")

# ---------- User Input Section ----------
brand = input("Enter Vehicle Brand: ")
model = input("Enter Vehicle Model: ")
battery_capacity = input("Enter Battery Capacity (in kWh): ")

print("\n" + "-" * 80 + "\n")

# ----------------- MULTILEVEL INHERITANCE -----------------
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def show_brand(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):  # inherits from Vehicle
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def show_model(self):
        print(f"Model: {self.model}")

class ElectricCar(Car):  # inherits from Car (multilevel)
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    def show_info(self):
        print("### Multilevel Inheritance Example ###")
        self.show_brand()
        self.show_model()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Create object for Multilevel Inheritance
tesla = ElectricCar(brand, model, battery_capacity)
tesla.show_info()

print("\n" + "-" * 80 + "\n")

# ----------------- MULTIPLE INHERITANCE -----------------
class Engine:
    def engine_info(self):
        print("Engine Type: Electric Dual Motor")

class Battery:
    def battery_info(self):
        print(f"Battery Type: Lithium-ion ({battery_capacity} kWh)")

class TeslaModelX(Engine, Battery):  # multiple inheritance
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_info(self):
        print("### Multiple Inheritance Example ###")
        print(f"Car Name: {self.brand} {self.model}")

# Create object for Multiple Inheritance
car = TeslaModelX(brand, model)
car.car_info()
car.engine_info()
car.battery_info()

print("\n" + "-" * 80)
print("Program executed successfully ✅")
