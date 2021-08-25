"""
The Habit class in the habit module is tested.
"""
from Habitsbox_app.application.habit import Habit

def test_print():
    """
    Attributes of the habit
    """
    habit_yoga = Habit('Yoga', 'weekly', 'flexibility', 'Before lunch')
    assert habit_yoga.name == 'Yoga'
    assert habit_yoga.periodicity == 'weekly'
    assert habit_yoga.motivation == 'flexibility'
    assert habit_yoga.description == 'Before lunch'
