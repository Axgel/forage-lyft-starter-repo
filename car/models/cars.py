from battery.models.batteries import SpindlerBattery, NubbinBattery
from engine.models.engines import CapuletEngine, WilloughbyEngine, SternmanEngine
from car.car import Car

class Calliope(Car):
  def __init__(self, engine, battery):
    super().__init__(engine, battery)

class Glissade(Car):
  def __init__(self, engine, battery):
    super().__init__(engine, battery)

class Palindrome(Car):
  def __init__(self, engine, battery):
    super().__init__(engine, battery)

class Rorschach(Car):
  def __init__(self, engine, battery):
    super().__init__(engine, battery)

class Thovex(Car):
  def __init__(self, engine, battery):
    super().__init__(engine, battery)