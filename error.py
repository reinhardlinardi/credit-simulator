class ValidationError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)

class InvalidVehicleError(ValidationError):
    pass
    
class InvalidConditionError(ValidationError):
    pass
