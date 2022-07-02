import pandas as pd
from datetime import datetime
from tkinter import filedialog as fd
import os.path

def school_year() -> str:
    month = int(datetime.now().month)
    year = int(datetime.now().year)

    if month >= 8:
        return str(year) +'-'+ str(year+1)
    return  str(year-1) +'-'+  str(year)

filepath='PS Big File.txt'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='Powerschool data', initialdir='.', filetypes=(('TXT files','*.txt'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')

filepath= fd.askopenfilename(title='Zillion Student Data', initialdir='.', filetypes=(('CSV files','*.csv'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_csv(filepath)
sheet['Student First Name'] = sheet['Student First Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'"))
sheet['Student Last Name'] = sheet['Student Last Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'"))

merged = sheet.merge(sid, how='left', left_on=['Student Last Name', 'Student First Name'], right_on=['Last_Name','First_Name'])

datafile = pd.DataFrame()

datafile['Student First Name'] = merged['Student First Name'].copy()
datafile['Student Middle Initial'] = ""
datafile['Student Last Name'] = merged['Student Last Name'].copy()
#datafile['Student'] = merged['Student Last Name']+ ', ' + merged['Student First Name']
datafile['Student ID'] = merged['State_StudentNumber'].copy()
datafile['School Year'] = school_year() #merged[''].copy()
datafile['Assessment Name'] = merged['Assignment Name'].copy()
datafile['Score'] = merged['Correct'].copy()
datafile['Assessment Group'] = "IM Learnzillion"
datafile['Assessment Window'] = merged['Assignment Name'].copy()
datafile['Date of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = "" #merged[''].copy()

datafile['Assessment Window'] = datafile['Assessment Window'].apply(lambda x: "MU" if "Mid-Unit" in x else "EOU")

now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_excel('Zill-merged-'+dt+'.xlsx', index=False)
#datafile.to_csv('Zill-merged-'+dt+'.csv', index=False)



