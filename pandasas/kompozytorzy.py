import pandas as pd


df=pd.read_csv('classical_composers.csv',encoding='ISO-8859-1')

print(df.index)

print(df.columns)
class ComposerAnalysis:
    def __init__(self,frame):
        self.frame=frame


    def nationality_alpha(self):
        sorted=self.frame.sort_values(by='  Nationality ',ascending=False)

        print(sorted.index)
        print(self.frame.sort_index())
        print("____________________")
        print(self.frame['  Nationality '].value_counts(ascending=False).sort_index(ascending=False))

        return sorted




app=ComposerAnalysis(df)

print(app.nationality_alpha())
