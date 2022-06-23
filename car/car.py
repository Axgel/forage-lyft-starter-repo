from battery.battery import Battery
from engine.engine import Engine 

class Car:
    def __init__(self, engine, battery):
      self.engine = engine 
      self.battery = battery 

    def changeBattery(self, newBattery):
      self.battery = newBattery
    
    def changeEngine(self, newEngine):
      self.engine = newEngine
    
    def getBattery(self):
      return self.battery
    
    def getEngine(self):
      return self.engine

    def shouldBeServiced(self):
      return self.engine.shouldBeServiced() or self.battery.shouldBeServiced()