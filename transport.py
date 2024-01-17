class transport:
    def __init__(self, brand: str, model: str, color: str) :
        self.brand = brand
        self.model = model
        self.color = color

    def setting(self, brand: str, model: str, color: str):
        self.brand = brand
        self.model = model
        self.color = color

    def get_info(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nColor: {self.color}\n"

class car(transport):
    def __init__(self,brand: str, model: str, color: str) :
        super().__init__(brand, model, color)
    
    def set_speed(self, new_speed: int):
        self.speed = new_speed
        
    def set_num_seat(self, num_seat: int):
        self.num_seat = num_seat

    def set_manifactured_date(self, manifactured_date: str):
        self.man_date = manifactured_date
        
    def get_info(self):
        return super().get_info() + f"Num seats: {str(self.num_seat)}\nSpeed: {str(self.speed)}\nMan.Date: {self.man_date}\n"

class truck(transport):
    def __init__(self, brand: str, model:str, color: str):
        super().__init__(brand, model, color)
        
    def set_weight_capacity(self, weight_capacity: float):
        self.weight_capacity = weight_capacity

    def get_info(self):
        return super().get_info() + f"Weight capacity: {self.weight_capacity}\n"

car1 = car(brand="Chevrolet", model="Nexia 2", color="Summit white")
car2 = car(brand="Chevrolet", model="Lacceti", color="Metalic black")

truck1 = truck(brand="Ford", model="Ranger", color="Velocity blue")

truck1.set_weight_capacity(500)
car1.set_manifactured_date('01.01.2008')
car1.set_num_seat(4)
car1.set_speed(200)

print(truck1.get_info())
print(car1.get_info())