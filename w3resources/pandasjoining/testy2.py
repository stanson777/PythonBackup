import pandas as pd


data1 = pd.DataFrame({
    'key1': ['K0', 'K0', 'K1', 'K2'],
    'key2': ['K0', 'K1', 'K0', 'K1'],
    'P': ['P0', 'P1', 'P2', 'P3'],
    'Q': ['Q0', 'Q1', 'Q2', 'Q3']
})

# Define data2
data2 = pd.DataFrame({
    'key1': ['K0', 'K1', 'K1', 'K2'],
    'key2': ['K0', 'K0', 'K0', 'K0'],
    'R': ['R0', 'R1', 'R2', 'R3'],
    'S': ['S0', 'S1', 'S2', 'S3']
})


#8. Write a Pandas program to join (left join) the two dataframes using keys from left dataframe only.

merged_left=pd.merge(data1,data2,on=['key1','key2'],how='left')

print(merged_left)


#9. Write a Pandas program to join two dataframes using keys from right dataframe only.

merged_right=data1.merge(data2,on=['key1','key2'],how='right')

print(merged_right)
