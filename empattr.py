import pandas as pd
import random as rand
import matplotlib.pyplot as plt

#choose a number of empolyees and attrition rate
emps = 1000
attr_prob = .03141592653

#create a list of employees and assign groups arbitrarily
emplist = ['Emp ' + str(i) for i in range(1,emps+1)]

#'flip coin' for each employee
losslist = rand.choices([1,0], weights=[attr_prob, 1-attr_prob], k=emps)

#finalize example database
df = pd.DataFrame({'Emplid':emplist, 'Loss':losslist})

#apply monte carlo simulation ('flip coin' for each employee in next time frame)
y_i = []
y_ii = []
y_iii = []
y_iv = []

#plot histograms one by one
for i in range(5):
    y_i.append(sum(rand.choices([1,0], weights=[attr_prob, 1-attr_prob], k=emps)))
plt.hist(y_i, bins=128)
plt.show()

for i in range(10):
    y_ii.append(sum(rand.choices([1,0], weights=[attr_prob, 1-attr_prob], k=emps)))
plt.hist(y_ii, bins=128)
plt.show()

for i in range(500):
    y_iii.append(sum(rand.choices([1,0], weights=[attr_prob, 1-attr_prob], k=emps)))
plt.hist(y_iii, bins=128)
plt.show()

for i in range(5000):
    y_iv.append(sum(rand.choices([1,0], weights=[attr_prob, 1-attr_prob], k=emps)))
plt.hist(y_iv, bins=128)
plt.show()
