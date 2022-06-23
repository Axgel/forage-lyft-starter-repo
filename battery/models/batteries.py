from battery.battery import Battery

class SpindlerBattery(Battery):
  def __init__(self, lastDateServiced):
    self.serviceFreq = 2
    super().__init__(lastDateServiced, self.serviceFreq)

class NubbinBattery(Battery):
  def __init__(self, lastDateServiced):
    self.serviceFreq = 4
    super().__init__(lastDateServiced, self.serviceFreq)