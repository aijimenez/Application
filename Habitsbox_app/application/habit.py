import datetime

class Habit:
    """Represents a habit in the Habitsbox"""
    
    def __init__(self, name, periodicity, motivation, description):
        self.name = name
        self.periodicity = periodicity
        self.motivation = motivation
        self.description = description
        self.creation_date = datetime.date.today()
    
    def __str__(self):
        return "Habit({}, {}, {}, {})".format(self.name, 
                                          self.periodicity, 
                                          self.motivation, 
                                          self.description)
