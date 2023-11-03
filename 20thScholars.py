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

filepath='MCHS.txt'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='District PS Data', initialdir='.', filetypes=(('TXT files','*.txt'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')

filepath= fd.askopenfilename(title='21st Century', initialdir='.', filetypes=(('XLSX files','*.xlsx'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_excel(filepath, header=0)
sheet['Student First Name'] = sheet['FIRST NAME'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'"))
sheet['Student Last Name'] = sheet['LAST NAME'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'"))

#merged = sheet.merge(sid, how='left', left_on=['Last_Name', 'First_Name'], right_on=['Student Last Name', 'Student First Name'])
merged = sheet.merge(sid, how='left', left_on=['Student Last Name', 'Student First Name'], right_on=['Last_Name', 'First_Name'])

datafile = pd.DataFrame()

datafile['Student Last Name'] = merged['Last_Name'].copy()
datafile['Student First Name'] = merged['First_Name'].copy()
datafile['Student Middle Initial'] = merged['Middle_Name'].copy()
datafile['Student ID'] = merged['Student_Number'].copy()
datafile['Score'] = merged['21ST APPLICATION STATUS'].copy()
datafile['Assessment Name'] = '21st Century Scholars' #merged['Assessment Name'].copy()
datafile['Assessment Window'] = merged['21ST APPLICATION YEAR'].copy()
datafile['School Year'] = school_year()
datafile['Date of Birth'] = merged['DATE OF BIRTH'].copy()
datafile['Student Grade Level'] = merged['Grade_Level'].copy()
datafile['Assessment Group'] = merged['COHORT YEAR'].copy()
datafile['Name Mismatch'] = merged['Student Last Name'].copy() + ', ' + merged['Student First Name'].copy()


now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_excel('20thCenturyScholars-merged-'+dt+'.xlsx', index=False)




