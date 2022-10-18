#!/usr/bin/env python
# coding: utf-8

# In[76]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px


# In[77]:


df = pd.read_csv('/Users/Yousif/jupyter_projects/coupons.csv')


# In[78]:


df.head()


# In[79]:


df.shape


# In[80]:


#2.Investigate the dataset for missing or problematic data.

df.isnull().sum()


# In[81]:


print('Percent of missing "car" records is %.2f%%' %((df['car'].isnull().sum()/df.shape[0])*100))


# In[82]:


#3.Decide what to do about your missing data -- drop, replace, other...

#drop car column

df.drop(columns=['car'])


# In[83]:


print('Percent of missing "Bar" records is %.2f%%' %((df['Bar'].isnull().sum()/df.shape[0])*100))


# In[84]:


#3.Decide what to do about your missing data -- drop, replace, other...
#replace missing values with mean

df['Bar'].fillna(df.mean(), inplace=True)


# In[85]:


print('Percent of missing "CoffeeHouse" records is %.2f%%' %((df['CoffeeHouse'].isnull().sum()/df.shape[0])*100))


# In[86]:


df['CoffeeHouse'].fillna(df.mean(), inplace=True)


# In[87]:


print('Percent of missing "CarryAway" records is %.2f%%' %((df['CarryAway'].isnull().sum()/df.shape[0])*100))


# In[88]:


df['CarryAway'].fillna(df.mean(), inplace=True)


# In[89]:


print('Percent of missing "RestaurantLessThan20" records is %.2f%%' %((df['RestaurantLessThan20'].isnull().sum()/df.shape[0])*100))


# In[90]:


df['RestaurantLessThan20'].fillna(df.mean(), inplace=True)


# In[91]:


print('Percent of missing "Restaurant20To50" records is %.2f%%' %((df['Restaurant20To50'].isnull().sum()/df.shape[0])*100))


# In[92]:


df['Restaurant20To50'].fillna(df.mean(), inplace=True)


# In[93]:


#5.Use a bar plot to visualize the coupon column.

plt= px.bar(df, x="coupon")
plt.show()


# In[94]:


#6.Use a histogram to visualize the temperature column.

hist = px.histogram(df, x= 'temperature')
hist


# In[95]:


s = df.coupon


# In[96]:


counts = s.value_counts()
counts


# In[97]:


percent = s.value_counts(normalize=True)
percent


# In[98]:


percent100 = s.value_counts(normalize=True).mul(100).round(1).astype(str)+'%'
percent100


# In[99]:


pd.DataFrame({'counts': counts, 'per': percent, 'per100': percent100})


# In[ ]:





# In[100]:


#4.What proportion of the total observations chose to accept the coupon?

df.groupby(['coupon'])['Y'].sum()


# In[101]:


df.groupby(['coupon'])['Y'].agg(['mean','sum'])


# In[166]:


df2=df[df["coupon"]=='Bar']
print(df2)


# In[207]:


#Investigating the Bar Coupons
#1.Create a new DataFrame that contains just the bar coupons
df = pd.read_csv('/Users/Yousif/jupyter_projects/coupons.csv')


# In[208]:


newdf=df[(df.coupon== "Bar")]
newdf.head()
b=len(newdf.index)
print(b)


# In[209]:


values=["Bar"]
print(df[df["coupon"].isin(values)])
print(df.loc[df['coupon'].isin(values)])


# In[210]:


#2.What proportion of bar coupons were accepted?

newdf=df[(df.coupon== "Bar")&(df.Y==1)]
newdf.head()
c=len(newdf.index)
print(b)
print(c)
m=c/b*100
print(m)


# In[212]:


#3.Compare the acceptance rate between those who went to a bar 3 or fewer times a month to those who went more.
newdfc = df[(df.coupon == "Bar") & (df.Y == 1) & (df.Bar =="1~3")]
newdfc.head()
bar3orless=len(newdfc. index)
print(bar3orless)
newdfd = df[(df.coupon == "Bar") & (df.Y == 1) & (df.Bar =="4~8")|(df.coupon == "Bar") & (df.Y == 1) & (df.Bar =="gt8")]
newdfd.head()
barmorethan3=len(newdfd.index)
print(barmorethan3)
acc3orless=bar3orless/b*100
acc3ormore=barmorethan3/b*100
print(acc3orless)
print(acc3ormore)


# In[213]:


#4.Compare the acceptance rate between drivers who go to a bar more than once a month and are over the age of 25 to the all others. Is there a difference?
newdfe = df[(df.coupon == "Bar") & (df.Y == 1) & (df.age > "25") &(df.age !="below21") 
            & ((df.Bar =="1~3")|(df.Bar =="gt8")|(df.Bar =="4~8"))]
newdfe.head()
morethan1over25=len(newdfe.index)
print(morethan1over25)

newdff = df[(df.coupon == "Bar") & (df.Y == 1) & ((df.age < "25")|(df.age =="below21")) 
            & ((df.Bar =="1~3")|(df.Bar =="gt8")|(df.Bar =="4~8"))]
newdff.head()
otherthanover25=len(newdff.index)
print(otherthanover25)

acc25andmorethan1=morethan1over25/b*100
print(acc25andmorethan1)

acclessthan25=otherthanover25/b*100
print(acclessthan25)


# In[217]:


#5. Use the same process to compare the acceptance rate between drivers who go to bars more than once a month 
#and had passengers that were not a kid and had occupations other than farming, fishing, or forestry.

newdfg = df[(df.coupon == "Bar") & (df.Y == 1) & (df.passanger != "Kid(s)") &(df.occupation !="Farming Fishing & Forestry") 
            & ((df.Bar =="1~3")|(df.Bar =="gt8")|(df.Bar =="4~8"))]
newdfg.head()
morethan1werenokid=len(newdfg.index)
print(morethan1werenokid)

newdfh = df[(df.coupon == "Bar") & (df.Y == 1) & ((df.passanger == "Kid(s)")|(df.occupation =="Farming Fishing & Forestry")) 
            & ((df.Bar =="1~3")|(df.Bar =="gt8")|(df.Bar =="4~8"))]
newdfh.head()
otherthan1werekid=len(newdfh.index)
print(otherthan1werekid)

acc2morethan1werenokid=morethan1werenokid/b*100
print(acc2morethan1werenokid)

accwerenokidoccufff=otherthan1werekid/b*100
print(accwerenokidoccufff)


# In[ ]:


#6.Compare the acceptance rates between those drivers who:
#go to bars more than once a month, had passengers that were not a kid, and were not widowed OR
#go to bars more than once a month and are under the age of 30 OR
#go to cheap restaurants more than 4 times a month and income is less than 50K.

newdf1 = df[(df.coupon == "Bar") & (df.Y == 1) & (df.passanger != "Kid(s)") &(df.maritalStatus !="widowed") 
            & ((df.Bar =="1~3")|(df.Bar =="gt8")|(df.Bar =="4~8"))]
newdf1.head()
notkidnotwid=len(newdf1.index)
print(notkidnotwid)
newdf2 = df[(df.coupon == "Bar") & (df.Y == 1) & ((df.age < 30)
            & ((df.Bar =="1~3")|(df.Bar =="gt8")|(df.Bar =="4~8"))]                                  
newdf2.head()
under30=len(newdf2.index)
print(under30)                                                  
                                                  
                                                  
newdf3= df[(df.coupon == "Bar") & (df.Y == 1) & (df.RestaurantLessThan20 =="4~8") &(df.income =="$37500 - $49999") 
            & ((df.Bar =="1~3")|(df.Bar =="gt8")|(df.Bar =="4~8"))]
newdf3.head()
morethan4lessthan50k=len(newdf3.index)
print(morethan4lessthan50k)                                                  
                                                                  

(newdf1)|(newdf2)|(newdf3)


# In[ ]:


#7.Based on these observations, what do you hypothesize about drivers who accepted the bar coupons?

Drivers who accepted the bar coupons are around 40% of drivers. 
Drivers who went to the bar more than 3 times a week are more likely to accept the coupons than those who go less than 3 times. 

