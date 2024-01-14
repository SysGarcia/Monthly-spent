# Monthly-spent

## Overview

Monthly-Spent is a Python application designed to track daily expenses and visualize them in a graph. This simple yet effective tool helps users keep an eye on their spending habits over the course of a month.
## Features

    Daily Expense Input: Allows users to input the amount spent each day.
    Data Storage: Records daily expenses in a text file on the user's desktop.
    Visualization: Generates a scatter plot graph to visualize spending over the month.

## Requirements

    Python 3.x
    Matplotlib library (for graphing)

## Installation

    Ensure Python 3.x is installed on your system.
    Install Matplotlib if you haven't already. You can install it using pip:

    bash

    pip install matplotlib

## Usage

    Run the Monthly-Spent script.
    When prompted, enter the amount you spent for the day. Ensure you enter a positive number.
    The program will record your input in a file named daily.txt on your desktop.
    It then generates and displays a graph showing your spending pattern over the month.

## File Structure

    daily.txt: This file is created on your desktop. It stores the daily spent amounts along with the corresponding dates.

## Code Explanation

* get_value(): Prompts the user for daily expense input and validates it.
* get_desktop(): Determines the path to the user's desktop.
* get_current_date(): Fetches the current date.
* get_lines_document(): Reads the number of lines (entries) in daily.txt.
* add_to_file(): Adds the new entry to daily.txt.
* create_graph(): Generates and displays a graph using Matplotlib.
* get_alltime_money(): Extracts the spent amounts from daily.txt.
* get_alltime_days(): Extracts the dates from daily.txt.

## Contribution

Contributions to this project are welcome. Please fork the repository and submit a pull request with your proposed changes.
