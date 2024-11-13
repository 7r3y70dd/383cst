# -*- coding: utf-8 -*-
"""
Categorical encoding lab

@author: Glenn
"""

import numpy as np
import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns

sns.set()
sns.set_context('talk')   
# default plot size
rcParams['figure.figsize'] = 9,7


#
# read the data
#
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/heart-categ.csv')

#
# problem 1
#

print(df.head(20))

# What are the types (o+rdinal, nominal, discrete quantitative,
# continuous quantitative) of each variable in the data set?

# YOUR ANSWER HERE (as a comment)

for column in df.columns:
    unique_values = df[column].unique()
    print(f"Column '{column}':")
    print(unique_values)
    print("\n")

#
# problem 2
#



# Modify the data set so that all variable are numeric.  Make sure
# the encoding of categorical variables is performed correctly.

# YOUR CODE HERE

#
# problem 3
#

# If you still have time, encode the categorical variables in the census data set
# df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/1994-census-summary.csv')










