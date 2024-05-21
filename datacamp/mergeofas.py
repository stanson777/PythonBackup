import pandas as pd



temperature = pd.DataFrame({'date': pd.date_range(start='2024-01-01', end='2024-01-10'),
                            'temperature': [20, 22, 19, 18, 17, 20, 23, 24, 21, 22]})
precipitation = pd.DataFrame({'date': pd.date_range(start='2024-01-01', end='2024-01-10'),
                               'precipitation': [0.5, 0.7, 0.3, 0.1, 0.0, 0.4, 0.8, 0.9, 0.6, 0.7]})



merged_data=pd.merge_asof(temperature,precipitation,on='date',direction='nearest')


print(merged_data)
merged_data2=pd.merge_asof(temperature,precipitation,on='date')



print(merged_data2)


print(pd.merge(temperature,precipitation,on='date'))


transactions = pd.DataFrame({
    'date': pd.to_datetime(['2024-01-01', '2024-01-04', '2024-01-07', '2024-01-10', '2024-01-15']),
    'amount': [100, 200, 150, 300, 250]
})

# Ramka danych z danymi o kursach walutowych
exchange_rates = pd.DataFrame({
    'date': pd.to_datetime(['2024-01-01', '2024-01-05', '2024-01-08', '2024-01-10', '2024-01-15']),
    'currency': ['USD', 'USD', 'USD', 'USD', 'USD'],
    'rate': [1.2, 1.3, 1.4, 1.35, 1.38]
})


print(transactions)

print(exchange_rates)
print(pd.merge_asof(transactions,exchange_rates,on='date'))
print(pd.merge_asof(transactions,exchange_rates,on='date',direction='nearest'))