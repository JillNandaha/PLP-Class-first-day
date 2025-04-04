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
