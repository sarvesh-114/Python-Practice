import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

data = pd.read_excel(r"C:\Users\sarvesh jathar\Downloads\PAN+Card+Validation+in+PYTHON+-+Scripts\PAN Card Validation in PYTHON - Scripts\PAN Number Validation Dataset.xlsx")
data.head()

print(f'The dataset has {data.shape[0]} rows and {data.shape[1]} row')

data['Pan_Numbers'] = data['Pan_Numbers'].astype('string').str.strip().str.upper()

data.head()

data[data['Pan_Numbers'] == '']

data.isnull().sum()

data = data.replace({'Pan_Numbers' : ''}, pd.NA)

data = data.dropna()
data.shape

data.duplicated().sum()
data['Pan_Numbers'].nunique()
data.drop_duplicates(inplace = True)
data.shape

def has_adjacent_repitition(pan):
    # for i in range(len(pan)-1):
    #     if pan[i] == pan[i+1]:
    #         return True
    # return False
    return any(pan[i] == pan[i+1] for i in range(len(pan) - 1))

print(has_adjacent_repitition('ABCDE'))
print(has_adjacent_repitition('AABCD'))

def is_sequential(pan):
    # for i in range(len(pan)-1):
    #     if ord(pan[i+1]) - ord(pan[i]) !=1:
    #         return False
    # return True
    return all(ord(pan[i+1]) - ord(pan[i]) ==1 for i in range(len(pan)-1))

print(is_sequential('ABCDO'))
print(is_sequential('MNOPQ'))
print(is_sequential('AAAAA'))

import re

def is_pan_valid(pan):
    if len(pan) != 10:
        return False

    if not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', pan):
        return False

    if has_adjacent_repitition(pan):
        return False

    if is_sequential(pan):
        return False
    return True

data['Status'] = data["Pan_Numbers"].apply(
    lambda x: "Valid" if is_pan_valid(x) else "Invalid"
)
