from mocksandstubs.sensor import Sensor

class Alarm(object):

    def __init__(self, sensor=None):
        self._low_pressure_threshold = 17
        self._hihg_pressure_threshold = 21
        self._sensor = sensor or Sensor()
        self._is_alarm_on = False

    def check(self):
        psi_pressure_value = self._sensor.sample_pressure()
        if psi_pressure_value <self._low_pressure_threshold \
            or self._hihg_pressure_threshold < psi_pressure_value:
            self._is_alarm_on = True

    @property
    def is_alarm_on(self):
        return self._is_alarm_on