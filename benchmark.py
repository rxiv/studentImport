import pandas as pd
from datetime import datetime
from tkinter import filedialog as fd
import os.path
import numpy as np


filepath='2022_2023 PS.txt'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='District PS Data', initialdir='.', filetypes=(('TXT files','*.txt'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')

filepath= fd.askopenfilename(title='Benchmark', initialdir='.', filetypes=(('XLSX files','*.xlsx'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_excel(filepath, header=0)
sheet['Student First Name'] = sheet['Student First Name'].apply(lambda x: str(x).strip().replace(u"\u2019", "'").replace(u"\u2018", "'"))
sheet['Student Last Name'] = sheet['Student Last Name'].apply(lambda x: str(x).strip().replace(u"\u2019", "'").replace(u"\u2018", "'"))

merged = sheet.merge(sid, how='left', left_on=['Student Last Name', 'Student First Name'], right_on=['Last_Name', 'First_Name'])

datafile = pd.DataFrame()

datafile['Student First Name'] = merged['Student First Name'].copy()
datafile['Student Middle Initial'] = merged['Middle_Name'].copy()
datafile['Student Last Name'] = merged['Student Last Name'].copy()
datafile['Student ID'] = merged['Student_Number'].copy()
datafile['School Year'] = merged['School Year'].copy()
datafile['Assessment Name'] = merged['Assessment Name'].copy()
datafile['Score'] = merged['Score'].copy()
datafile['Assessment Group'] = merged['Assessment Group'].copy()
datafile['Assessment Window'] = merged['Assessment Window'].copy()
datafile['Date of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = merged['[1]Grade_Level'].copy()
#datafile['Name Mismatch'] = merged['Student Last Name'].copy()


now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_csv('Benchmark-merged-'+dt+'.csv', index=False)




