class soldier:
    def __init__(self, gender: str, height: float, weight: float, age: int) :
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age

class army:
    def __init__(self, soldier: soldier):
        self.soldier = soldier

    def call_up(self):
        if self.soldier.age >= 18 and self.soldier.gender == 'Male':
            if self.soldier.height < 150 and self.soldier.weight < 75:
                return 'Infantry soldiers'
            else:
                return 'Tank troops'
        else:
            return 'You are not old enough or Female'
        
soldier1 = soldier('Male', 175, 95, 18)
entity = army(soldier=soldier1)

print(entity.call_up())