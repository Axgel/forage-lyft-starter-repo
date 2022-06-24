from tire.tire import Tire
import random

class Carrigan(Tire):
  def __init__(self):
    self.name = "Carrigan"
  
  def shouldBeServiced(self):
    rand = []
    for i in range(4):
      rand.append(random.uniform(0,1))
    for num in rand:
      if num >= 0.9:
        return True
    return False

class Octoprime(Tire):
  def __init__(self):
    self.name = "Octoprime"
  
  def shouldBeServiced(self):
    rand = []
    for i in range(4):
      rand.append(random.uniform(0,1))
    sumVal = 0
    for num in rand:
      sumVal+=num
    return sumVal >= 3