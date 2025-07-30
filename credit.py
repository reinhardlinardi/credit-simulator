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

    def set_vehicle(self, vehicle):
        if vehicle != Vehicle.MOTORCYCLE and vehicle != Vehicle.CAR:
            raise InvalidVehicleError('kendaraan tidak valid')
        
        self.vehicle = vehicle
        
    def set_condition(self, condition):
        if condition != Condition.USED and condition != Condition.NEW:
            raise InvalidConditionError('kondisi tidak valid')
        
        self.condition = condition
        
    def set_year(self, year):
        current_year = datetime.now().year
        if year > current_year:
            raise InvalidYearError('tahun tidak valid')
        
        last_year = current_year-1
        if self.condition == Condition.NEW and year < last_year:
            raise InvalidYearNewVehicleError('kendaraan baru minimal tahun {}'.format(last_year))
        
        self.year = year

