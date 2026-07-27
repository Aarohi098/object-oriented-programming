#create class
class Vehicle:
    #create init method
    def __init__(self, maxspeed, mileage):
        #bind the arguements
        self.maxspeed = maxspeed
        self.mileage = mileage
        
#object creation
modelX = Vehicle(240, 18)
#access variables inside init method
print("Max speed is", modelX.maxspeed)
print("Mileage is", modelX.mileage)