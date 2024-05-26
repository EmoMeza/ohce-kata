import unittest
from datetime import datetime
from src.ohce import Ohce

class TestOhce(unittest.TestCase):

    def test_greeting_night(self):
        ohce = Ohce(name="Pedro", current_time=datetime.strptime("22:00", "%H:%M"))
        self.assertEqual(ohce.greet(), "¡Buenas noches Pedro!")

    def test_greeting_morning(self):
        ohce = Ohce(name="Pedro", current_time=datetime.strptime("07:00", "%H:%M"))
        self.assertEqual(ohce.greet(), "¡Buenos días Pedro!")

    def test_greeting_afternoon(self):
        ohce = Ohce(name="Pedro", current_time=datetime.strptime("15:00", "%H:%M"))
        self.assertEqual(ohce.greet(), "¡Buenas tardes Pedro!")

if __name__ == '__main__':
    unittest.main()
