import pandas as pd
from datetime import datetime
from tkinter import filedialog as fd
import os.path

def replace_year(year: str) -> str:
    dt = datetime.strptime(year, '%m/%d/%Y')
    return str(dt.year-1) + '-' + str(dt.year)

def pass_fail(status: str) -> int:
    if status.strip().upper() == "PASS":
        return 1
    return 0

# change
filepath='PS Big File.txt'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='District PS Data', initialdir='.', filetypes=(('TXT files','*.txt'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')

filepath= fd.askopenfilename(title='CTE Student Data', initialdir='.', filetypes=(('CSV files','*.csv'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_csv(filepath)
sheet['Student First Name'] = sheet['Student First Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'"))
sheet['Student Last Name'] = sheet['Student Last Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'"))

merged = sheet.merge(sid, how='left', left_on=['Student Last Name', 'Student First Name'], right_on=['Last_Name','First_Name'])

datafile = pd.DataFrame()

datafile['Student First Name'] = merged['Student First Name'].copy()
datafile['Student Middle Initial'] = ""
datafile['Student Last Name'] = merged['Student Last Name'].copy()
datafile['Student ID'] = merged['State_StudentNumber'].copy()
datafile['School Year'] = merged['Date Completed'].copy()
datafile['Assessment Name'] = merged['Test Name'].copy()
datafile['Score'] = merged['Pass/Fail'].copy()
datafile['Assessment Group'] = "CTE Certification"
datafile['Assessment Window'] = "Yearly" 
datafile['Date of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = "" #merged[''].copy()

datafile['Score'] = datafile['Score'].apply(lambda x: pass_fail(x))
datafile['School Year'] = datafile['School Year'].apply(lambda x: replace_year(x))

now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_excel('cte-merged-'+dt+'.xlsx', index=False)

