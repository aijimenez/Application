import pytest
from application.habit import Habit

def test_print():
    habit1 = Habit('Yoga', 'weekly', 'flexibility', 'Before lunch')
    assert habit1.name == 'Yoga'
    assert habit1.periodicity == 'weekly'
    assert habit1.motivation == 'flexibility'
    assert habit1.description == 'Before lunch'

