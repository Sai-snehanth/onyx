#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[7]:


data = pd.read_excel(r"C:\Users\saisn\Downloads\Onyx Data -DataDNA Dataset Challenge - Email Analysis Dataset - July 2024\Onyx Data -DataDNA Dataset Challenge - Email Analysis Dataset - July 2024.xlsx")


# In[9]:


data.head()


# In[10]:


data.info()


# In[11]:


data.describe()


# In[12]:


data.tail()


# In[13]:


data.isnull()


# In[17]:


data.describe().T


# In[18]:


data


# In[20]:


data.head(5)


# In[23]:


plt.figure(figsize=(10, 6))
plt.plot(data['Email id'],data['Date'])
plt.show()


# In[22]:


plt.bar(data['Within work hours'],data['Email id'])


# In[29]:


import seaborn as sns


# In[27]:


# Violin Plot: Emails Sent Within Work Hours
plt.figure(figsize=(10, 6))
sns.violinplot(x='Within work hours', y='Email id', data=df)
plt.title('Emails Sent Within Work Hours vs. Outside Work Hours')
plt.xlabel('Within Work Hours')
plt.ylabel('Email ID')
plt.show()


# In[34]:


# Mapping sentiment to numerical values for plotting
sentiment_map = {'neutral': 0, 'positive': 1}
df['Sentiment_value'] = df['Sentiment'].map(sentiment_map)
plt.figure(figsize=(8, 8))
# Convert 'Within work hours' to numerical values for plotting
work_hours_map = {'yes': 1, 'no': 0}
df['Within_work_hours_value'] = df['Within work hours'].map(work_hours_map)

sns.jointplot(x='Sentiment_value', y='Within_work_hours_value', data=df, kind='scatter', height=8)
plt.suptitle('Sentiment vs. Within Work Hours', y=1.02)
plt.xlabel('Sentiment (0: Neutral, 1: Positive)')
plt.ylabel('Within Work Hours (0: No, 1: Yes)')
plt.show()


# In[33]:


# Joint Plot: Date vs. Device
# Convert 'Device' to numerical values for plotting
device_map = {'desktop': 0, 'mobile': 1}
df['Device_value'] = df['Device'].map(device_map)
plt.figure(figsize=(8, 8))
sns.jointplot(x='Date', y='Device_value', data=df, kind='scatter', height=8)
plt.suptitle('Date vs. Device Usage', y=1.02)
plt.xlabel('Date')
plt.ylabel('Device (0: Desktop, 1: Mobile)')
plt.show()


# In[32]:


df = pd.DataFrame(data)

# Count the occurrences of each sentiment
sentiment_counts = df['Sentiment'].value_counts()

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Email Sentiments')
plt.show()


# In[37]:


df = pd.DataFrame(data)

# Filter to only include numerical columns
numerical_df = df.select_dtypes(include=['number'])

# Generate descriptive statistics for numerical data
desc = numerical_df.describe()

# Plot the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(desc, annot=True, linewidths=0.5, cmap='coolwarm')
plt.title('Summary Statistics Heatmap')
plt.show()


# In[ ]:




