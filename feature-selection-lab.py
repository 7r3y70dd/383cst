# -*- coding: utf-8 -*-
"""
Feature selection lab

Instructions:
    - edit this code by answering the 4 problems below
    - work with your team
    - I've provided all the imports you will need

@author: Dr. Bruns
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

sns.set()
sns.set_context('talk')   # 'talk' for slightly larger
rcParams['figure.figsize'] = 7,5

def plot_selected(selected, accuracies, predictors):
    """ Create a bar plot of variables and their accuracy """
    
    pd.Series(accuracies, index=predictors[selected]).plot.barh()
    plt.xlabel('Cross-validation accuracy')
    plt.title('Result of forward feature selection')

#
# Read the data
#

# note the index_col=0 option
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv', index_col=0)
df['Private'] = (df['Private'] == 'Yes').astype(int)

df.info()

target = 'Private'
predictors = df.columns[df.columns != target]
X = df[predictors].values
y = df[target].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

print(X.shape)  # 17 predictors
print(y.shape)

"""
Problem 1.

Modify the following code so that it will find the single best predictor.
The returned selected and accuracies lists should contain only a single value each.

Your code should have a single loop over the remaining list.

Use cross_val_score() to compute the accuracy when using the selected features.

Use a KNN classifier as your classifier.

Experiment with your code after you write it.
"""

def forward_selection_classif(clf, X, y, num_folds=5):
        
    # remaining is a list of features yet to be selected
    # Each feature is identified by a column of NumPy array X
    remaining = list(range(X.shape[1]))
    # selected is a list of column numbers have already been selected
    # selected[0] is the first column selected
    selected = []
    # accuracies[0] is the accuracy if you use the feature selected[0]
    # accuracies[1] is the accuracy if you use features selected[0], selected[1]
    # etc.
    accuracies = []

    while len(remaining)!= 0:
        

    return np.array(selected), accuracies


# run your code
selected, accuracies = forward_selection_classif(KNeighborsClassifier(), X_train, y_train)


"""
Problem 2.

Modify your code from the previous problem so that it does forward
feature selection.

Refer to the pseudocode given in class.

You will have an outer loop that runs as long as 'remaining' is not empty.
"""

# run your code
selected, accuracies = forward_selection_classif(KNeighborsClassifier(), X_train, y_train)
plot_selected(selected, accuracies, predictors)

"""
Problem 3.

Modify your code from the previous problem so that it take a 'threshold'
parameter.

The code should only add a feature to selected if that feature has caused
an improvement in accuracy that is greater than the value of 'threshold'.
"""
    
# test your code
selected, accuracies = forward_selection_classif(KNeighborsClassifier(), X_train, y_train, threshold=0.003)
plot_selected(selected, accuracies, predictors)


"""
Problem 4.

Modify your code from the previous problem so that it take a 'num_folds'
parameter, which specifies the number of folds to be used in cross validation.
"""

# test your code
selected, accuracies = forward_selection_classif(KNeighborsClassifier(), X_train, y_train, num_folds=20)
plot_selected(selected, accuracies, predictors)





