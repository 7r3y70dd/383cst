# -*- coding: utf-8 -*-
"""

Coping with missing data in 2016 US Presidential Campaign contribution data.

Each problem is defined using special comment lines:
    
#@ problem     Lines that start like this give the problem ID.

##             Lines that start like this give the problem description.

#@ assume      Lines that start like this list the variables you can refer
               to in your code.
               
#@ assign      Lines like are used when you modify a variable or assign to it,
               and gives the variable name.

If a problem doesn't have a #@ assign line, your answer should be
an expression.

Provide your answer on the first blank line after the problem lines.

Use no loops.  Almost every problem can easily be done in one line of code.
Multiple lines are acceptable, as long as the last line is correctly either
an expression or an assignment.
    
In all problems, "NA" means NA values as decided by function
numpy.isna(), and not any other values that may also seem to indicate
missing data, such as the string "N/A".
    
The data used here is a sample of a larger data set.  I will test your
code on a different sample of the full data set.

@author: Glenn Bruns

"""

import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 500)

# Read the data.  This data is a subset of the 2016 presidential
# campaign contribution data for the state of California.  Spend
# a little time looking at the data -- it is interesting.

df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/campaign-ca-2016-sample.csv")

# get a summary of the data, and get a rough
# idea of where NA values lie

df.info()

#@ problem 1
## What is the total number of NAs in df?
## (compute a number)
#@ assume df
total = df.isna().sum().sum()
print(total)
print('')


#@ problem 2
## What fraction of all values in df are NA values?
## (compute a number between 0 and 1)
#@ assume df
print(total/df.size)
print('')

#@ problem 3
## What fraction of the values in each column are NA?
## Show only non-zero values, and sort the result by
## decreasing value.
## (compute a Pandas Series)
#@ assume df
total_per_column = df.isna().sum()
totals = total_per_column / df.shape[0]
totals_sorted = totals.sort_values(ascending=False)
print(totals_sorted[totals_sorted > 0])
print('')
# for i in totals_sorted.index:
#     if totals_sorted[i] > 0:
#         print(f"{i}: {totals_sorted[i]:.5f}")

#@ problem 4
## Which columns contain more than 40% NA values?
## (compute a NumPy array of the column names, sorted alphabetically)
#@ assume df
over_40 = totals[totals > 0.4].index
sorted = np.sort(over_40)
print(sorted)
print('')

#@ problem 5
## Compute a series that show the cumulative fraction of
## NA data contained in columns, ordered by most-NA column first.
##
## Example: Suppose we have a dataframe with columns a, b, c, and d.
## Suppose a contains 3 NAs, b contains no NAs, c contains 5 NAs,
## and d contains 2 NAs.  Then the result should be a series with
## values 0.5, 0.8, 1.0, 1.0 and index 'c', 'a', 'd', 'b'.
## This says: column c contains 50% of all the NAs, columns c and a
## together contain 80% of all the NAs, columns c, a, and d together
## contain 100% of all the NAs, etc.
##
## Hint: there is a "cumsum" function for series in Pandas.
## (compute a NumPy series)
#@ assume df
total_n_sorted = total_per_column.sort_values(ascending=False)
cdf = total_n_sorted.cumsum() / total_n_sorted.sum()
print(cdf)
print('')

#@ problem 6
## What fraction of the rows in df contain at least 2 NA values?
## (compute a single number between 0 and 1)
#@ assume df
tot_na = df.isna().sum(axis=1)
two_or_more = (tot_na >= 2).sum()
print(two_or_more / df.shape[0])
print('')
#@ problem 7
## There are other values in the dataset, besides NA, that
## represent missing data.  How to find them?
## For example, how many empty strings are in the data?  Do not 
## search in the numeric columns: 'contb_receipt_amt' and 'file_num'.
## Hint: to get only the 'object' type columns, consider
## pandas.DataFrame.select_dtypes.
## (compute a single number)
#@ assume df

#@ problem 8
## Would you expect contbr_employer to contain data that
## represent missing values?  Create a series with counts
## of the values that occur in the contbr_employer column the
## most.  The series should contain the 15 most-occurring
## values, listed in decreasing order.  Do you think any
## of the values represent missing values?
## (compute a Series)
#@ assume df
val_counts = df['contbr_employer'].value_counts().head(15)
print('')
print(val_counts)
print('')
#@ problem 9
## Repeat the previous problem, but this time create a data
## frame showing the 15 most-occurring values for columns
## contbr_employer, contbr_occupation, and contbr_city.
## You will not show the counts.  Hint: create a function
## that takes a series s and returns a series containing
## as data the 15 most-occurring values in s, in descending
## order.  The index of the returned series should range from
## 0 to 14.  Then use pandas.DataFrame.apply() with this function.
## (compute a DataFrame)
#@ assume df
def top_15_values(s, k=None):
    if k is None:
        final = pd.Series(s.value_counts().head(15).index, index=range(15))

        return final
    else:
        final = pd.DataFrame({s.name : s.value_counts().head(15).index, k.name: k.value_counts().head(15).index})

        final.index = range(15)

        return final

val_counts_1_5 = df['contbr_employer']
print(top_15_values(val_counts_1_5))
print('')
val_counts_2 = df['contbr_occupation']
val_counts_3 = df['contbr_city']
print('')
print(top_15_values(val_counts_2, val_counts_3))
print('')

#@ problem 10
## Look carefully at the output of the last problem.  (Do this
## before continuing.)
## Did you notice that the contbr_employer and contbr_occupation
## columns contain values 'INFORMATION REQUESTED' and
## 'INFORMATION REQUESTED PER BEST EFFORTS'?  These values -- but
## not values like 'NOT EMPLOYED' -- seem to indicate missing data.
## Modify df so that *all* values 'INFORMATION REQUESTED' and
## 'INFORMATION REQUESTED PER BEST EFFORTS' are placed with nan.
## Use DataFrame.replace(), with option 'inplace=True'.
## (write a pd.DataFrame.replace() statement)
#@ assume df
#@ assign df
df.replace(['INFORMATION REQUESTED', 'INFORMATION REQUESTED PER BEST EFFORTS'], np.nan, inplace=True)

#@ problem 11
## Did you notice that 'NOT EMPLOYED' and 'NONE'
## appear frequently in the contbr_employer column?   Do you
## think that these values represent missing data?  Replace
## all occurrences of 'NONE' in column 'contbr_employer'
## with 'NOT EMPLOYED'.
## Use Series.replace(), with option 'inplace=True'.
## (write a pd.Series.replace() statement)
#@ assume df
#@ assign df
df.replace({'contbr_employer': {'NONE', 'NOT EMPLOYED'}}, inplace=True)

#@ problem 12
## Lots of people are self-employed.  Compute a NumPy array of
## all the values in 'contbr_occupation' that contain the string 'SELF'.
## You may want to use pd.Series.str.contains().  Check out the 'na' option.
## (compute a NumPy array)
#@ assume df
self_employed = df['contbr_occupation'][df['contbr_occupation'].str.contains('SELF', na=False)].unique()

print(self_employed)
print('')

#@ problem 13
## Update df to remove all columns containing at least 50% NA values.
## Use DataFrame.dropna with the 'thresh' option
## (write a pd.DataFrame.dropna() statement)
#@ assume df
#@ assign df
df.dropna(axis=1, thresh=df.shape[0] * 0.5, inplace=True)

#@ problem 14
## Column election_tp has a very small number of NA values.
## Drop all *rows* of df for which election_tp is NA.
## (write a pd.DataFrame.dropna() statement)
#@ assume df
#@ assign df
df.dropna(subset=['election_tp'], inplace=True)

#@ problem 15
## What about bad zip values?  
## How many contbr_zip values contain characters that are not digits?
## Hint: the regular expression that matches something that is not
## a digit is '[^0-9]'  Consider using Series.str.contains() for this.
## (compute a number)
#@ assume df
bad_zip = df['contbr_zip'].str.contains('[^0-9]').sum()
print(bad_zip)
print('')

#@ problem 16
## What fraction of contb_receipt_amt values are less than 0?
## (compute a number between 0 and 1)
#@ assume df
frac = (df['contb_receipt_amt'] < 0).mean()
print(frac)
print('')









