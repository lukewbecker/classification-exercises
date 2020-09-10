# Creating the function for ingesting, cleaning and preparing the titanic database for exploration.

def prep_titanic(titanic_data):
    # Importing the libraries I'll need for this function.
    from sklearn.impute import SimpleImputer
    import warnings
    warnings.filterwarnings("ignore")
    
    # Handling the missing data
    titanic_data = titanic_data[~titanic_data.embark_town.isnull()]
    # Removing the 'deck' column    
    titanic_data = titanic_data.drop(columns = 'deck')
    # Creating dummy variables
    dummy_titanic_df = pd.get_dummies(titanic_data['embarked'], dummy_na = False)
    titanic_data = pd.concat([titanic_data, dummy_titanic_df], axis=1)
    
    # Using the impute method to fill the missing values in the age column
    imputer = SimpleImputer(strategy = 'most_frequent')
    imputer.fit(titanic_data[['age']])
    titanic_data[['age']] = imputer.transform(titanic_data[['age']])
    return titanic_data