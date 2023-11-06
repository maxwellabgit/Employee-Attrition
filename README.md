# Employee Attrition Using Monte Carlo Simulations
## Our goals in this project are:
 - Create a Synthetic Employee Database
 - Use Monte Carlo Methodology to Predict Attrition

This is a basic implementation of Monte Carlo methodology to forecast employee attrition. Statistical models are a respectable choice given the problem set. The advantages to this model over an ML classifier is firstly that this is a logic-driven methodology which can be easily explained or justified. Secondly, this implementation is fairly efficient, producing usable visualizations in minutes. Lastly, this is a good method to use in tandem with Machine Learning solutions, either as a baseline or to affect model weights.

### Create a Synthetic Employee Database

Let's install pandas and numpy (as always), random for Monte Carlo probabilities, and matplotlib for some visualization at the end.

    import pandas as pd
    import random as rand
    import numpy as np
    import matplotlib.pyplot as plt

We create a list of ten thousand employee IDs, "Emp 1" through "Emp 10001", and assign them random groups with varying sizes for a later use case.

    emplist = ['Emp ' + str(i) for i in range(1,10001)]
    grouplist = rand.choices(['A', 'B', 'C', 'D', 'E'], weights = [.2, .15, .2, .25, .2], k=5000)

Choose an overall attrition rate, in this case about 3%, and add a new field to our employee database. Use a '1' to notate 'attrited' and '2' to notate 'retained'. Then, create our finalized database.

    attr_prob = .03141592653
    losslist = rand.choices([1,0], weights=[attr_prob, 1-attr_prob], k=len(emplist))
    df = pd.DataFrame({'Emplid':emplist, 'Group':grouplist, 'Pay_Band':paybandlist, 'Loss':losslist})

### Use Monte Carlo Methodology to Predict Attrition

Here is where the casino comes in. Monte Carlo works by calculating a normal distribution using known probabilities and quantities. By calculating the attrition rate this time period and applying it to the quantity of employees in the next period, we can calculate a distribution and associated confidence level.

Let's first calculate the attrition probability for each subgroup. Initialize a dictionary with groups and their attrition rates, then calculate the actual attrited / retained value in a 'for' loop. Although our overall attrition rate was about 3.14% this time period, each group is a different size, (and in the real world, has many other variables) affecting the actual attrition rate.

    groups = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0}
    for group in groups:
        groups[group] = sum(np.where(df['Group']==group, df['Loss'],0)) / sum(np.where(df['Group']==group,1,0))

We apply each group's attrition rate to every employee for every group. For example, if we had a 3% attrition rate last time period, then I will point to every employee we retained in this current time period and predict attrition with a coin flip weighted 97:3. After predicting for each employee, I can repeat the process ten thousand more times and visualize the total predicted attrition values in a normal distribution.

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

Finally, plot histograms with matplotlib

    plt.hist(y_total)
    plt.show()

## Summary

In our process, the number of employees is free to change quarter to quarter, year to year, etc. However, the ratio is derived from previous time frames. This is the logical basis for establishing a statistical prediction of the likely outcomes. A core factor of this model is how we utilize the historical dataset in relation to our applied probability in the Monte Carlo Simulation. In the real world, I might start with a weighted average to give more influence to the most recent time frames.

Monte Carlo is a useful approach for many data problems. Firstly for the purpose of building explainable systems, and secondly because it is a widely-used technique which can serve as a fine baseline. This model can be used to aid weights optimization, exploratory correlation analyses, and much more beyond the scope of this mini demonstration.
