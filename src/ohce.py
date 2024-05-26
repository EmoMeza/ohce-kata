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
        reversed_text = text[::-1]
        if text == reversed_text:
            return f"{reversed_text}\n¡Bonita palabra!"
        return reversed_text