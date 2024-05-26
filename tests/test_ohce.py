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

    def test_reverse_text(self):
        ohce = Ohce(name="Pedro")
        self.assertEqual(ohce.reverse_text("hola"), "aloh")
        self.assertEqual(ohce.reverse_text("oto"), "oto")

    def test_palindrome_recognition(self):
        ohce = Ohce(name="Pedro")
        self.assertEqual(ohce.process_text("oto"), "oto\n¡Bonita palabra!")
    
    def test_stop_recognition(self):
        ohce = Ohce(name="Pedro")
        self.assertEqual(ohce.process_input("Stop"), "Adios Pedro")

    def test_case_insensitive_stop(self):
        ohce = Ohce(name="Pedro")
        self.assertEqual(ohce.process_input("Stop"), "Adios Pedro")
        self.assertEqual(ohce.process_input("STOP"), "Adios Pedro")
        self.assertEqual(ohce.process_input("stop"), "Adios Pedro")
        self.assertEqual(ohce.process_input("StoP"), "Adios Pedro")




if __name__ == '__main__':
    unittest.main()
