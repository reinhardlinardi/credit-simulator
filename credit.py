from datetime import datetime
from enums import Vehicle, Condition
from error import *

MAX_LIMIT = 1000000000
MAX_DURATION_YEAR = 6

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
            raise VehicleInvalidError('kendaraan tidak valid')
        
        self.vehicle = vehicle
        
    def set_condition(self, condition):
        if condition != Condition.USED and condition != Condition.NEW:
            raise ConditionInvalidError('kondisi tidak valid')
        
        self.condition = condition
        
    def set_year(self, year):
        current_year = datetime.now().year
        if year > current_year:
            raise YearInvalidError('tahun tidak valid')
        
        last_year = current_year-1
        if self.condition == Condition.NEW and year < last_year:
            raise NewVehicleYearInvalidError('kendaraan baru minimal tahun {}'.format(last_year))
        
        self.year = year

    def set_total(self, total):
        if total <= 0:
            raise TotalInvalidError('total pinjaman tidak valid')
        if total > MAX_LIMIT:
            raise TotalLimitExceededError('total pinjaman maksimal 1 milyar')

        self.total = total

    def set_duration(self, duration):
        if duration <= 0:
            raise DurationInvalidError('tenor tidak valid')
        if duration > MAX_DURATION_YEAR:
            raise MaxDurationExceededError('tenor maksimal {} tahun'.format(MAX_DURATION_YEAR))
        
        self.duration = duration

