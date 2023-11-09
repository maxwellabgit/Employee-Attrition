# Employee Attrition Using Monte Carlo Simulations
## Our goals in this project are:
1. Understand how Monte Carlo Simulations work
2. Create an example Employee Database
3. Use Monte Carlo methodology to predict attrition

This is a basic implementation of Monte Carlo methodology to forecast employee attrition. Statistical models are a respectable choice given the problem set. The advantages to this model over an ML classifier is firstly that this is a logic-driven methodology which can be easily explained or justified. Secondly, this implementation is fairly efficient, producing usable visualizations in minutes. Lastly, this is a good method to use in tandem with Machine Learning solutions, either as a baseline or to affect model weights.

### Understanding Monte Carlo

A brief summary of the thought process behind Monte Carlo simulations from [britannica.com](https://www.britannica.com/science/Monte-Carlo-method):

> "American scientist Stanislaw Ulam wondered what was the probability of winning a game of solitaire and realized that simply playing a number of games and noting the percentage of winning games would be much simpler than trying to calculate all the possible combinations of cards. He then further realized that such an approach could be applied to problems such as the production and diffusion of neutrons in radioactive material, a problem in which at each step there were so many possibilities that a solution was impossible to calculate."
> "The likelihood of a particular solution can be found by dividing the number of times that solution was generated by the total number of trials. By using larger and larger numbers of trials, the likelihood of the solutions can be determined more and more accurately."

The number of factors that contribute to the probability of an employee resigning from a position (voluntarily or involuntarily) are so numerous that it is impossible to perfectly capture the impact of every variable. In a problem like this, a machine learning solution seems like a good fit given the ability to estimate weights for many variables at once to make a prediction. However, explaining the logic behind the model's results eventually boils down to "we should trust the model based on the rules we created". On the other hand, statistical models like Monte Carlo provide a model with a logical flow of operations. __The more easily understandable the solution is, the more likely a customer is to trust the product.__ Using a Monte Carlo Simulation here allows us to estimate the solution to a complex problem using simple statistical and probablistic methods, and sets a baseline for a potential machine learning solution.

### Create a Synthetic Employee Database

Let's install pandas and numpy (as always), random for Monte Carlo probabilities, and matplotlib for some visualization at the end.

    import pandas as pd
    import random as rand
    import numpy as np
    import matplotlib.pyplot as plt

We create a list of ten thousand employee IDs, "Emp 1" through "Emp 10001", and assign them random groups with varying sizes for a later use case.

    emplist = ['Emp ' + str(i) for i in range(1,10001)]
    grouplist = rand.choices(['A', 'B', 'C', 'D', 'E'], weights = [.2, .15, .2, .25, .2], k=5000)

Choose an overall attrition rate, in this case about 3%, and create a new field to our employee database called "Loss" (from losslist). Use a '1' to notate 'attrited' and '2' to notate 'retained'. __Our employee database is complete.__ 

    attr_prob = .03141592653
    losslist = rand.choices([1,0], weights=[attr_prob, 1-attr_prob], k=len(emplist))
    df = pd.DataFrame({'Emplid':emplist, 'Group':grouplist, 'Pay_Band':paybandlist, 'Loss':losslist})

[IMAGE OF DATABASE]

### Use Monte Carlo Methodology to Predict Attrition

Here is where the casino comes in. Monte Carlo works by calculating a normal distribution using known probabilities and quantities. By calculating the attrition rate this time period and applying it to the quantity of employees in the next period, we can calculate a distribution and associated confidence level.

Let's first calculate the attrition probability for each subgroup. Initialize a dictionary with groups and their attrition rates, then calculate the actual attrited / retained value in a 'for' loop. Although our overall attrition rate was about 3.14% this time period, each group is a different size, (and in the real world, has many other variables) affecting the actual attrition rate.

    groups = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0}
    for group in groups:
        groups[group] = sum(np.where(df['Group']==group, df['Loss'],0)) / sum(np.where(df['Group']==group,1,0))

We apply each group's attrition rate to every employee for every group. For example, if we had a 3% attrition rate last time period, then I will point to every employee we retained in this current time period and predict attrition with a coin flip weighted 97:3. After making a prediction for each employee, I aggregate the results to the total attrited vs retained (it should be close to 3%, but won't always) and visualize to obtain a __simulation__ of what would happen if our attrition rate was the same as last time frame.

> [!IMPORTANT]
> I can repeat the process as many times as I choose to increase the simulation's fidelity until we visualize attrition values in a normal distribution.

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

[IMAGE OF 5 ITERATIONS] [IMAGE OF 100 ITERATIONS] [IMAGE OF 5000 ITERATIONS]

## Summary

In our process, the number of employees is free to change quarter to quarter, year to year, etc. However, the ratio is derived from previous time frames. This is the logical basis for establishing a statistical prediction of the likely outcomes. A core factor of this model is how we utilize the historical dataset in relation to our applied probability in the Monte Carlo Simulation. In the real world, I might start with a weighted average to give more influence to the most recent time frames.

Monte Carlo is a useful approach for many data problems. Firstly for the purpose of building explainable systems, and secondly because it is a widely-used technique which can serve as a fine baseline. This model can be used to aid weights optimization, exploratory correlation analyses, and much more beyond the scope of this mini demonstration.
