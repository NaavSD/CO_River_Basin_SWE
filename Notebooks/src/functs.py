############################################################
# Custom function list for Water Storage Management Project#
# -------------------by Brian Reynolds---------------------#
############################################################


# function for performing a adfuller test and returning a readable result
def dicky_fuller_test(data, alpha):
    
    # import dependant library
    from statsmodels.tsa.stattools import adfuller
    
    is_stationary = adfuller(data)[1] < alpha
    if is_stationary == True:
        print(f'The data is stationary with a fuller score of {round(adfuller(data)[1],3)}')
    else:
        print(f'The data is not stationary with a fuller score of {round(adfuller(data)[1],3)}')
    return


# Function interpolates and backfills for time series data
def fix_na(df, interpolation_method='linear', fill_method='backfill'):
    
    # interpolate and backfill
    df = df.interpolate(method='linear').fillna(value=None, method='backfill', axis=None, limit=None, downcast=None).dropna(axis=1, how='all')
    return df


# Define a function to remove XLS file artifacts from dataframes.
def del_unnamed(df):
    cols = df.columns.tolist()
    to_remove = []
    
    for i in cols:
        if i.startswith('Unnamed'):
            to_remove.append(i)
    return df.drop(columns=to_remove)

# Function reformats water withdrawal data into timeseries with datetime index
def format_water_data(df, column):
    df.index = pd.to_datetime(df['YEAR'], format='%Y', infer_datetime_format=True)
    return df.groupby(df.index).aggregate({column : 'sum'})