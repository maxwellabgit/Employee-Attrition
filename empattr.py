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
df = pd.DataFrame({'Emplid':emplist, 'Group':grouplist, 'Pay_Band':paybandlist, 'Loss':losslist})

#calculate attrition rate
attr_total = sum(df['Loss']) / len(df['Emplid'])

#calculate attrition rate for subgroup
attr_A = sum(np.where(df['Group']=='A',df['Loss'],0)) / sum(np.where(df['Group']=='A',1,0))


#apply monte carlo simulation ('flip coin' for each employee in next time frame). The number of employees
#is free to change, but the ratio is derived from previous time frames. The deciding factor in this forecasting model
#is how we utilize the historical dataset in relation to my attrition ratio. In the real world, I would start with
#a weighted average of previous time frames that weighs more recent time frames higher.
y_total = []
y_A = []

for i in range(1,10001):
    y_total.append(sum(rand.choices([1,0], weights=[attr_prob, 1-attr_prob], k=len(df['Emplid']))))
    y_A.append(sum(rand.choices([1,0], weights=[attr_A, 1-attr_A], k=len(df['Emplid']))))


plt.hist(y_total)
plt.show()

plt.hist(y_A)
plt.show()
