# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:38:41 2024

@author: Heng2020
"""
import pandas as pd
import dataframe_short as ds
from typing import Union, Dict, List

# def upsampling(X_df, y_df, verbose = 1):
    
#     import pandas as pd
#     import numpy as np
    
#     """
#     Perform manual upsampling on a dataset to balance class distribution.

#     This function upsamples the minority classes in a dataset to match the 
#     number of instances in the majority class. It operates by randomly 
#     duplicating instances of the minority classes.

#     Parameters:
#     X_df (pd.DataFrame): DataFrame containing the feature set.
#     y_df (pd.Series): Series containing the target variable with class labels.
#     verbose: 
#         0 print nothing
#         1 print out before & after upsampling
    

#     Returns:
#     list: Contains two elements:
#         - pd.DataFrame: The upsampled feature DataFrame.
#         - pd.Series: The upsampled target Series.

#     Note:
#     The function does not modify the input DataFrames directly. Instead, it 
#     returns new DataFrames with the upsampled data. The indices of the 
#     returned DataFrames are reset to maintain uniqueness.
#     """
    
    
#     # Determine the majority class and its count
#     majority_class = y_df.value_counts().idxmax()
#     majority_count = y_df.value_counts().max()
    
#     if verbose == 0:
#         pass
#     elif verbose == 1:
#         print("Before upsampling: ")
#         print()
#         print(y_df.value_counts())
#         print()
    
    
#     # Initialize the upsampled DataFrames
#     X_train_oversampled = X_df.copy()
#     y_train_oversampled = y_df.copy()

#     # Perform manual oversampling for minority classes
#     for label in y_df.unique():
#         if label != majority_class:
#             samples_to_add = majority_count - y_df.value_counts()[label]
#             indices = y_df[y_df == label].index
#             random_indices = np.random.choice(indices, samples_to_add, replace=True)
#             X_train_oversampled = pd.concat([X_train_oversampled, X_df.loc[random_indices]], axis=0)
#             y_train_oversampled = pd.concat([y_train_oversampled, y_df.loc[random_indices]])

#     # Reset index to avoid duplicate indices
#     X_train_oversampled.reset_index(drop=True, inplace=True)
#     y_train_oversampled.reset_index(drop=True, inplace=True)
    
#     if verbose == 0:
#         pass
#     elif verbose == 1:
#         print("After upsampling: ")
#         print()
#         print(y_train_oversampled.value_counts())
#         print()
    
#     return [X_train_oversampled, y_train_oversampled]


def upsampling(X_df: pd.DataFrame, y_df: pd.Series, strategy: Union[str, Dict[str, float]] = 'equal', random_state: int = 1, verbose: int = 1) -> List:
    # medium tested seem to work now
    # solo from ChatGPT
    import pandas as pd
    import numpy as np
    """
    Perform manual upsampling on a dataset to balance class distribution according to a specified strategy.

    Parameters:
    X_df (pd.DataFrame): DataFrame containing the feature set.
    y_df (pd.Series): Series containing the target variable with class labels.
    strategy (str or dict): If 'equal', all classes are upsampled to the same number as the majority class. If a dict, each class is upsampled to match a specified proportion.
    random_state (int): The seed used by the random number generator.
    verbose (int): 
        0 print nothing
        1 print before & after upsampling

    Returns:
    list: Contains two elements:
        - pd.DataFrame: The upsampled feature DataFrame.
        - pd.Series: The upsampled target Series.
    """
    np.random.seed(random_state)

    if verbose == 1:
        print("Before upsampling: ")
        print(y_df.value_counts(), "\n")
    
    # Determine the majority class and its count
    if strategy == 'equal':
        majority_count = y_df.value_counts().max()
        sample_proportions = {label: majority_count for label in y_df.unique()}
    elif isinstance(strategy, dict):
        total_proportion = sum(strategy.values())
        sample_proportions = {label: int((strategy.get(label, 0) / total_proportion) * len(y_df)) for label in y_df.unique()}
    
    # Initialize the upsampled DataFrames
    X_train_oversampled = pd.DataFrame()
    y_train_oversampled = pd.Series()

    # Perform manual oversampling for each class
    for label, target_count in sample_proportions.items():
        indices = y_df[y_df == label].index
        if len(indices) == 0:
            continue
        if target_count <= len(indices):
            sampled_indices = np.random.choice(indices, target_count, replace=False)
        else:
            sampled_indices = np.random.choice(indices, target_count, replace=True)
        X_train_oversampled = pd.concat([X_train_oversampled, X_df.loc[sampled_indices]], axis=0)
        y_train_oversampled = pd.concat([y_train_oversampled, y_df.loc[sampled_indices]])

    # Reset index to avoid duplicate indices
    X_train_oversampled.reset_index(drop=True, inplace=True)
    y_train_oversampled.reset_index(drop=True, inplace=True)

    if verbose == 1:
        print("After upsampling: ")
        print(y_train_oversampled.value_counts(), "\n")
    
    return [X_train_oversampled, y_train_oversampled]


def test_upsampling():
    df_path = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python Modeling\Modeling 01\Dataset Classification\04 Credit Risk Customer.csv"
    df = pd.read_csv(df_path)
    y_name = 'property_magnitude'
    X_data = df.drop(columns = [y_name])
    y_data = df[y_name]
    strategy = {
        'real estate':1
        ,'life insurance':2
        ,'no known property':3
        ,'car':4
        }
    
    X_train_oversampled, y_train_oversampled = upsampling(X_data,y_data,strategy=strategy)
    print()

test_upsampling()