"""
https://www.practicepython.org
MichelePratusevich

Exercise 36: Birthday Plots
3 chilis

This exercise is Part 4 of 4 of the birthday data exercise series. The other
exercises are: Part 1, Part 2, and Part 3.

In the previous exercise we counted how many birthdays there are in each
month in our dictionary of birthdays.

In this exercise, use the bokeh Python library to plot a histogram of which
months the scientists have birthdays in! Because it would take a long time
for you to input the months of various scientists, you can use my scientist
birthday JSON file. Just parse out the months (if you don’t know how, I
suggest looking at the previous exercise or its solution) and draw your histogram.

If you are using a purely web-based interface for coding, this exercise won’t
work for you, since it requires installing the bokeh Python package. Now might
be a good time to install Python on your own computer.

http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html

"""

import json
import sys
from collections import Counter
from bokeh.plotting import figure, show, output_file


def get_birthdays(file):
    with open(file) as birthday_list_file:
       return(json.load(birthday_list_file))

if __name__ == '__main__':

    if len(sys.argv) == 2:
        file = str(sys.argv[1])
    else:
        file = 'birthdays.json'
    birthdays = get_birthdays(file)

    # my json file entries are mmm dd, yyyy format
    months = Counter([item.split()[0] for item in birthdays.values()])
    monthsk = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'Septmber', 'October', 'November', 'December']
    monthsv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for k, v in months.items():
        if k == "January":
            monthsv[0] = v
        elif k == "February":
            monthsv[1] = v
        elif k == "March":
            monthsv[2] = v
        elif k == "April":
            monthsv[3] = v
        elif k == "May":
            monthsv[4] = v
        elif k == "June":
            monthsv[5] = v
        elif k == "July":
            monthsv[6] = v
        elif k == "August":
            monthsv[8] = v
        elif k == "September":
            monthsv[9] = v
        elif k == "October":
            monthsv[10] = v
        elif k == "November":
            monthsv[11] = v
        elif k == "December":
            monthsv[11] = v
    
    output_file("birthday_plot.html")
    p = figure(x_range=monthsk)
    p.vbar(x=monthsk, top=monthsv, width=0.5)
    show(p)
