import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates as md


file = pd.read_csv('Motor Vehicle Collisions working.csv', dtype={8: str, 22: str})  # , nrows=10_000)
df = pd.DataFrame(file)
df_cleaned_time_precrash = df.drop(df.columns[[0, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                               13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24]], axis=1)
# print(df.isnull().sum())
print(df.info())
# print(df_cleaned.head())
print(df_cleaned_time_precrash.info())
# print(df_cleaned_time_precrash.to_string())
# df_cleaned_time_precrash['CRASH_TIME'] = pd.to_datetime()
# print(type(pd.to_datetime(df['CRASH_TIME'])))


# remove NaN rows based on the 'PRE_CRASH' column and re-index df_cleaned_time_precrash
df_cleaned_time_precrash.dropna(subset='PRE_CRASH', inplace=True)
df_cleaned_time_precrash.reset_index(drop=True, inplace=True)
df_cleaned_time_precrash['CRASH_TIME'] = pd.to_datetime(df_cleaned_time_precrash['CRASH_TIME'], format='%H:%M')
# print(df_cleaned_time_precrash['CRASH_TIME'].info())
# print(df_cleaned_time_precrash['CRASH_TIME'].to_string())
# print(df_cleaned_time_precrash.head())


# produces a scatter plot representing PRE_CRASH (x) type and CRASH_TIME (y)
def precrash_crashtime_scatter():
    plt.scatter(df_cleaned_time_precrash['PRE_CRASH'], df_cleaned_time_precrash['CRASH_TIME'])
    plt.xticks(rotation=45)
    plt.xlabel('Action Before Crash')
    plt.ylabel('Time of Day')
    plt.gca().yaxis.set_major_formatter(md.DateFormatter('%H:%M'))
    plt.gca().yaxis.set_major_locator(md.HourLocator(byhour=[0, 3, 6, 9, 12, 15, 18, 21, 24]))

    plt.show()


# produces a histogram of the frequency at which crashes occur by time ranges (per hour)
# creates new column, 'CRASH_HOUR' that extracts time from 'CRASH_DATE'
def time_frequency_hist():
    df_cleaned_time_precrash['CRASH_HOUR'] = df_cleaned_time_precrash['CRASH_TIME'].dt.time

    plt.hist(df_cleaned_time_precrash['CRASH_TIME'], edgecolor='black', linewidth=1.2)
    plt.title('Crash-Time Frequency')
    plt.xlabel('Time (hourly)')
    plt.ylabel('Occurrences')
    plt.gca().xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
    plt.gca().xaxis.set_major_locator(md.HourLocator(byhour=range(24), interval=1))
    plt.show()
# hourly 'buckets' on x-axis
# https://stackoverflow.com/questions/68902125/how-to-add-hourly-buckets-on-x-axis-labels-on-a-histogram

# print(df_cleaned_time_precrash[df_cleaned_time_precrash['PRE_CRASH'] == 'Parked'])


# produces histograms for the 'CRASH_TIME' based on the unique 'PRE_CRASH' conditions
# used to display frequency at which crash occurred per each 'PRE_CRASH' condition
def unique_precrash_hist() -> None:
    for pre_crash_type in df_cleaned_time_precrash['PRE_CRASH'].unique():
        # print(pre_crash_type)
        crash_type_col = df_cleaned_time_precrash.loc[df_cleaned_time_precrash['PRE_CRASH'] == pre_crash_type]
        plt.hist(crash_type_col['CRASH_TIME'], bins=int(24*60/30), edgecolor='black', rwidth=0.5)
        plt.title(pre_crash_type + ' Frequency')
        plt.xlabel('Hour')
        plt.ylabel('Occurrences')
        plt.gca().xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
        plt.gca().xaxis.set_major_locator(md.HourLocator(byhour=range(24), interval=1))  # x-axis in 1-hour intervals
        plt.show()

    return None


# produces histograms for the ___ based on ___ with time ranges (1 hour interval)
def f_hist():
    return None

# precrash_crashtime_scatter()
# time_frequency_hist()
# unique_precrash_hist()

