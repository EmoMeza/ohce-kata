from datetime import datetime

class Ohce:
    def __init__(self, name, current_time=None):
        self.name = name
        self.current_time = current_time if current_time else datetime.now()

    def greet(self):
        hour = self.current_time.hour
        if 20 <= hour or hour < 6:
            return f"¡Buenas noches {self.name}!"
        elif 6 <= hour < 12:
            return f"¡Buenos días {self.name}!"
        else:
            return f"¡Buenas tardes {self.name}!"

    def reverse_text(self, text):
        return text[::-1]

    def process_text(self, text):
        reversed_text = self.reverse_text(text)
        if text == reversed_text:
            return f"{reversed_text}\n¡Bonita palabra!"
        return reversed_text
    
    def process_input(self, text):
        if text == "Stop":
            return f"Adios {self.name}"
        else:
            return self.process_text(text)
    
    def test_empty_input(self):
        ohce = Ohce(name="Pedro")
        self.assertEqual(ohce.process_input(""), "")

    def test_input_with_spaces(self):
        ohce = Ohce(name="Pedro")
        self.assertEqual(ohce.process_input("   "), "   ")

