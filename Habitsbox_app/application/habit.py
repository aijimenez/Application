"""
These module contains the characteristics of a habit
"""
import datetime

class Habit:
    """Information about the characteristics of a habit """

    def __init__(self, name, periodicity, motivation, description):
        """
        Parameters
        ----------
        name : str
            Name of the habit
        periodicity : str
            Periodicity of the habit, daily or weekly
        motivation :
            Motivation of the user to perform the habit
        description :
            Description of the habit
        """
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
