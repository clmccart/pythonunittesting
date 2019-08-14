
class TestSensor:

    def __init__(self, pressure):
        self.pressure = pressure
    
    def sample_pressure(self):
        return self.pressure