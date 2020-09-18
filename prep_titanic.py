# Importing libraries in use.
import pandas as pd
import numpy as np
from scipy import stats
    
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

from sklearn.model_selection import train_test_split


# Creating the function for ingesting, cleaning and preparing the titanic database for exploration.

def prep_titanic_data(titanic_data):
          
    # Importing the libraries I'll need for this function.
    # import pandas as pd
    # import numpy as np
    # from scipy import stats
    
    # from sklearn.impute import SimpleImputer
    # from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

    # from sklearn.model_selection import train_test_split
    
    # Initialization
    titanic_data = titanic_data


    # Handling the missing data
    titanic_data = titanic_data[~titanic_data.embark_town.isnull()]
    # Removing the 'deck' column    
    titanic_data = titanic_data.drop(columns = 'deck')
    # Drop passenger_id column:
    titanic_data = titanic_data.drop(columns = 'passenger_id')
    # Creating dummy variables
    dummy_titanic_df = pd.get_dummies(titanic_data['embarked'], dummy_na = False)
    titanic_data = pd.concat([titanic_data, dummy_titanic_df], axis=1)
    # Creating dummy column for the gender column:
    dummy_titanic_df = pd.get_dummies(titanic_data['sex'], dummy_na = False, drop_first = True)
    titanic_data = pd.concat([titanic_data, dummy_titanic_df], axis=1)
    titanic_data.rename(columns = {'male': 'sex_cat'}, inplace = True)
    
    # Using the impute method to fill the missing values in the age column
    imputer = SimpleImputer(strategy = 'most_frequent')
    imputer.fit(titanic_data[['age']])
    titanic_data[['age']] = imputer.transform(titanic_data[['age']])
    
    # Return the prepped dataframe:
    return titanic_data


def prep_titanic_data_split(titanic_data):
          
    # Importing the libraries I'll need for this function.
    # import pandas as pd
    # import numpy as np
    # from scipy import stats
    
    # from sklearn.impute import SimpleImputer
    # from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

    # from sklearn.model_selection import train_test_split
    
    # Initialization
    titanic_data = titanic_data


    # Handling the missing data
    titanic_data = titanic_data[~titanic_data.embark_town.isnull()]
    # Removing the 'deck' column    
    titanic_data = titanic_data.drop(columns = 'deck')
    # Drop passenger_id column:
    titanic_data = titanic_data.drop(columns = 'passenger_id')
    # Creating dummy variables
    dummy_titanic_df = pd.get_dummies(titanic_data['embarked'], dummy_na = False)
    titanic_data = pd.concat([titanic_data, dummy_titanic_df], axis=1)
    # Creating dummy column for the gender column:
    dummy_titanic_df = pd.get_dummies(titanic_data['sex'], dummy_na = False, drop_first = True)
    titanic_data = pd.concat([titanic_data, dummy_titanic_df], axis=1)
    titanic_data.rename(columns = {'male': 'sex_cat'}, inplace = True)
    
    # Using the impute method to fill the missing values in the age column
    imputer = SimpleImputer(strategy = 'most_frequent')
    imputer.fit(titanic_data[['age']])
    titanic_data[['age']] = imputer.transform(titanic_data[['age']])

    # Splitting the data:
    train, validate, test = train_valid_test(titanic_data)
    
    # Return the prepped dataframe:
    return train, validate, test


# Split function for titanic data:

def train_valid_test(df):
    df = train_validate, test = train_test_split(df, test_size = .2, random_state = 123, stratify = df.survived)
    train, validate = train_test_split(train_validate, test_size = .3, random_state = 123, stratify = train_validate.survived)
    return train, validate, test