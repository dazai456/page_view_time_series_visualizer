# Page View Time Series Visualizer

## Overview
This project is part of the freeCodeCamp Data Analysis with Python certification. It involves visualizing time series data using a line chart, bar chart, and box plots with the help of Pandas, Matplotlib, and Seaborn libraries. The dataset contains the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03.

## Objective
The goal is to understand the patterns in visits and identify yearly and monthly growth through data visualization.

## Features
- Import data using Pandas and set the index to the date column.
- Clean the data by filtering out days with page views in the top 2.5% or bottom 2.5% of the dataset.
- Visualize the data using:
  - A line chart to show daily freeCodeCamp forum page views over time.
  - A bar chart to display average daily page views for each month grouped by year.
  - Box plots to compare the distribution of values within a given year or month over time.

## Functions
- `draw_line_plot`: Draws a line chart showing daily page views.
- `draw_bar_plot`: Creates a bar chart showing average daily page views per month, grouped by year.
- `draw_box_plot`: Generates box plots to show year-wise and month-wise distribution of page views.

## Development
Write your code in `time_series_visualizer.py`. Use `main.py` to test your functions.

## Testing
Unit tests are provided in `test_module.py`. They will run automatically when you execute the `run` button.

## Submission
Submit your project's URL to freeCodeCamp once you've completed the project.

## Acknowledgments
This project was created as part of the curriculum for the freeCodeCamp Data Analysis with Python certification.