#base class with protected attributes
class Car:
    def __init__(self, brand, model, year, top_speed):
        self.brand = brand
        self.model = model
        self.year = year
        self._top_speed = top_speed         # Protected attribute
        self.__engine_on = False            # Private attribute

    def start_engine(self):
        self.__engine_on = True
        print(f"{self.brand} {self.model} engine started.")

    def stop_engine(self):
        self.__engine_on = False
        print(f"{self.brand} {self.model} engine stopped.")

    def is_engine_on(self):  # Getter for private variable
        return self.__engine_on

    def accelerate(self):
        if self.__engine_on:
            print(f"{self.brand} {self.model} is accelerating to {self._top_speed} km/h!")
        else:
            print("Start the engine first!")

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model} - Top Speed: {self._top_speed} km/h")


##inheritance and polymorphism
class ElectricCar(Car):
    def __init__(self, brand, model, year, top_speed, battery_range):
        super().__init__(brand, model, year, top_speed)
        self.battery_range = battery_range

    def charge(self):
        print(f"{self.brand} {self.model} is charging...")

    def accelerate(self):  # Polymorphism: overriding parent method
        if self.is_engine_on():
            print(f"{self.brand} {self.model} zooms silently to {self._top_speed} km/h with electric torque!")
        else:
            print("Start the engine first!")


class SportsCar(Car):
    def __init__(self, brand, model, year, top_speed, horsepower):
        super().__init__(brand, model, year, top_speed)
        self.horsepower = horsepower

    def turbo_boost(self):
        print(f"{self.brand} {self.model} activates turbo boost with {self.horsepower} HP!")

    def accelerate(self):  # Polymorphism
        if self.is_engine_on():
            print(f"{self.brand} {self.model} ROARS to {self._top_speed} km/h in seconds!")
        else:
            print("Start the engine first!")


#to test the classes
# Create instances
my_ev = ElectricCar("Tesla", "Model S", 2023, 250, "600km")
my_sports = SportsCar("Ferrari", "F8", 2022, 340, 710)

# Display info
my_ev.display_info()
my_sports.display_info()

# Try actions
my_ev.start_engine()
my_ev.accelerate()
my_ev.charge()

print("---")

my_sports.start_engine()
my_sports.accelerate()
my_sports.turbo_boost()
