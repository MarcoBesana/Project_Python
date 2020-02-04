#!/usr/bin/env python
# coding: utf-8

# In[116]:


import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *
import tkinter as tkr
import csv
import tkinter
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

df=pd.read_csv('C:\\Users\\Klimz\\Desktop\\cars.csv',delimiter=';',nrows=408,skiprows=[1])
df
GUI=Tk()
GUI.title("Cars")
GUI.geometry("300x130")

def Power_Weight():
    
    y=df['Weight'];
    x=df['Horsepower']
    fig1,ax1=plt.subplots()
    ax1.scatter(x,y)
    ax1.set_title('Relationship between Horsepower and Weight')
    ax1.set_xlabel('Horsepower'); ax1.set_ylabel('Weight');
    
Power_Weight=tkr.Button(GUI,width=5, height=3, text="Relationship between Horsepower and Weight", command=Power_Weight)
Power_Weight.pack(fill="x")
def ShowData():
    y=df['Acceleration'];
    x=df['Horsepower']
    fig2,ax2=plt.subplots()
    ax2.scatter(x,y)
    ax2.set_title('Relationship between Acceleratione and Horsepower')
    ax2.set_xlabel('Acceleration'); ax2.set_ylabel('Horsepower');
    
    
ShowData=tkr.Button(GUI,width=5, height=3, text="Relationship between Acceleratione and Horsepower", command=ShowData)
ShowData.pack(fill="x")

GUI.mainloop()


# In[ ]:





# In[ ]:




