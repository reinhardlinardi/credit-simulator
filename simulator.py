from enums import Vehicle

CAR_BASE_RATE = 8
MOTORCYCLE_BASE_RATE = 9

class CreditSimulator:
    def __init__(self):
        self.credit = None
        self.details = []

    def set_credit(self, credit):
        self.credit = credit

    def get_details(self):
        return self.details
    
    def get_avg_monthly(self):
        sum = 0

        for detail in self.details:
            sum += detail.yearly

        return sum / (12 * self.credit.duration)

    def simulate(self):
        c = self.credit
        base = c.total - c.dp
        
        if c.vehicle == Vehicle.MOTORCYCLE:
            rate = MOTORCYCLE_BASE_RATE
        elif c.vehicle == Vehicle.CAR:
            rate = CAR_BASE_RATE
        
        for elapsed in range(0, c.duration):
            d = Details()
            d.base = base
            d.rate = rate

            d.total = d.base + d.base * d.rate / 100
            d.monthly = d.total / (12 * (c.duration - elapsed))
            d.yearly = d.monthly * 12

            self.details.append(d)
            base = d.total - d.yearly

            if elapsed % 2 == 0:
                rate += 0.1
            else:
                rate += 0.5

class Details:
    def __init__(self):
        self.base = 0
        self.rate = 0
        self.total = 0
        self.monthly = 0
        self.yearly = 0
