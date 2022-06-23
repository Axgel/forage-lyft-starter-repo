from engine.engine import Engine
from engine.state import State

class CapuletEngine(Engine):
    def __init__(self, lastServiceMileage, currentMileage):
      self.serviceMileage = 30000
      self.hasIndicator = False
      self.indicator = State.NORMAL
      super().__init__(lastServiceMileage, currentMileage, self.serviceMileage, self.hasIndicator, self.indicator)

class WilloughbyEngine(Engine):
    def __init__(self, lastServiceMileage, currentMileage):
      self.serviceMileage = 60000
      self.hasIndicator = False
      self.indicator = State.NORMAL
      super().__init__(lastServiceMileage, currentMileage, self.serviceMileage, self.hasIndicator, self.indicator)

class SternmanEngine(Engine):
    def __init__(self, lastServiceMileage, currentMileage, indicator):
      self.serviceMileage = 0
      self.hasIndicator = True
      super().__init__(lastServiceMileage, currentMileage, self.serviceMileage, self.hasIndicator, indicator)