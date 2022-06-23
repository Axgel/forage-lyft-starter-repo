from engine.state import State

class Engine:
    def __init__(self, lastServiceMileage, currentMileage, serviceMileage, hasIndicator, indicator):
      self.lastServiceMileage = lastServiceMileage
      self.currentMileage = currentMileage
      self.serviceMileage = serviceMileage
      self.hasIndicator = hasIndicator
      self.indicator = indicator

    def shouldBeServiced(self):
        if self.hasIndicator:
          return self.indicator == State.WARNING
        return self.currentMileage - self.lastServiceMileage > self.serviceMileage
