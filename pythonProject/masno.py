import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import random
import tkinter as tk

with open('data.jsonl') as jsonl_file:
    data_list=[json.loads(line)for line in jsonl_file]

questions=[]
for data in data_list:
    questions.append(data['response'])



class App:
    def __init__(self,master):
        self.master=master


        self.label=tk.Label(self.master,text="Test")
        self.label.pack()


        self.btn=tk.Button(self.master,text='Generuj pytanie',command=self.generate)
        self.btn.pack()


        self.textbox=tk.Entry(self.master)
        self.textbox.config(width=100)
        self.textbox.pack()
    def generate(self):
        text=random.choice(questions)

        self.textbox.delete(0,tk.END)
        self.textbox.insert(0,text)
root=tk.Tk()

app_instance=App(root)

root.mainloop()

print(random.choice(questions))
df=pd.read_csv("road_accidents_czechia_2016_2022.csv")


print(df.columns)
filtered=df[df["killed_persons"]>=3]



print(filtered[['crash_kind','cause_of_accident','alcohol']])



