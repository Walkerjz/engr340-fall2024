import sys

from numpy.ma.core import argmax


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]
    Hburg_data=[]
    Rock_data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)
#Create two new lists of all the harrisonburg and rockingham data while we are at it.
        if entry[1] == 'Harrisonburg city':
            Hburg_data.append(entry)
        if (entry[1] == 'Rockingham') & (entry[2] == 'Virginia'):
            Rock_data.append(entry)


    return data, Rock_data, Hburg_data

def first_question(data, Rock_data, Hburg_data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    #Note that the parsing code was modified to return the rockingham and harisonburg data
    print( "The first positive in Rockingham County was: "+ str(Rock_data[0][0]))
    print("The first positive in Harrisonburg City was: " + str(Hburg_data[0][0]))

    return

def second_question(data, Rock_data, Hburg_data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    #define lists to hold the daily changes in covid cases
    Rock_data_new = [0]
    Hburg_data_new = [0]
    i = 0
    while i<(len(Rock_data)-1):
        Rock_data_new.append(int(Rock_data[i+1][3]) - int(Rock_data[i][3]))
        i=i+1
    j = 0
    while j<(len(Hburg_data)-1):
        Hburg_data_new.append(int(Hburg_data[j+1][3]) - int(Hburg_data[j][3]))
        j=j+1

    Hburg_worst_day = Hburg_data[argmax(Hburg_data_new)][0]
    Rock_worst_day = Rock_data[argmax(Rock_data_new)][0]
    look = Hburg_data_new
    print("The greatest number of new daily cases recorded in Rockingham County was on: " + str(Rock_worst_day))
    print("The greatest number of new daily cases recorded in Harrisonburg was on: " + str(Hburg_worst_day))
    #print(Hburg_data_new)
    return Rock_data_new, Hburg_data_new

def third_question(data, Rock_data_new, Hburg_data_new):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    Rock_weekly_new = []
    i=0
    while i<(len(Rock_data_new)-6):
        #add the weekly new cases
        Rock_weekly_new.append(int(Rock_data_new[i]) + int(Rock_data_new[i+1]) + int(Rock_data_new[i+2]) + int(Rock_data_new[i+3]) + int(Rock_data_new[i+4]) + int(Rock_data_new[i+5]) + int(Rock_data_new[i+6]))
        i=i+1
    Rock_worst_week = Rock_data[argmax(Rock_weekly_new)][0]
    print("The week with the most new covid cases in Rockingham county started on: " + str(Rock_worst_week))

    Hburg_weekly_new = []
    j=0
    while j<(len(Hburg_data_new)-6):
        #add the weekly new cases
        Hburg_weekly_new.append(int(Hburg_data_new[j]) + int(Hburg_data_new[j+1]) + int(Hburg_data_new[j+2]) + int(Hburg_data_new[j+3]) + int(Hburg_data_new[j+4]) + int(Hburg_data_new[j+5]) + int(Hburg_data_new[j+6]))
        j=j+1
    Hburg_worst_week = Hburg_data[argmax(Hburg_weekly_new)][0]
    print("The week with the most new covid cases in Harrisonburg City started on: " + str(Hburg_worst_week))
    return

if __name__ == "__main__":
    data, Rock_data, Hburg_data = parse_nyt_data('us-counties.csv')

    target = 5
    '''for (date, county, state, cases, deaths) in data:
        print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')
'''

    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data, Rock_data, Hburg_data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    Rock_data_new, Hburg_data_new = second_question(data, Rock_data, Hburg_data)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(data, Rock_data_new, Hburg_data_new)


