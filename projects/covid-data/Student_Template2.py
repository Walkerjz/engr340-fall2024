import sys
import pandas as pd
import numpy as np
from numpy.ma.core import argmax


def first_question():
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    #Note that the parsing code was modified to return the Rockingham and Harrisonburg data

    Rstartdate = Rock.iloc[[0], [0]].to_numpy()
    print("The first positive in Rockingham County was: ")
    print(str(Rstartdate[0]))

    Hstartdate = Hburg.iloc[[0], [0]].to_numpy()
    "The first positive in Harrisonburg City was: "
    print(str(Hstartdate[0]))

def second_question():
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    Rock_cases = Rock['cases'].to_numpy()
    Hburg_cases = Hburg['cases'].to_numpy()

    Rinit = np.concatenate((Rock_cases, [0]), axis=0)
    Hinit = np.concatenate((Hburg_cases, [0]), axis=0)

    Rsub = np.concatenate(([0], Rock_cases), axis=0)
    Hsub = np.concatenate(([0], Hburg_cases), axis=0)

    dRock = Rinit - Rsub
    dHburg = Hinit - Hsub

    # remove the last entry its a 0- last number that doesn't mean anything to us
    dRock = np.delete(dRock, [-1])
    dHburg = np.delete(dHburg, [-1])

    Rock_argmax = argmax(dRock)
    Hburg_argmax = argmax(dHburg)

    Rock_worst_day = Rock.iloc[[Rock_argmax], [0]].to_numpy()
    Hburg_worst_day = Hburg.iloc[[Hburg_argmax], [0]].to_numpy()

    print(str(Rock_worst_day[0]))
    print(str(Hburg_worst_day[0]))
    return

def third_question():
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    Rock_cases = Rock['cases'].to_numpy()
    Hburg_cases = Hburg['cases'].to_numpy()

    Rinit = np.concatenate((Rock_cases, [0]), axis=0)
    Hinit = np.concatenate((Hburg_cases, [0]), axis=0)

    Rsub = np.concatenate(([0], Rock_cases), axis=0)
    Hsub = np.concatenate(([0], Hburg_cases), axis=0)

    dRock = Rinit - Rsub
    dHburg = Hinit - Hsub

    # remove the last entry its a 0- last number that doesn't mean anything to us
    dRock = np.delete(dRock, [-1])
    dHburg = np.delete(dHburg, [-1])

    Rock_weekly_new = []

    # itterate through the list adding up each consecutive 7-day period of days to make a list of weekly new case totals
    i = 0
    while i < (len(Rock_cases) - 6):
        Rock_weekly_new.append(
            int(dRock[i]) + int(dRock[i + 1]) + int(dRock[i + 2]) + int(dRock[i + 3]) + int(dRock[i + 4]) + int(
                dRock[i + 5]) + int(dRock[i + 6]))
        i = i + 1
    Rock_worst_week = Rock.iloc[[argmax(Rock_weekly_new)], [0]].to_numpy()
    print(str(Rock_worst_week[0]))

    Hburg_weekly_new = []

    #why answers different???????
    '''
    i=0
    while i<(len(Hburg_cases)-6):
        Hburg_weekly_new.append(int(Hburg_cases[i+6])-int(Hburg_cases[i]))
        i=i+1
        '''
    i = 0
    while i < (len(Hburg_cases) - 6):
        Hburg_weekly_new.append(
            int(dHburg[i]) + int(dHburg[i + 1]) + int(dHburg[i + 2]) + int(dHburg[i + 3]) + int(dHburg[i + 4]) + int(
                dHburg[i + 5]) + int(dHburg[i + 6]))
        i = i + 1

    Hburg_worst_week = Hburg.iloc[[argmax(Hburg_weekly_new)], [0]].to_numpy()
    print(str(Hburg_worst_week[0]))
    return

if __name__ == "__main__":
    #import data using pandas
    df = pd.read_csv('us-counties.csv')
    # harisonburg fips is 51660
    # rockingham county fips is 51165
    # grab our counties using fips numbers (this is why they are so great)
    Rock = df[df['fips'] == 51165]
    Hburg = df[df['fips'] == 51660]

    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question()


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question()

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question()


