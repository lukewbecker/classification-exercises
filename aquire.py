# Creating the aquire.py file

# Make a new python module, acquire.py to hold the following data aquisition functions:
# get_titanic_data
# get_iris_data

# Importing libraries:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Importing the os library specifically for reading the csv once I've created the file in my working directory.
import os

# Make a function named get_titanic_data that returns the titanic data from the codeup data science database as a pandas data frame. Obtain your data from the Codeup Data Science Database.

# Setting up the user credentials:

from env import host, user, password

def get_db(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# titanic_db query
sql_query = 'SELECT * FROM passengers'


def get_titanic_data():
    return pd.read_sql('SELECT * FROM passengers', get_db('titanic_db'))

# Showing the df: 
# print(get_titanic_data())

# Make a function named get_iris_data that returns the data from the iris_db on the codeup data science database as a pandas data frame. The returned data frame should include the actual name of the species in addition to the species_ids. Obtain your data from the Codeup Data Science Database.
def get_iris_data():
    return pd.read_sql('''SELECT measurement_id, sepal_length, sepal_width, petal_length, petal_width, m.species_id, species_name
FROM measurements AS m
JOIN species AS s on m.species_id = s.species_id;''', get_db('iris_db'))

# Once you've got your get_titanic_data and get_iris_data functions written, now it's time to add caching to them. To do this, edit the beginning of the function to check for a local filename like titanic.csv or iris.csv. If they exist, use the .csv file. If the file doesn't exist, then produce the SQL and pandas necessary to create a dataframe, then write the dataframe to a .csv file with the appropriate name.

def get_titanic_data_cache():
    filename = 'titanic.csv'
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        titanic_df = pd.read_sql('SELECT * FROM passengers', get_db('titanic_db'))
        titanic_df.to_csv(filename, index = False)
        # Ryan was using .to_file, but I was getting error when trying to use that function.
        return titanic_df

# print(get_titanic_data_cache())


# Defining the variable for my titanic data:
# df_titanic = get_titanic_data_cache()

# # Creating a seaborn chart:
# sns.relplot(data = df_titanic, x = 'age', y = 'fare', hue = 'class')
# plt.show()

# Doing the same for the iris_db:

def get_iris_data_cache():
    filename = 'iris.csv'
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        iris_df = get_iris_data()
        iris_df.to_csv(filename, index = False)
        # Ryan was using .to_file, but I was getting error when trying to use that function.
        return iris_df

# print(type(get_iris_data_cache()))

# print(get_iris_data_cache())

print('End of file.')