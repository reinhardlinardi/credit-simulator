from datetime import datetime
from enums import Vehicle, Condition
from error import *

class Credit:
    def __init__(self):
        self.vehicle = 0
        self.condition = 0
        self.year = 0
        self.total = 0
        self.duration = 0
        self.dp = 0

    def set(self, vehicle, condition, year, total, duration, dp):
        self._set_vehicle(vehicle)
        self._set_condition(condition)

    def _set_vehicle(self, vehicle):
        if vehicle != Vehicle.MOTORCYCLE and vehicle != Vehicle.CAR:
            raise InvalidVehicleError('kendaraan invalid')
        
    def _set_condition(self, condition):
        if condition != Condition.USED and condition != Condition.NEW:
            raise InvalidConditionError('kondisi invalid')
