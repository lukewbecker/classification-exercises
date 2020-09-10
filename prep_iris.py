# Prep iris database script for ingesting, cleaning and preparing the iris database for exploration.

def prep_iris(x): 
    x.rename(columns = {'species_name': 'species'}, inplace=True)
    x = x.drop(columns = ['species_id', 'measurement_id'])
    dummy_df = pd.get_dummies(x['species'], dummy_na=False)
    x = pd.concat([x, dummy_df], axis=1)
    return x
