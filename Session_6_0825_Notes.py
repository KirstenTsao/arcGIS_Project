#3 types of error

number=8
number2=0
try:
    print(number/number2)
except Exception as e: #here the exception is general  
    print(e) #print the exception
print('code continue')


#Objects
class Car():
    """This is a car class"""
    def __init__(self):
        self.name='No Name'
        self.color='white'
        self.door=4
        self.engine='gas'
        self.on= False
        self.speed=0
    
    def trunOn(self):
        self.on=True
        return "Car started"
    
    def turnOff(self):
        self.on=False
        return "Car turned off"
    
    def setSpeed(self,speed):
        self.speed=speed
    
    def brake(self):
        self.speed=0
        return('car stopped')
    
    def horn(self):
        print('HONK')

    def status(self):
        print(f'The {self.door} door {self.color} car called {self.name} is currently {self.on}.')

c1=Car()
c2=Car()
dir(c1)

c1.name="Toyota"
c2.name="Honda"
c1.trunOn()
c1.setSpeed(50)
c1.color='Blue'
c1.status()
c2.status()


#Using the Car object
class Tesla(Car):
    def __init__(self):
        super().__init__() #make sure name, color... are in place
        self.engine='electric'
        self.batterysize=100
        self.color='Black'

c3=Tesla()
c3.name='TeslaTest'
c3.status()