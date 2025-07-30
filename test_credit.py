import unittest

from datetime import datetime
from enums import Vehicle, Condition
from credit import *
from error import *

class TestSet(unittest.TestCase):
    def test_vehicle_invalid(self):
        cr = Credit()

        with self.assertRaises(VehicleInvalidError):
            cr.set_vehicle(10)

    def test_condition_invalid(self):
        cr = Credit()
        cr.set_vehicle(Vehicle.MOTORCYCLE)

        with self.assertRaises(ConditionInvalidError):    
            cr.set_condition(-1)

    def test_year_invalid(self):
        cr = Credit()
        cr.set_vehicle(Vehicle.CAR)
        cr.set_condition(Condition.USED)
        
        current_year = datetime.now().year

        with self.assertRaises(YearInvalidError):    
            cr.set_year(current_year+1)

    def test_new_vehicle_year_invalid(self):
        cr = Credit()
        cr.set_vehicle(Vehicle.CAR)
        cr.set_condition(Condition.NEW)
        
        current_year = datetime.now().year

        with self.assertRaises(NewVehicleYearInvalidError):
            cr.set_year(current_year-2)

    def test_total_invalid(self):
        cr = Credit()
        cr.set_vehicle(Vehicle.MOTORCYCLE)
        cr.set_condition(Condition.USED)
        cr.set_year(2022)

        with self.assertRaises(TotalInvalidError):
            cr.set_total(0)

    def test_total_limit_exceeded(self):
        cr = Credit()
        cr.set_vehicle(Vehicle.MOTORCYCLE)
        cr.set_condition(Condition.USED)
        cr.set_year(2022)

        with self.assertRaises(TotalLimitExceededError):
            cr.set_total(MAX_LIMIT+1)

    def test_duration_invalid(self):
        cr = Credit()
        cr.set_vehicle(Vehicle.MOTORCYCLE)
        cr.set_condition(Condition.USED)
        cr.set_year(2022)
        cr.set_total(10000000)

        with self.assertRaises(DurationInvalidError):
            cr.set_duration(0)

    def test_max_duration_exceeded(self):
        cr = Credit()
        cr.set_vehicle(Vehicle.MOTORCYCLE)
        cr.set_condition(Condition.USED)
        cr.set_year(2022)
        cr.set_total(10000000)

        with self.assertRaises(MaxDurationExceededError):
            cr.set_duration(MAX_DURATION_YEAR+1)
    

if __name__ == '__main__':
    unittest.main()
