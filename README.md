# Habitsbox Application

## Description

The Habitsbox Application allows users to create and track their daily and weekly habits, providing analysis of the trackings recorded.

## Table of contents
* [Screenshots](#Screenshots)
* [Features](#Features)
* [Prerequisites](#Prerequisites)
* [Dependencies](#Dependencies)
* [Installation](#Installation)
* [Usage](#Usage)
* [Documentation](#Documentation)
* [Testing](#Testing)
* [Links](#Links)

## Screenshots

![Analytics](./images/screenshoot1.png)
![Analytics](./images/screenshoot2.png)
![Analytics](./images/screenshoot3.png)

## Features

* Creation and deletion of habits
* Two different periodicities; daily and weekly
* Individual habit information
* Information on all recorded habits divided by tracked und untracked habits
* Information on habits by periodicity
* Counting days or weeks of activity according to periodicity
* Longest streak for each tracked habit
* Longest streak of all tracked habits
* Part of the day when the habit is performed most of the time

## Prerequisites
* Python version 3.7  
## Dependencies  
* PyInputPlus

## Installation

**Step 1: Install python**  

The application is built using Python version 3.7. Before start using the application, it is neccesary to [install Python](https://www.python.org/downloads/) . 

**Step 2: Install dependencies**  

Use ``pip`` to install PyInputPlus
```
pip install pyinputplus
```
On macOS and Linux
```
pip3 install pyinputplus
```

**Step 3: Download the source code**  

Clone or download the source code from ``git``. To clone the source code repository, open the command line interpreter, navigate to the desired folder, the run:
```
git clone https://github.com/aijimenez/Application.git
```

**Step 4: Run the application**  

1. Navigate to the directory ``Application``
```
cd Application\Habitsbox_app
```
2. Run
```
python menu.py
```

3. Result image  

The Habitsbox application includes five predefined habits. Three of them are daily and two are weekly. Each habit has tracking data for a four-week period.

![Five habits](./images/five_habits.png)

**Step 5: Exit the application**

To exit the application you must press the number zero once if you are in the main menu, twice if you are using any of the menu options.

## Usage

**Optional Step: Delete the five default habits**

To use the application without the five default habits

1. Navigate to the directory ``Application``
```
cd Application\Habitsbox_app
```
2. Delete all predefined habits before running the application

```
del DB_Habitsbox_app.db
```
3. Run the application
```
python menu.py
```
4. First image

Once the predefined habits have been deleted, this will be the first image.

![First habit](./images/welcome.png)

**Step 1: Create a habit**

1. Choose the option ``Add a new habit`` with the number 1 and press enter.

2. Write the name of your habit, choose the frecuency, write your motivation and a short description of the habit.

3. At the end of your habit registration there will be a confirmation.

![Confirmation](./images/Added_habit_confirmation.png)

4. If you wish you can add another habit by pressing number 1 or return to the main menu with number zero.

**Step 2: Check a habit off**

For a better analysis, it is necessary to check your habit off immediately after you have done it.

1. To mark a habit as done, choose the option ``Check a habit off`` in the main menu with the number 2 and press enter.

2. Choose the id that corresponds to the habit you want to check off and press enter.

3. You will receive a confirmation that your habit has been checked off.

_Daily habits:_ The habit is expected to be performed every day without exception, the time is not important just make sure you perform it before the end of the day and mark it immediately after you have done it. Two or more check-off on the same day will count as one.

_Weekly habits:_ The habit should be marked as done on any day of the week. The beginning of each week does not depend on when you first checked your habit off. A week starts on Monday and ends on Sunday. Two or more check-off in the same week will count as one. 

_Streak_ The number of consecutive days or weeks in which the habit has been marked as done. The minimum streak is 1 and consists of a single check-off.

**Option: Delete a habit**

The chosen habit and its trackings will be permanently erase.

1. To delete a habit and its trackings, choose the option ``Delete a habit`` in the main menu with the number 3 and press enter.

2. Type the name of the habit you wish to delete in upper or lower case and press enter.

3. A confirmation that your habit has been deleted will appear.

**Option: See a habit**

With this option you will be able to see the information of your registered habits individually by choosing only the id of the habit you want to see.

**Option: See all habits registered**

This option appears in the main menu after two registered habits.

Here you can see all the registered habits along with the information entered at the time of registration. The registered habits are separated into tracked and untracked habits.

**Option: See habits with same periodicity**

This option appears in the main menu after two registered habits.

It allows you to see all the habits that have the same periodicity. Trackings analysis will be shown for tracked habits. If the habit has no trackings, you will only be able to see the information you provided at the time of registration.

**Option: See my longest streak of all habits**

This option will be displayed only when you have two or more registered habits and when at least one of them has at minimum one tracking.

Here you can see the name of the habit with the longest streak of all habits and its streak. All habit streaks with daily and weekly trackings are compared.

**Back to the main menu**

Once you have selected a menu option you can always return to the main menu by typing the number zero and pressing enter. This action can be carried out regardless of whether or not the selected option has been completed.

## Documentation  

The documentation for the application was generated using ``pydoc`` and can be found at ``Application\docs``. 

## Testing

The application was tested with Pytest version 6.2, the tests can be found in ``Application\tests``. To run the tests, follow the instructions below.  

**Step 1: Install Pytest**

Use ``pip`` to install PyInputPlus
```
pip install pytest==6.2
```

**Step 2: Run the tests**   

1. Navigate to the directory ``Application``
```
cd Application
```
If you already run the application and you are in ``Habitsbox_app`` directory, go back to the ``Application`` directory

```
cd ..
```
2. Run the tests
```
pytest -vv
```
## Links