import unittest

from datetime import datetime
from credit import Credit
from enums import Vehicle, Condition
from error import *

class TestSet(unittest.TestCase):
    def test_invalid_vehicle(self):
        cr = Credit()

        with self.assertRaises(InvalidVehicleError):
            cr.set_vehicle(10)

    def test_invalid_condition(self):
        cr = Credit()
        cr.set_vehicle(Vehicle.MOTORCYCLE)

        with self.assertRaises(InvalidConditionError):    
            cr.set_condition(-1)

    def test_invalid_year(self):
        cr = Credit()
        cr.set_vehicle(Vehicle.CAR)
        cr.set_condition(Condition.USED)
        
        current_year = datetime.now().year

        with self.assertRaises(InvalidYearError):    
            cr.set_year(current_year+1)

    def test_invalid_new_vehicle_year(self):
        cr = Credit()
        cr.set_vehicle(Vehicle.CAR)
        cr.set_condition(Condition.NEW)
        
        current_year = datetime.now().year

        with self.assertRaises(InvalidYearNewVehicleError):
            cr.set_year(current_year-2)

if __name__ == '__main__':
    unittest.main()
