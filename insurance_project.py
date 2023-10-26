#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 13:07:20 2023

@author: ssloniu
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('/Users/ssloniu/Documents/Projekty/python-portfolio-project-starter-files/insurance.csv')

#print(df.head())
#print(df.columns)

# I split database for smokers and non-smokers, I think it's better to do analysis separetly

smokers = df.loc[df['smoker']=='yes']
smokers_avg_charges = round(smokers['charges'].mean(), 2)
count_smokers = smokers['age'].count()
print("Patiens which smoke cigarettes pay on average " + str(smokers_avg_charges) + "$ for insurance, sample: " + str(count_smokers))
non_smokers = df.loc[df['smoker']=='no']
non_smokers_avg_charges = round(non_smokers['charges'].mean(), 2)
count_non_smokers = non_smokers['age'].count()
print(f"Patriens which doesn't smoke pay on average {non_smokers_avg_charges}$ for insurance, sample {count_non_smokers}\n")
print("Clearly smokers pay way more for insurance than non-smokers\n")

# Now I've realized that some functions might be helpful :)

def avg_charge(dataframe):
    counter = dataframe['age'].count()
    charge = round(dataframe['charges'].mean(), 2)
    charge_med = round(dataframe['charges'].median(), 2)
    print(f" pay on average (mean) {charge}$ (median: {charge_med}$ for insurance, sample: {counter}\n")
    
def list_avg(list_of_dataframes):
    list_charges = []
    for dataframe in list_of_dataframes:
        list_charges.append(round(dataframe['charges'].mean(), 2))
    return list_charges

def list_avg_med(list_of_dataframes):
    list_charges_median = []
    for dataframe in list_of_dataframes:
        list_charges_median.append(round(dataframe['charges'].median(), 2))
    return list_charges_median

def sex_ratio(dataframe):
    men = dataframe.loc[dataframe['sex']=='male']
    women = dataframe.loc[dataframe['sex']=='female']
    total = dataframe['sex'].count()
    men_ratio = round((men['sex'].count()/total)*100, 2)
    women_ratio = round((women['sex'].count()/total)*100, 2)
    print(f"In sample there is {men_ratio}% of men and {women_ratio}% of women.\n")
    
def smokers_ratio(dataframe):
    smokers = dataframe.loc[df['smoker']=='yes']
    non_smokers = dataframe.loc[df['smoker']=='no']
    total = dataframe['sex'].count()
    smokers_ratio = round((smokers['sex'].count()/total)*100, 2)
    non_smokers_ratio = round((non_smokers['sex'].count()/total)*100, 2)
    print(f"In that region smokers are {smokers_ratio}% of population, and non-smokers are {non_smokers_ratio}%.\n")
# To see if region has influence on charges  I've split data to all regions

sw = df.loc[df['region']=='southwest']
se = df.loc[df['region']=='southeast']
nw = df.loc[df['region']=='northwest']
ne = df.loc[df['region']=='northeast']

print("People in Southwest region")
avg_charge(sw)
sex_ratio(sw)
smokers_ratio(sw)
print("People in Southeast region")
avg_charge(se)
sex_ratio(se)
smokers_ratio(se)
print("People in Northwest region")
avg_charge(nw)
sex_ratio(nw)
smokers_ratio(nw)
print("People in Northeast region")
avg_charge(ne)
sex_ratio(ne)
smokers_ratio(ne)

sw_smoker = smokers.loc[smokers['region']=='southwest']
print("Smoker from southwest region")
avg_charge(sw_smoker)
sex_ratio(sw_smoker)
se_smoker = smokers.loc[smokers['region']=='southeast']
print("Smoker from southeast region")
avg_charge(se_smoker)
nw_smoker = smokers.loc[smokers['region']=='northwest']
print("Smoker from northwest region")
avg_charge(nw_smoker)
ne_smoker = smokers.loc[smokers['region']=='northeast']
print("Smoker from northeast region")
avg_charge(ne_smoker)

sw_non_smoker = non_smokers.loc[non_smokers['region']=='southwest']
print("Non smoker from southwest region")
avg_charge(sw_non_smoker)
se_non_smoker = non_smokers.loc[non_smokers['region']=='southeast']
print("Non smoker from southeast region")
avg_charge(se_non_smoker)
nw_non_smoker = non_smokers.loc[non_smokers['region']=='northwest']
print("Non smoker from northwest region")
avg_charge(nw_non_smoker)
ne_non_smoker = non_smokers.loc[non_smokers['region']=='northeast']
print("Non smoker from northeast region")
avg_charge(ne_non_smoker)

x_bar_regions = ['Southwest', 'Southeast', 'Northwest', 'Northeast']
y_smokers = list_avg([sw_smoker, se_smoker, nw_smoker, ne_smoker])
y_non_smokers = list_avg([sw_non_smoker, se_non_smoker, nw_non_smoker, ne_non_smoker])
y_smokers_med = list_avg_med([sw_smoker, se_smoker, nw_smoker, ne_smoker])
y_non_smokers_med = list_avg_med([sw_non_smoker, se_non_smoker, nw_non_smoker, ne_non_smoker])

plt.bar(x_bar_regions, y_smokers)
plt.bar(x_bar_regions, y_non_smokers)
plt.title("Mean charge split by regions")
plt.legend(['Smokers','Non-smokers'], loc=8)
plt.show()

plt.bar(x_bar_regions, y_smokers_med)
plt.bar(x_bar_regions, y_non_smokers_med)
plt.title("Median charge split by regions")
plt.legend(['Smokers','Non-smokers'], loc=8)
plt.show()

# Next I'll check difference between men and women

males = df.loc[df['sex']=='male']
print("Men ")
avg_charge(males)
females = df.loc[df['sex']=='female']
print("Women")
avg_charge(females)
men_smokers = smokers.loc[smokers['sex']=='male']
print("Men which smoke ")
avg_charge(men_smokers)
women_smokers = smokers.loc[smokers['sex']=='female']
print("Women which smoke ")
avg_charge(women_smokers)
men_non_smokers = non_smokers.loc[non_smokers['sex']=='male']
print("Men which doesn't smoke ")
avg_charge(men_non_smokers)
women_non_smokers = non_smokers.loc[non_smokers['sex']=='female']
print("Women which doesn't smoke")
avg_charge(women_non_smokers)

x_sex = ['Smoking men', 'Smoking women', 'Non-smokin men', 'Non-smoking women']
y_sex = list_avg([men_smokers, women_smokers, men_non_smokers, women_non_smokers])
y_sex_med = list_avg_med([men_smokers, women_smokers, men_non_smokers, women_non_smokers])

fig = plt.figure(figsize=[10,6])
plt.bar(x_sex, y_sex)
plt.title("Mean charge for smoking men and women")
plt.show()

figu = plt.figure(figsize=[10,6])
plt.bar(x_sex, y_sex_med)
plt.title("Median charge for smoking men and women")
plt.show()

# examining how having children affects insurance cover
#print(df['children'].unique())
childrens = [0, 1, 2, 3, 4, 5]

for x in childrens:
    c = df.loc[df['children']==x]
    count = c['age'].count()
    m = round(c['charges'].mean(),2)
    print(f"Patients which have {x} children pay on average {m}$ for insurance, sample: {count}")
print("Having more children might have influence on how much patient pay for insurance.")
    
# Right, now I'm gonna focus on BMI

conditions = [
    df['bmi'] < 18.5,
    (df['bmi'] >= 18.5) & (df['bmi'] < 25),
    (df['bmi'] >= 25) & (df['bmi'] < 30),
    df['bmi'] >= 30
]
choices = ['underweight', 'optimum', 'overweight', 'obesity']
df['weight'] = pd.Series(np.select(conditions, choices))

underweight = df.loc[df['weight']=='underweight']
optimum = df.loc[df['weight']=='optimum']
overweight = df.loc[df['weight']=='overweight']
obese = df.loc[df['weight']=='obesity']

fig1 = plt.figure(figsize=[10,6])
y_weight = list_avg([underweight, optimum, overweight, obese])
plt.bar(choices, y_weight)
plt.title("Mean charges for each BMI group")
plt.show()

fig2 = plt.figure(figsize=[10,6])
y_weight_med = list_avg_med([underweight, optimum, overweight, obese])
plt.bar(choices, y_weight_med)
plt.title("Median charges for each BMI group")
plt.show()

print("Clearly fatter you get, you pay more and that's fair.")
    
# Now it's time for scatterplots

fig3 = plt.figure(figsize=[12,7])
ax1 = plt.subplot(1,2,1)
plt.scatter(smokers['bmi'],smokers['charges'])
plt.xlabel("BMI")
ax1.set_title("Smokers charges")
ax2 = plt.subplot(1,2,2)
plt.scatter(non_smokers['bmi'], non_smokers['charges'])
plt.xlabel("BMI")
ax2.set_title("Non-smokers charges")
plt.show()

fig4 = plt.figure(figsize=[10,6])
colors = {'underweight': 'red', 'optimum': 'green', 'overweight': 'blue', 'obesity': 'purple'}
plt.scatter(df['age'], df['charges'], c=df['weight'].map(colors))
plt.title("Charges vs Age")
for weight, color in colors.items():
    plt.scatter([], [], c=color, label=weight)
plt.legend()
plt.xlabel("Age")
plt.ylabel("$")
plt.show()
print("Looks like there's a pattern, older patients must pay more.")
