class Error(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)

class InvalidVehicleError(Error):
    pass
    
class InvalidConditionError(Error):
    pass

class InvalidYearError(Error):
    pass

class InvalidYearNewVehicleError(Error):
    pass
