import pandas as pd
import matplotlib.pyplot as plt



df=pd.read_csv('student_math_clean.csv')


print(df.columns)

df=
for i in df.columns:
    print(f'{i} : {df[i].unique}')
class StudentAnalysis:
    def __init__(self,df):
        self.df=df



    def show_specific_column(self,column):

        print(self.df[column])


    def sex_analysis(self):
        grouped=self.df.groupby('sex')['student_id'].count()

        grouped.plot(kind='bar')

        plt.show()

    def alcohol_and_parents(self):

        print(self.df['parent_status'].unique())

        print(self.df['weekend_alcohol'].unique())



        self.df.plot(kind='scatter',y='weekend_alcohol',x='absences',title="Zaleznosc")

        plt.show()

    def show_best_students(self):
        self.df['overall_best_students']=(self.df['grade_1']+self.df['grade_2']+self.df['final_grade'])/3

        sorted=self.df.sort_values(by='overall_best_students',ascending=True)

    def rozklad_wieku(self):
        groupie=self.df.groupby("age")['student_id'].count()

        groupie.plot(kind='bar')
        plt.show()

    def living_space(self):
        grouped=self.df.groupby("address_type")['student_id'].count()

        grouped.plot.pie(y=grouped.values,labels=grouped.index,autopct='%1.1f%%')


        plt.title("Living Space")


        plt.show()


    def korelacja_ucznia_rodzica(self):

        grouped1=self.df.groupby("mother_job")['student_id'].count()

        grouped2=self.df.groupby("father_job")['student_id'].count()

        print("Najbardziej powszechne prace wsrod matek")
        sorted=grouped1.sort_values(ascending=False)
        print(sorted)

        print("Najbardziej powszechne prace wsrod ojcow")
        sorted = grouped2.sort_values(ascending=False)
        print(sorted)

studentanalysis=StudentAnalysis(df)

app=StudentAnalysis(df)

app.korelacja_ucznia_rodzica()