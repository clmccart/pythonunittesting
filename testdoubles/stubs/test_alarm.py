import unittest
from testdoubles.stubs.alarm import Alarm
from testdoubles.stubs.stub_sensor import TestSensor
from unittest.mock import * 
from testdoubles.stubs.sensor import Sensor

class AlarmTest(unittest.TestCase):

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_alarm_on)

    def test_check_too_low_pressure_sounds_alarm(self):
        alarm = Alarm(sensor=TestSensor(15))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    def test_check_too_high_pressure_sounds_alarm(self):
        alarm = Alarm(sensor=TestSensor(22))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    def test_check_normal_pressure_doesnt_sound_alarm(self):
        alarm = Alarm(sensor=TestSensor(18))
        alarm.check()
        self.assertFalse(alarm.is_alarm_on)

    def test_check_with_pressure_ok_with_mock_fw(self):
        test_sensor = Mock(Sensor)
        test_sensor.sample_pressure.return_value = 18
        alarm = Alarm(test_sensor)
        alarm.check()
        self.assertFalse(alarm.is_alarm_on)

    def test_check_with_too_high_pressure_monkeypatching(self):
        with patch('testdoubles.stubs.alarm.Sensor') as test_sensor_class:
            test_sensor_instance = Mock()
            test_sensor_instance.sample_pressure.return_value = 22
            test_sensor_class.return_value = test_sensor_instance
            alarm = Alarm()
            alarm.check()
            self.assertTrue(alarm.is_alarm_on)
    
    @patch("testdoubles.stubs.alarm.Sensor")
    def test_check_with_too_low_pressure_monkeypatching_decorator(self, test_sensor_class):
        test_sensor_instance = Mock()
        test_sensor_instance.sample_pressure.return_value = 15
        test_sensor_class.return_value = test_sensor_instance
        alarm = Alarm()
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)
