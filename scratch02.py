# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 13:02:20 2023

@author: Heng2020
"""
import pandas as pd

if output_folder is None:
    out_excel_path = str(out_excel_name_in)
else:
    out_excel_path = str(Path(output_folder) / Path(out_excel_name_in))

import numpy as np
import random

# Create a list of 10 random categories
categories = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# Create a list of 10 column names
columns = ["col_" + str(i) for i in range(1, 11)]

# Create a dataframe of 10 rows and 10 columns with random values
df = pd.DataFrame(np.random.randint(1e6, 1e9, size=(10, 10)), columns=columns)

# Assign a random category to each row
df["category"] = random.choices(categories, k=10)

# Display the dataframe
print(df)

# Import datatable
import datatable as dt

# Create a Frame from a list of dictionaries
DT = dt.Frame([{"name": "Alice", "age": 25, "gender": "F"},
               {"name": "Bob", "age": 30, "gender": "M"},
               {"name": "Charlie", "age": 35, "gender": "M"}])

# Display the Frame
print(DT)

# name     age  gender
# str32  int32  str32
# Alice     25      F
# Bob       30      M
# Charlie   35      M

# Select the first two rows and the last column
print(DT[:2, -1])

# gender
# str32
# F
# M

# Filter the rows where age is greater than 30
print(DT[dt.f.age > 30, :])

# name     age  gender
# str32  int32  str32
# Bob       30      M
# Charlie   35      M

# Create a new column with the length of the name
DT[:, dt.update(name_len = dt.len(dt.f.name))]
print(DT)

# name     age  gender  name_len
# str32  int32  str32     int32
# Alice     25      F



