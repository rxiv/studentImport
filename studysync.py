import pandas as pd
from datetime import datetime
from tkinter import filedialog as fd
import os.path
import numpy as np

def school_year() -> str:
    month = int(datetime.now().month)
    year = int(datetime.now().year)

    if month >= 8:
        return str(year) +'-'+ str(year+1)
    return  str(year-1) +'-'+  str(year)

filepath='2022_2023 PS.txt'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='District PS Data', initialdir='.', filetypes=(('TXT files','*.txt'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')
sid['Name'] = sid['Last_Name'] + ', ' + sid['First_Name']

filepath= fd.askopenfilename(title='StudySync', initialdir='.', filetypes=(('XLSX files','*.xlsx'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_excel(filepath, header=0)
sheet['Student'] = sheet['Student'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'"))

merged = sheet.merge(sid, how='left', left_on=['Student'], right_on=['Name'])

datafile = pd.DataFrame()

datafile['Assessment Name'] = merged['Assessment Name'].copy()
datafile['Teacher'] = merged['Teacher'].copy()
datafile['Group'] = merged['Group'].copy()
datafile['Student'] = merged['Student'].copy()
datafile['Requires Grading'] = merged['Requires Grading'].copy()
datafile['Question Count'] = merged['Question Count'].copy()
datafile['Score'] = merged['Score'].copy()

datafile['Student ID'] = merged['Student_Number'].copy()
datafile['School Year'] = school_year()
datafile['Date of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = merged['[1]Grade_Level'].copy()
#datafile['Name Mismatch'] = merged['Student Last Name'].copy()

now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_csv('StudySync-merged-'+dt+'.csv', index=False)




