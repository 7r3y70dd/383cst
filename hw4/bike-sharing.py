# -*- coding: utf-8 -*-
"""
Aggregation in Lyft San Francisco bike ride-sharing data, April, 2019.

Data source:
    https://www.kaggle.com/jolasa/bay-area-bike-sharing-trips

Some of the questions we'll look into:
    - what are the ages of the riders?
    - how long are typical rides (in terms of time)?
    - does riding behavior depend on age?
    - does riding behavior depend on gender?
    - does riding behavior depend on whether rider is a subscriber or a casual
      rider?
    - which start/stop locations are most common?

Each problem is defined using special comment lines:
    
#@ problem     Lines that start like this give the problem ID.

##             Lines that start like this give the problem description.

#@ assume      Lines that start like this list the variables you can refer
               to in your code.

#@ assign      Lines like are used when you modify a variable or assign to it,
               and gives the variable name.

If a problem doesn't have a #@ assign line, then your answer 
should be an expression.

Provide your answer on the first blank line after the problem lines.

Use no loops.  Almost every problem can easily be done in one line of code.
    
@author: Glenn Bruns

"""

import numpy as np
import pandas as pd

# =============================================================================
# Read the data
# =============================================================================

df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/lyft-2019-04.csv")

# =============================================================================
# Data preprocessing
# =============================================================================

df.info()

# drop NAs
df.isna().mean().sort_values()
df.dropna(inplace=True)

# create new variable showing member age
df['member_age'] = (2019 - df['member_birth_year']).astype(int)
df = df[df['member_age'] < 100]

# great new variable showing member age group
age_groups = [18, 25, 35, 50, 100]
group_names = ['18-25', '25-35', '35-50', '>50']
df['age_group'] = pd.cut(df['member_age'], age_groups, labels=group_names).astype(object)

# drop the month column
df.drop('month', axis=1, inplace=True)


#@ problem 1
## Add new integer variable 'trip_min' (trip minutes) to df.
## Compute this using existing variable 'trip_duration_sec'.
## Obviously, to convert seconds to minutes, you need to
## divide by 60.
## Hint: use astype() to convert from float to int.
## The "assign df" below means the df dataframe, or part of it,
## will be assigned to.  Your answer will be a statement.
#@ assume df
#@ assign df
df['trip_min'] = (df['trip_duration_sec'] / 60).astype(int)


#@ problem 2
## Make start_station_id variable into int type.
#@ assume df
#@ assign df
df['start_station_id'] = df['start_station_id'].astype(int)



#@ problem 3
## Make end_station_id variable into int type.
#@ assume df
#@ assign df
df['end_station_id'] = df['end_station_id'].astype(int)



#@ problem 4
## Create a new column of df called 'route' that contains the
## start_station_id and the end_station_id, with '->' between
## them.  For example, if the value of start_station_id on a
## row is 1, and the end_station_id is 2, then the value of
## route for that row should be the string '1->2'.
## Hint: convert the station IDs to string using astype(), then
## concatenate them.  
#@ assume df
#@ assign df
df['route'] = df['start_station_id'].astype(str) + '->' + df['end_station_id'].astype(str)



#@ problem 5
## create a new column of df called 'BART' that is True if either the start
## or end station name contains 'BART'
#@ assume df
#@ assign df
df['BART'] = df['start_station_name'].str.contains('BART') | df['end_station_name'].str.contains('BART')



# =============================================================================
# Data exploration
# =============================================================================

# Please note: in this section of the assignment there's a problem for which
# you may want to use unique(), which is a method for Pandas series.  It gives
# all the unique values found in the series.  For example,
# pd.Series(['a','b','c','b']).unique() returns NumPy array(['a','b','c']).
#
# Of course, the unique values of a series could also be computed using
# valued_counts(), but that is a less direct approach.

#@ problem 6
## how many rows in dataframe df?
#@ assume df
df.shape[0]



#@ problem 7
## what are the column names of df?
#@ assume df
df.columns



#@ problem 8
## what is the length of the longest trip, in hours?
## Use trip_min, not trip_duration_sec
#@ assume df
df['trip_min'].max() / 60


#@ problem 9
## what is the median trip length, in minutes?
## Use trip_min, not trip_duration_sec
#@ assume df
df['trip_min'].median()


#@ problem 10
## What is the age of the oldest rider?
#@ assume df
df['member_age'].max()


#@ problem 11
## What is the age of the youngest rider?
#@ assume df
df['member_age'].min()


#@ problem 12
## Compute the first 10 rows of df, using only columns trip_min, member_age, 
## member_gender, and user_type (in that order).
#@ assume df
df[['trip_min', 'member_age', 'member_gender', 'user_type']].head(10)


#@ problem 13
## What are the unique values in column user_type?
## Your answer should be a NumPy array.
#@ assume df
df['user_type'].unique()


#@ problem 14
## What fraction of the user_type values are 'Subscriber'?
## Remember, a fractional value is between 0 and 1.
#@ assume df
(df['user_type'] == 'Subscriber').mean()


#@ problem 15
## Are the bikes mostly used for commuting or for pleasure?
## Compute the fraction of rides that last more than 1 hour.
#@ assume df
(df['trip_min'] > 60).mean()


#@ problem 16
## What are the station names?
## Compute the unique station names from column 'start_station_name',
## and assign the value to variable 'station_names'.  The value of
## station_names must be a Pandas Series!
#@ assume df
#@ assign station_names
station_names = df['start_station_name'].unique()


#@ problem 17
## What fraction of the station names contain the word 'Station'?
## Use variable station_names to compute this.
#@ assume station_names
(station_names.str.contains('Station')).mean()


#@ problem 18
## What fraction of the rides end at a station contining the word 'Station'?
## Use df to compute this.
#@ assume df
(df['end_station_name'].str.contains('Station')).mean()


#@ problem 19
## What fraction of rides either start or stop (or both) at a station with
## BART in the name?
## Use the BART variable of df to compute this.
## Hint: you may want to use a Pandas vectorized string operation as
## part of your solution.
#@ assume df
(df['BART']).mean()

# =============================================================================
# Aggregation with value_counts()
# =============================================================================

#@ problem 20
## How many rides are associated with each user type?
#@ assume df
df['user_type'].value_counts()


#@ problem 21
## What fraction of the rides are associated with each gender? 
## Hint: Read the pandas documentation for value_counts(), especially
## the documenation on option 'normalize'.
#@ assume df
df['member_gender'].value_counts(normalize=True)


#@ problem 22
## What fraction of the rides are associated with each age group?
## (list largest fraction first)
#@ assume df
df['age_group'].value_counts(normalize=True).sort_values(ascending=False)


#@ problem 23
## What fraction of the rides are associated with each age group?
## (list in order of age ranges, youngest first)
## (Hint: use fancy indexing, .loc, and the group_names variable)
#@ assume df,group_names
df['age_group'].value_counts(normalize=True).reindex(group_names)


#@ problem 24
## How many rides are associated with each end station name?
## (list station that occurs that most first, and show only
## the top 20 stations)
#@ assume df
df['end_station_name'].value_counts().head(20)


#@ problem 25
## How many rides are associated with each start station name?
## (list station that occurs that most first, and show only
## the top 20 stations)
#@ assume df
df['start_station_name'].value_counts().head(20)


#@ problem 26
## How many rides are associated with each combination of
## start and end stations?
## Compute the number of rides associated with the 20 most
## common combinations of start and end stations.
## Use value_counts(), and use the 'start_station_name' and
## 'end_station_name' columns of df.  Do not use the 'route' column.
## (Hint: .value_counts() can be applied to Pandas data frames,
## not just Pandas series.)
#@ assume df
df.groupby(['start_station_name', 'end_station_name']).size().nlargest(20)


#@ problem 27
## Which are the most-used routes?
## Compute the number of rides associated with the 20 most-used routes,
## then assign the route values to new Series variable top_routes.
## Your answer must be the index of a Pandas Series (a Pandas Index).
## (Hint: use the 'route' column.)
#@ assume df
#@ assign top_routes
top_routes = df['route'].value_counts().nlargest(20).index

# =============================================================================
# Aggregation with groupby()
# =============================================================================


#@ problem 28
## Do different age groups ride for different amounts of time?
## What is the average trip time (in minutes) for each age group?
## Your answer should be a Pandas Series.
## Hint: use groupby().
#@ assume df
df.groupby('age_group')['trip_min'].mean()


#@ problem 29
## The median trip length may be better then the average trip length.
## (Average trip length is heavily influenced by long rides.)
## What is the median trip time (in minutes) for each age group?
#@ assume df
df.groupby('age_group')['trip_min'].median()


#@ problem 30
## Do subscribers tend to be older or younger than casual riders?
## Compute the median member age for each user type.
#@ assume df
df.groupby('user_type')['member_age'].median()


#@ problem 31
## Do men tend to ride for a longer period of time then women, or
## vice versa?
## Compute the median trip length (in minutes) for each value of
## member_gender.  Your answer should be a Pandas Series.
## Use trip_min, not trip_duration_sec.
#@ assume df
df.groupby('member_gender')['trip_min'].median()


#@ problem 32
## Looking at riders in terms of gender and age group, are there
## differences in trip length?
## Compute the median trip length (in minutes) for each combination 
## of member_gender and age_group.
## Use trip_min, not trip_duration_sec.
#@ assume df
df.groupby(['member_gender', 'age_group'])['trip_min'].median()


#@ problem 33
## Compute the mean *and* median trip length (in minutes) for each age group.
## For each age group, the mean should be listed before the median.
## Use trip_min, not trip_duration_sec.
#@ assume df
df.groupby('age_group')['trip_min'].agg(['mean', 'median'])


#@ problem 34
## Do commuters tend to be younger or older often than casual riders?
## To try to answer this question, compute the median age of riders for
## 1) rides that end at a station with 'Station' in its name, and
## 2) rides that don't end at a station with 'Station' in its name. 
## Use groupby().
## Hint: groups can be defined by boolean array, not just by column names.
## For this problem, the boolean array will be true when the end station name
## contains 'Station'.
## See lecture notes on aggregation for more details.
#@ assume df
df.groupby(df['end_station_name'].str.contains('Station'))['member_age'].median()


#@ problem 35
## Maybe commuters tend to be subscribers, rather than casual users.
## Compute, for the case where the end station name contains "BART",
## and for the case where the end station name does not contain "BART",
## the fraction of trips in which user_type is Subscriber.
## Your answer should be a Pandas Series.
## Use group_by().
## Hint 1: as we saw in lecture, groups can be defined by boolean masks,
## not just by column names.
## Hint 2: don't forget that aggregation with groupby can be done by any
## function, not just 'mean', 'max', etc.  It can be a function you define.
#@ assume df
df.groupby(df['end_station_name'].str.contains('BART'))['user_type'].apply(lambda x: (x == 'Subscriber').mean())


#@ problem 36
## Do trips on common routes tend to have about the same trip time?
## Answer this question with two lines of code.  
## Line 1: create a data frame (you could call it df_top_routes) that contains
## all the rows of df in which the value of 'route' is in 'top_routes'.
## Line 2: compute the median trip_min for each route in the new data frame.
## The median trip values should be given in descending order.
## Hint: to see if a route is in top_routes, consider Pandas method .isin().
## For example, try this:  pd.Series(['a','b','c']).isin(['a','b'])
#@ assume df,top_routes
df_top_routes = df[df['route'].isin(top_routes)]
df_top_routes.groupby('route')['trip_min'].median().sort_values(ascending=False)


# =============================================================================
# Aggregation with two categorical variables
# =============================================================================

# Aggregation is most commonly used with one categorical variable
# and one quantitative variable.  For example, get the average
# ride distance (quantitative variable) for each age group
# (categorical variable).
# When we have two categorical variables, it is common to use
# the Pandas crosstab() function, which we'll cover in class soon.


#@ problem 37
## What fraction of the rides are in each combination of user_type
## and age_group?
## Hint: use value_counts() on two columns of df.
## Hint: we want fractional values, not counts.
#@ assume df
df.groupby(['user_type', 'age_group']).size() / len(df)

