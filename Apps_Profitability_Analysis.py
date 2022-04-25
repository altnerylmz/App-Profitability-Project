#!/usr/bin/env python
# coding: utf-8

# # Profitable App Profiles for the App Store and Google Play Markets
# 

# **Our aim in this project is to find mobile app profiles that are profitable for the App Store and Google Play markets.**

# ## Opening and Exploring the Data
# 

# Collecting data for over 4 million apps requires a significant amount of time and money, so we'll try to analyze a sample of the data instead. To avoid spending resources on collecting new data ourselves, we should first try to see if we can find any relevant existing data at no cost. Luckily, here are two data sets that seem suitable for our goals:

#  - A dataset containing data about approximately 10,000 Android apps from Google Play; the data was collected in August 2018. You can download the data set directly from this [link](https://dq-content.s3.amazonaws.com/350/googleplaystore.csv).
#  - A dataset containing data about approximately 7,000 iOS apps from the App Store; the data was collected in July 2017. You can download the data set directly from this [link](https://dq-content.s3.amazonaws.com/350/AppleStore.csv).

# Let's start by opening the two data sets and then continue with exploring the data.
# 
# 

# In[16]:


from csv import reader

### for Google Play Dataset ###

opened_file = open('/Users/altan/Downloads/googleplaystore.csv',encoding="utf8")
read_file = reader(opened_file)
android = list(read_file)
android_header = android[0]
android = android[1:]

### for Apple Dataset ### 
opened_file = open('/Users/altan/Downloads/AppleStore.csv', encoding ="utf8")
read_file= reader(opened_file)
ios = list(read_file)
ios_header= ios[0]
ios = ios[1:]


# To make it easier to explore the two data sets, we'll first write a function named explore_data() that we can use repeatedly to explore rows in a more readable way. We'll also add an option for our function to show the number of rows and columns for any data set.

# In[14]:


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line between rows
        
    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))

print(android_header)
print('\n')
explore_data(android, 0, 3, True)


# 
# We see that the Google Play data set has 10841 apps and 13 columns. At a quick glance, the columns that might be useful for the purpose of our analysis are `App`, `Category`, 'Reviews', 'Installs', 'Type', 'Price', and 'Genres'.

# Now let's take a look at IOS apps.

# In[17]:


print(ios_header)
print('n\'')
explore_data(ios, 0 , 3, True)


# We have 7197 iOS apps in this data set, and the columns that se
# em interesting are: 'track_name', 'currency', 'price', 'rating_count_tot', 'rating_count_ver', and 'prime_genre'

# ### Deleting wrong/missing data

# In the previous step, we opened the two data sets and explored the data. Before beginning our analysis, we need to make sure the data we analyze is accurate, or the results of our analysis will be wrong. This means that we need to do the following:
# 
# - Detect inaccurate data, and correct or remove it.
# - Detect duplicate data, and remove the duplicates.

# In this [link](https://www.kaggle.com/datasets/lava18/google-play-store-apps/discussion/66015) a missing row is mentioned. Let's print this row and compare it against the header and another row that is correct.

# In[20]:


print(android[10472])  # incorrect row
print('\n')
print(android_header)  # header
print('\n')
print(android[1])      # correct row


# In[ ]:




