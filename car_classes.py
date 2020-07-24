# Create a Car class with custom speed, acceleration, and weight.
# Add a drive function that adds speed to the car with the formula:
#        speed_increase = acceleration * weight
# Instantiate multiple car models with different attributes and race them against each other. 

class Car():
    def __init__(self, acceleration, weight, max_speed):
        self.current_speed = 0
        self.acceleration = acceleration
        self.weight = weight
        self.max_speed = max_speed
    def drive(self):
        speed_increase = self.acceleration  / self.weight / 2

        if self.current_speed <= self.max_speed:
            self.current_speed += speed_increase
        
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        print('The car is driving at', self.current_speed, 'kmph.')
            

        
toyota = Car(0.5, 1.8, 70)
ford = Car(0.4, 2.4, 90)
porsche = Car(1.8, 0.9, 120)
ferrari = Car(2.2, 1.0, 210)

while True:
    toyota.drive()
    ford.drive()
    porsche.drive()
    ferrari.drive()

    if ferrari.current_speed >= ferrari.max_speed:
        break

print("Finished!")
