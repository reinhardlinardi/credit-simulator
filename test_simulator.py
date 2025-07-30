import unittest

from enums import Vehicle, Condition
from credit import Credit
from simulator import CreditSimulator

class TestGetAvgMonthly(unittest.TestCase):
    def test_get_avg_monthly(self):
        cr = Credit()
        cr.set_vehicle(Vehicle.CAR)
        cr.set_condition(Condition.USED)
        cr.set_year(2024)
        cr.set_total(100000000)
        cr.set_duration(3)
        cr.set_dp(25000000)

        cs = CreditSimulator()
        cs.set_credit(cr)
        cs.simulate()

        avg = cs.get_avg_monthly()
        self.assertEqual(2441224.5, avg)

if __name__ == '__main__':
    unittest.main()
