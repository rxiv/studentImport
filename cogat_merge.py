import pandas as pd
from datetime import datetime
from tkinter import filedialog as fd
import os.path


# Powerschool data
filepath='9_19_2022 All student Data.txt'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='Powerschool Data', initialdir='.', filetypes=(('TXT files','*.txt'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')
#sid['name'] = sid['Last_Name'] + ', ' + sid['First_Name']
sid['Last_Name'] = sid['Last_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sid['First_Name'] = sid['First_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sid['Middle_Name'] = sid['Middle_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())

# File to merge
filepath= fd.askopenfilename(title='CoGAT', initialdir='.', filetypes=(('XLSX files','*.xlsx'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_excel(filepath, header=0)
#sheet.columns = sheet.columns.str.replace(' ','') # remove spaces in column headers

sheet['Sheet_Last'] = sheet['Last Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sheet['Sheet_First'] = sheet['First Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sheet['Sheet_Middle'] = sheet['Middle Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())

merged = sheet.merge(sid, how='left', left_on=['Sheet_Last', 'Sheet_First', 'Sheet_Middle'], right_on=['Last_Name', 'First_Name', 'Middle_Name'])


# Create the final exportable dataframe
# datafile = pd.DataFrame()

# datafile['Student First Name'] = merged['First'].copy()
# datafile['Student Last Name'] = merged['Last'].copy()
# datafile['Student ID'] = merged['State_StudentNumber'].copy()
# datafile['Date of Birth'] = merged['DOB'].copy()
# datafile['Student Grade Level'] = merged['Grade'].copy()
#datafile['Name Mismatch'] = merged['Last'].copy()


now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
merged.to_csv('Cogat-merged-'+dt+'.csv', index=False, sep=',')



