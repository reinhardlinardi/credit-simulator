class Error(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)

class VehicleInvalidError(Error):
    pass
    
class ConditionInvalidError(Error):
    pass

class YearInvalidError(Error):
    pass

class NewVehicleYearInvalidError(Error):
    pass

class TotalInvalidError(Error):
    pass

class TotalLimitExceededError(Error):
    pass

class DurationInvalidError(Error):
    pass

class MaxDurationExceededError(Error):
    pass

class DPInvalidError(Error):
    pass

class DPLessThanMinimumError(Error):
    pass
