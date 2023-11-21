import pandas as pd
import random as rand
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

#choose an attrition rate
attr_prob = .03141592653
emps = 1000

#define a time series
fyq = ['FY22Q1', 'FY22Q2', 'FY22Q3', 'FY22Q4', 'FY23Q1', 'FY23Q2', 'FY23Q3', 'FY23Q4']

#I want to simulate a seasonal change
#np.linspace defines a number of points to return, in a list, from any function in a defined range
x = 1+np.sin(np.linspace(-(np.pi/4), (np.pi+np.pi/4), num=4))/2
#plt.plot(x)

#weights for each quarter over two years in a list
fsin = [x[0], x[1], x[2], x[3], x[0], x[1], x[2], x[3]]

#initialize df
df = pd.DataFrame({'Emplid':[None], 'Group':[None], 'Loss':[None], 'FYQ':[None]})

i = 0
while i < len(fyq):
    #create a list of employees and assign groups randomly, then adjust attrition probability with seasonal function
    emplist = ['Emp ' + str(n) for n in range(1,emps+1)]
    grouplist = rand.choices(['A', 'B', 'C', 'D'], weights = [.2, .35, .2, .25], k=emps)
    adj_ap = attr_prob*fsin[i]
    
    #flip the coin of attrition for each employee, 1 for attr 0 for retain
    #assume 30 new employees every quarter, we won't deal with employee retention analysis in this project
    losslist = rand.choices([1,0], weights=[adj_ap, 1-adj_ap], k=emps)
    df = pd.concat([df, pd.DataFrame({'Emplid':emplist, 'Group':grouplist, 'Loss':losslist, 'FYQ':fyq[i]})]).reset_index(drop=True)
    emps = emps-sum(losslist)+10
    i+=1

df = df.dropna()
#x = sorted(set(df['FYQ']))
#height=[len(df[df['FYQ']==i]) for i in list(set(df['FYQ']))]
#plt.bar(x, height)

#weighted average
#8 points (one for each quarter) aligned to a logarithmic curve
wavg = np.exp(np.linspace(0, np.e, num=8))/np.exp(np.e)
#plt.plot(wavg)

#calculate the attrition probability for each quarter and store in a list
probs = [sum(df.loc[df['FYQ']==i, ['Loss']].sum(axis=1))/len(df[df['FYQ']==i]) for i in fyq]

#apply the weights to each quarter's attrition probability and sum to get the weighted mean attrition. 
wattr = [i * j for i, j in zip(wavg, probs)]



#a second way to calculate a weighted mean for this dataset might be to balance the weights of each quarter a bit more.
wavg = list(np.exp(np.linspace(0, np.e, num=8))/np.exp(np.e))
#all we have to do is reverse the list and use the function y = f(2c-x)
wavg.reverse()
wavg = [(2*.5) - i for i in wavg]
#plt.plot(wavg)



empnq = len(df[df['FYQ']==fyq[-1]]) - sum(df.loc[df['FYQ']==fyq[-1], ['Loss']].sum(axis=1))
wmean_attr = sum(wattr)/len(wattr)

#5 iterations
y_total = []
for i in range(5):
    y_total.append(sum(rand.choices([1,0], weights=[wmean_attr, 1-wmean_attr], k=empnq)))
plt.hist(y_total, bins = 128)
plt.show()

#50 iterations
y_total = []
for i in range(50):
    y_total.append(sum(rand.choices([1,0], weights=[wmean_attr, 1-wmean_attr], k=empnq)))
plt.hist(y_total, bins = 128)
plt.show()

#5000 iterations
y_total = []
for i in range(500):
    y_total.append((sum(rand.choices([1,0], weights=[wmean_attr, 1-wmean_attr], k=empnq))/empnq)*100)
plt.hist(y_total, bins = 128)
plt.show()

confidence=0.95
a = 1.0 * np.array(y_total)
n = len(a)
h = st.sem(a) * st.t.ppf((1 + confidence) / 2., n-1)
print(np.mean(a), np.mean(a)-h, np.mean(a)+h)

#this produces a really small confidence interval. what happens if we simulate with all probabilities?
#5 iterations
y_total = []
for i in range(2000):
    y_total.append(sum(rand.choices([1,0], weights=[probs[0], 1-probs[0]], k=empnq)))
    y_total.append(sum(rand.choices([1,0], weights=[probs[1], 1-probs[1]], k=empnq)))
    y_total.append(sum(rand.choices([1,0], weights=[probs[2], 1-probs[2]], k=empnq)))
    y_total.append(sum(rand.choices([1,0], weights=[probs[3], 1-probs[3]], k=empnq)))
    y_total.append(sum(rand.choices([1,0], weights=[probs[4], 1-probs[4]], k=empnq)))
    y_total.append(sum(rand.choices([1,0], weights=[probs[5], 1-probs[5]], k=empnq)))
    y_total.append(sum(rand.choices([1,0], weights=[probs[6], 1-probs[6]], k=empnq)))
    y_total.append(sum(rand.choices([1,0], weights=[probs[7], 1-probs[7]], k=empnq)))

plt.hist(y_total, bins = 128)
plt.show()

#let's also remove everything outside 3 standard deviations (99.7%) of the data
y_total.mean() + 3 * y_total.std()

[rand.choice([i,None]) for i in y_total]



#50 iterations
y_total = []
for i in range(50):
    y_total.append(sum(rand.choices([1,0], weights=[wmean_attr, 1-wmean_attr], k=empnq)))
plt.hist(y_total, bins = 32)
plt.show()


y_mean = sum(y_total)/len(y_total)
c_interval = st.norm.interval(alpha=.90, loc=y_mean, scale=st.sem(y_total))

for i in range(5):
    y_total.append(sum(rand.choices([1,0], weights=[wmattr, 1-wmattr], k=)))

for i in range(1,10001):
    y_total.append(sum(rand.choices([1,0], weights=[wmattr, 1-wmattr], k=)))


