import unittest
from datetime import datetime

from car.models.cars import Calliope, Glissade, Palindrome, Rorschach, Thovex
from battery.models.batteries import SpindlerBattery, NubbinBattery
from engine.models.engines import CapuletEngine, WilloughbyEngine, SternmanEngine

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car_engine = CapuletEngine(last_service_mileage, current_mileage)
        car_battery = SpindlerBattery(last_service_date)

        car = Calliope(car_engine, car_battery)
        self.assertTrue(car.shouldBeServiced())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car_engine = CapuletEngine(last_service_mileage, current_mileage)
        car_battery = SpindlerBattery(last_service_date)

        car = Calliope(car_engine, car_battery)
        self.assertFalse(car.shouldBeServiced())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car_engine = CapuletEngine(last_service_mileage, current_mileage)
        car_battery = SpindlerBattery(last_service_date)

        car = Calliope(car_engine, car_battery)
        self.assertTrue(car.shouldBeServiced())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car_engine = CapuletEngine(last_service_mileage, current_mileage)
        car_battery = SpindlerBattery(last_service_date)

        car = Calliope(car_engine, car_battery)
        self.assertFalse(car.shouldBeServiced())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car_engine = SternmanEngine(0, 0, warning_light_is_on)
        car_battery = SpindlerBattery(last_service_date)

        car = Palindrome(car_engine, car_battery)
        self.assertTrue(car.shouldBeServiced())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        car_engine = SternmanEngine(0, 0, warning_light_is_on)
        car_battery = SpindlerBattery(last_service_date)

        car = Palindrome(car_engine, car_battery)
        self.assertFalse(car.shouldBeServiced())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car_engine = SternmanEngine(0, 0, warning_light_is_on)
        car_battery = SpindlerBattery(last_service_date)

        car = Palindrome(car_engine, car_battery)
        self.assertTrue(car.shouldBeServiced())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car_engine = SternmanEngine(0, 0, warning_light_is_on)
        car_battery = SpindlerBattery(last_service_date)

        car = Palindrome(car_engine, car_battery)
        self.assertFalse(car.shouldBeServiced())

class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        car_battery = NubbinBattery(last_service_date)

        car = Rorschach(car_engine, car_battery)
        self.assertTrue(car.shouldBeServiced())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        car_battery = NubbinBattery(last_service_date)

        car = Rorschach(car_engine, car_battery)
        self.assertFalse(car.shouldBeServiced())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        car_battery = NubbinBattery(last_service_date)

        car = Rorschach(car_engine, car_battery)
        self.assertTrue(car.shouldBeServiced())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        car_battery = NubbinBattery(last_service_date)

        car = Rorschach(car_engine, car_battery)
        self.assertFalse(car.shouldBeServiced())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car_engine = CapuletEngine(last_service_mileage, current_mileage)
        car_battery = NubbinBattery(last_service_date)

        car = Thovex(car_engine, car_battery)
        self.assertTrue(car.shouldBeServiced())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car_engine = CapuletEngine(last_service_mileage, current_mileage)
        car_battery = NubbinBattery(last_service_date)

        car = Thovex(car_engine, car_battery)
        self.assertFalse(car.shouldBeServiced())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car_engine = CapuletEngine(last_service_mileage, current_mileage)
        car_battery = NubbinBattery(last_service_date)

        car = Thovex(car_engine, car_battery)
        self.assertTrue(car.shouldBeServiced())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car_engine = CapuletEngine(last_service_mileage, current_mileage)
        car_battery = NubbinBattery(last_service_date)

        car = Thovex(car_engine, car_battery)
        self.assertFalse(car.shouldBeServiced())


if __name__ == '__main__':
    unittest.main()
