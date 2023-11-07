import pandas as pd
import random as rand
import numpy as np
import matplotlib.pyplot as plt


#create a list of employees and assign groups arbitrarily
emplist = ['Emp ' + str(i) for i in range(1,10001)]
grouplist = rand.choices(['A', 'B', 'C', 'D', 'E'], weights = [.2, .15, .2, .25, .2], k=5000)

#choose a probability for the attrition rate
attr_prob = .03141592653

#'flip coin' for each employee
losslist = rand.choices([1,0], weights=[attr_prob, 1-attr_prob], k=len(emplist))

#finalize example employee database
df = pd.DataFrame({'Emplid':emplist, 'Group':grouplist, 'Loss':losslist})

#calculate attrition rates
groups = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0}

for group in groups:
    groups[group] = sum(np.where(df['Group']==group, df['Loss'],0)) / sum(np.where(df['Group']==group,1,0))

#apply monte carlo simulation ('flip coin' for each employee in next time frame)
y_total = []
y_A = []
y_B = []
y_C = []
y_D = []
y_E = []

for i in range(1,10001):
    y_total.append(sum(rand.choices([1,0], weights=[attr_prob, 1-attr_prob], k=len(df['Emplid']))))
    y_A.append(sum(rand.choices([1,0], weights=[attr_A, 1-attr_A], k=len(df['Emplid']))))
    y_B.append(sum(rand.choices([1,0], weights=[attr_A, 1-attr_A], k=len(df['Emplid']))))
    y_C.append(sum(rand.choices([1,0], weights=[attr_A, 1-attr_A], k=len(df['Emplid']))))
    y_D.append(sum(rand.choices([1,0], weights=[attr_A, 1-attr_A], k=len(df['Emplid']))))
    y_E.append(sum(rand.choices([1,0], weights=[attr_A, 1-attr_A], k=len(df['Emplid']))))

#plot histograms one by one
plt.hist(y_total)
plt.show()

plt.hist(y_A)
plt.show()

plt.hist(y_B)
plt.show()

plt.hist(y_C)
plt.show()

plt.hist(y_D)
plt.show()

plt.hist(y_E)
plt.show()
