import pandas as pd

data1 = {
    'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
    'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
    'marks': [200, 210, 190, 222, 199]
}

student_data1 = pd.DataFrame(data1)

# Creating the second dataframe
data2 = {
    'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
    'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'],
    'marks': [201, 200, 198, 219, 201]
}
student_data2=pd.DataFrame(data2)





#Along rows
merged2=pd.concat([student_data1,student_data2])

print(merged2)

#Along columns

merged3=pd.concat([student_data1,student_data2],axis=1)
print(merged3)

data = {
    'student_id': ['S1', 'S2', 'S3', 'S4', 'S5', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'],
    'exam_id': [23, 45, 12, 67, 21, 55, 33, 14, 56, 83, 88, 12]
}

exam_data=pd.DataFrame(data)
def adding_students(id,name,marks):
    global student_data1
    new_student=pd.DataFrame({'student_id':[id],'name':[name],'marks':[marks]})
    student_data1=pd.concat([student_data1,new_student],ignore_index=True)

adding_students('S8',"Dick",420)

print(student_data1)

#Write a Pandas program to join the two given dataframes along rows and merge with another dataframe along the common column id

result_data=pd.concat([student_data1,student_data2])


new=pd.merge(result_data,exam_data,on='student_id')

print(new)


#Write a Pandas program to join the two dataframes using the common column of both dataframes.

merged=pd.merge(student_data1,student_data2,on='student_id')
print(merged)

#7. Write a Pandas program to join the two dataframes with matching records from both sides where available.



merged2=pd.merge(student_data1,student_data2,on='student_id',how='outer')

print(merged2)