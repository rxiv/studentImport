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

filepath='PS Big File.txt'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='District PS Data', initialdir='.', filetypes=(('TXT files','*.txt'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')
sid['name'] = sid['Last_Name'] + ', ' + sid['First_Name']

filepath= fd.askopenfilename(title='On Track - Educlimber', initialdir='.', filetypes=(('XLSX files','*.xlsx'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_excel(filepath, header=0)
#sheet['Student First Name'] = sheet['Student First Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'"))
sheet['Student Last Name'] = sheet['Student Last Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'"))

sheet[['last', 'firstmiddle']] = sheet['Student Last Name'].str.split(', ', n=1, expand=True)
sheet[['first', 'middle']] = sheet['firstmiddle'].str.split(' ', n=1, expand=True)

merged = sheet.merge(sid, how='left', left_on=['last', 'first'], right_on=['Last_Name', 'First_Name'])

datafile = pd.DataFrame()

datafile['Student First Name'] = merged['First_Name'].copy()
datafile['Student Middle Initial'] = ""
datafile['Student Last Name'] = merged['Last_Name'].copy()
datafile['Student ID'] = merged['State_StudentNumber'].copy()
datafile['School Year'] = merged['School Year'].copy()
datafile['Assessment Name'] = merged['Assessment Name'].copy()
datafile['Score'] = merged['Score'].copy()
datafile['Assessment Group'] = merged['Assessment Group'].copy()
datafile['Assessment Window'] = merged['Assessment Window'].copy()
datafile['Date of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = merged['Student Grade Level'].copy()
datafile['Name Mismatch'] = merged['Student Last Name'].copy()


now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_excel('OnTrack-merged-'+dt+'.xlsx', index=False)




