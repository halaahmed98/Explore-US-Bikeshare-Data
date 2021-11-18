import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:

        city = input("What is  city do you want?  (Chicago - New York City - Washington)" '\n')
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('please enter the correct city name!')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("What is month do you want? (January - February - March - April - May - June ) or All ?" '\n')
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:

            print('please enter the correct month name!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(
            "What is day do you want? (Monday, Tuesday, .....Sunday) or All ?" '\n')
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print('please enter the correct day name!')

    print('-' * 40)

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    print('The most Common month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most Common Day of Week:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    common_hour = df['hour'].mode()[0]

    print('The most common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print('The most Commonly Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most Commonly End Station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    comb_start_end = (df['Start Station'] + " and " + df['End Station']).mode()[0]
    print('The most frequent combination of start station and end station trip:', comb_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print('The Total travel time:', total_travel_time, 'sec')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The  average of traveling time:', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The counts of user types', user_type)

    # TO DO: Display counts of gender (washington doesn't have this data)
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print('The count of gender:', gender)
    else:
        print('this data is not available in Washington')

        # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('The earliest year of birth:', earliest)
        print('The most recent year of birth:', recent)
        print('The most common year of birth:', common_year)
    else:
        print('this data is not available in Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?" "\n")
    start_loc = 0

    while True:

        if view_data.lower() == 'yes':
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            view_data = input("Do you wish to continue?: Yes or No" '\n').lower()
        elif view_data.lower() == "no":
            print('Done!')
            break
        else:
            print('Please enter yes or no')
            return display_data(df)





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break




if __name__ == "__main__":
    main()
