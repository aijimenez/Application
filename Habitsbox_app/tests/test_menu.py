
from application.menu import Menu
from unittest import mock


@mock.patch("application.menu.Menu.run.choose_menu.analytics.get_all_names")
def test_choose_menu(mock_habits_names):
    mock_habits_names.return_value = ['Yoga']
    assert Menu.run.choose_menuchoose_menu() == 'One habit'

    # def choose_menu(self):
    #     habits_names = self.analytics.get_all_names()
    #     # return []
    #     # return ['Yoga']
    #     number_of_habits = len(habits_names)
    #     if number_of_habits == 0:
    #         print('No habits')
    #     elif number_of_habits == 1:
    #         print('One habit')
    #     else:
    #         print('Many habits')
    
    # def get_all_habits(self):
    #     """Return all the habits and all the fields
    #     available in the table habits in the DB"""
    #     self.cursor.execute("SELECT * FROM habits")
    #     return self.cursor.fetchall()
    
    # def get_all_names(self):
    #     """Return the names of the habits in a list"""
    #     all_habits = self.get_all_habits()
    #     if len(all_habits) >= 1:
    #         return [habit[1] for habit in all_habits]
    #     else:
    #         return []

# import mock
# import pytest
# from pytest_mock import mocker
# from application.menu import Menu

# def test_choose_menu(mocker):
#     mocker.patch.object(Menu.run.choose_menu, )

