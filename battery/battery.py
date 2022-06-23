import datetime


class Battery:
    def __init__(self, lastDateServiced, serviceFreq):
      self.lastDateServiced = lastDateServiced 
      self.serviceFreq = serviceFreq
    
    def shouldBeServiced(self):
      serviceThresholdDate = self.lastDateServiced.replace(year=self.lastDateServiced.year + self.serviceFreq)
      return serviceThresholdDate < datetime.today().date()