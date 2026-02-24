class Car: 
    #  attributes
    def __init__(self,name, color, model, size):
        self.name = name
        self.color = color
        self.model = model
        self.size = size

    # behavoirs - methods

    def carDescription(self):
    #    print(f"This is a {self.model} it is of color {self.color}")
        pass



toyota = Car("Buddy", "green","Toyota", "4X4")

#  accesed the attributes
output = toyota.name
output = toyota.color
output = toyota.model

#  access ythe behaviours:

toyota.carDescription()

mazda = Car("Kadogo", "blue","MAZDA - XR", "4X4")
mazda.carDescription()

output = f" FIRST CAR: {mazda.name} SECOND-CAR: {toyota.name}"
mazda.name
# INHERITANCE:  You have parent class and a child class( the child class inherits evryhitng form the parent class)


# print("======================")
# print(output)
# print("======================")

"""
CLASS: blueprint that helps create an real object
"""

# defining a Class
class Monitor:
    # attribute
    # shape ="rectangular"
    # resolution="1080"
    # size = "large"
    # yom = 2020

#  an initialize invoked the moment the object is created
    def __init__(self, shape, resolution,size, yom, color):
        self.shape = shape
        self.resolution = resolution
        self.size = size
        self.yom = yom 
        self.color = color 

    # methods (function taht resides inside a class)
    def switchOnMonitor(self):
        print("turning on monitor")

    def displayInterface(self):
        print("diplaying OS")

# OBJECTS: Instances of classes ("a real world thing")
# create objects
hpMonitor = Monitor("rectangular", 1080, 21, 2000, "gray")
dellMonitor = Monitor(shape="oval", resolution=1280, size=34, yom=2020, color="black" )

# hpMonitor.switchOnMonitor()
# dellMonitor.switchOnMonitor()

# print(f"===> {hpMonitor.shape}")
# print(f"===> {dellMonitor.shape}")


"""
- INHERITANCE: 
    get attributes | methods from the parent class

- ENCAPSULATION
- POLYMORPHISM
"""

class Vehicle: 
    # attributes: 
    def __init__(self, model, color, isElectric): 
        self.model = model
        self.color = color
        self.isElectric = isElectric

    # methods
    def carFeatures(self):
        print(f"This vehicle is of model {self.model} it is color {self.color}. Is it electric? {self.isElectric}")
    
    def startCar(self):
        print(f"Starting your {self.model} car!")

tesla = Vehicle("Tesla","Space-Gray", True)
toyota = Vehicle("Toyota", "White", False)

class Tuktuk(Vehicle): # inheritance, the parent is Vehicle an child: Tuktuk
    # attribute
    def __init__(self,model, color, isElectric,numberOfWheels):
        super().__init__(model, color, isElectric) 
        self.numberOfWheels = numberOfWheels 
    
    def wheelNumber(self):
        print(f"Your tuktuk has {self.numberOfWheels} wheels")

redTuktuk = Tuktuk("TKTK", "RED", True,"3")

redTuktuk.carFeatures()
redTuktuk.wheelNumber()

