import pandas as pd
import numpy as np
# Sample licenses DataFrame
licenses_data = {
    'account': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'license_type': ['TypeA', 'TypeB', 'TypeA', 'TypeC', 'TypeB', 'TypeA', 'TypeC', 'TypeB', 'TypeA', 'TypeC'],
    'license_fee': [100, 150, 120, 200, 180, 130, 220, 160, 190, 210],
    'year_issued': [2022, 2023, 2022, 2024, 2023, 2022, 2024, 2023, 2022, 2024]
}

licenses = pd.DataFrame(licenses_data)

# Sample biz_owners DataFrame
owners_data = {
    'account': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'title': ['CEO', 'Secretary', 'CEO', 'Vice President', 'Secretary', 'CEO', 'Vice President', 'CEO', 'Secretary', 'Vice President'],
    'gender': ['Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Male']
}

biz_owners = pd.DataFrame(owners_data)

# Displaying the sample DataFrames
print("Licenses DataFrame:")
print(licenses)

print("\nBiz Owners DataFrame:")
print(biz_owners)



#1.Total Number of Licenses per Business Owner


licenses_biz=licenses.merge(biz_owners,on='account')

grouped_licenses_biz=licenses_biz.groupby('account')['title'].count()


print(grouped_licenses_biz)



#2.Average License Fee by Business Owner Title

grouped2_licenses_biz=licenses_biz.groupby('title')['license_fee'].mean()

print(grouped2_licenses_biz)



#3.List Business Owners with Multiple Licenses
# I cannot do that becouse i dont get enough data to do this

#4.Most Common License Type by Business Owner
grouped3_licenses_biz=licenses_biz.groupby('license_type')['account'].count()

print(grouped3_licenses_biz)
print(f"Most common license type is: {grouped3_licenses_biz.mode()}")



#5.Not enough data to do this


#6.Number of Licenses Issued Each Year

grouped4_licenses_biz=licenses_biz.groupby('year_issued')['license_fee'].count()

print(grouped4_licenses_biz)

#7.Business Owners with Highest Total License Fees


sorted_licenses_biz=licenses_biz.sort_values(by='license_fee',ascending=False)
print(sorted_licenses_biz)


#8.Percentage of Licenses Held by Top Business Owners

suma_of_licenses=np.sum(licenses_biz['license_fee'])
print(suma_of_licenses)


licenses_biz['percentage']=(licenses_biz['license_fee']/suma_of_licenses)*100
def percentage_of_licenses(n):
    sorted2_licenses_biz=licenses_biz.sort_values(by='percentage',ascending=False)
    if n<=len(licenses_biz):
        return sorted2_licenses_biz.head(n)
    else:
        return "Number you give is too high"


print(percentage_of_licenses(3))


#9.Not enough data


#10.Average License Fee by Business Owner Gender

grouped5_license_biz=licenses_biz.groupby('gender')['license_fee'].mean()

print(grouped5_license_biz)




#11.Product Sales

# Sample sales DataFrame
sales_data = {
    'product_id': [1, 2, 1, 3, 2, 1, 3, 2, 1, 3],
    'quantity_sold': [10, 5, 8, 15, 12, 7, 18, 14, 9, 20],
    'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-01', '2022-01-02', '2022-01-03', '2022-01-01', '2022-01-02', '2022-01-03', '2022-01-01']
}

sales = pd.DataFrame(sales_data)

# Sample products DataFrame
products_data = {
    'product_id': [1, 2, 3],
    'product_name': ['ProductA', 'ProductB', 'ProductC'],
    'category': ['Electronics', 'Clothing', 'Home Appliances']
}

products = pd.DataFrame(products_data)


merged_sales_products=sales.merge(products,on='product_id')


print(merged_sales_products)
print(merged_sales_products.groupby(['product_id','category'],as_index=False)['quantity_sold'].sum())



#3.Customer Orders


# Sample orders DataFrame
orders_data = {
    'order_id': [1, 2, 3, 4, 5],
    'customer_id': [101, 102, 103, 101, 104],
    'order_date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05']
}

orders = pd.DataFrame(orders_data)

# Sample order_details DataFrame
order_details_data = {
    'order_id': [1, 1, 2, 3, 3, 3, 4, 5],
    'product_id': [101, 102, 103, 104, 105, 106, 107, 108],
    'quantity': [5, 3, 2, 4, 1, 3, 2, 6]
}

order_details = pd.DataFrame(order_details_data)



orders_merged=orders.merge(order_details,on='order_id')



grouped_orders=orders_merged.groupby(["customer_id","product_id"])['quantity'].sum()

print(grouped_orders)

#** Just for fun

print(orders_merged)


# above or equal as avg_quantity


print(orders_merged[orders_merged["quantity"]>=np.mean(orders_merged["quantity"])])


#4.Library Books


# Sample books DataFrame
books_data = {
    'book_id': [1, 2, 3, 4, 5],
    'title': ['BookA', 'BookB', 'BookC', 'BookD', 'BookE'],
    'author': ['Author1', 'Author2', 'Author3', 'Author1', 'Author4']
}

books = pd.DataFrame(books_data)

# Sample loans DataFrame
loans_data = {
    'loan_id': [101, 102, 103, 104, 105],
    'customer_id': [201, 202, 203, 201, 204],
    'book_id': [1, 2, 1, 3, 2],
    'return_date': ['2022-01-05', '2022-01-08', '2022-01-10', '2022-01-12', '2022-01-15']
}

loans = pd.DataFrame(loans_data)



merged_books_loan=books.merge(loans,on='book_id')

print(merged_books_loan)

print(merged_books_loan.groupby(['book_id','title'])['loan_id'].count())