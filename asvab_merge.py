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
    filepath = fd.askopenfilename(title='District PS Data', initialdir='.', filetypes=(('TXT files','*.txt'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')
sid['name'] = sid['Last_Name']+ ', ' + sid['First_Name']

filepath= fd.askopenfilename(title='ASVAB Spreadsheet', initialdir='.', filetypes=(('xlsx files','*.xlsx'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_excel(filepath, header=1, usecols=[0,1])
sheet.columns = ['Seniors','Score']
sheet.dropna(subset='Score', inplace=True)
sheet['Seniors'] = sheet['Seniors'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'"))

#merged = sheet.merge(sid, how='left', left_on=['First_Name', 'Last_Name'], right_on=['Last_Name','First_Name'])
merged = sheet.merge(sid, how='left', left_on=['Seniors'], right_on=['name'])

datafile = pd.DataFrame()

datafile['Student First Name'] = merged['First_Name'].copy()
datafile['Student Middle Initial'] = ""
datafile['Student Last Name'] = merged['Last_Name'].copy()
datafile['Student ID'] = merged['State_StudentNumber'].copy()
datafile['School Year'] = school_year() #merged['Date Completed'].copy()
datafile['Assessment Name'] = "AFQT" #merged['Level'].copy()
datafile['Score'] = merged['Score'].copy()
datafile['Assessment Group'] = "ASVAB"
datafile['Assessment Window'] = "2021" #merged['Attempt'].copy() 
datafile['Date of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = "12" #merged[''].copy()

datafile['MergeName'] = merged['Seniors'].copy()

now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_excel('ASVAB-Seniors-'+dt+'.xlsx', index=False)

sheet = pd.read_excel(filepath, header=1, usecols=[2,3])
sheet.columns = ['Juniors','Score']
sheet.dropna(subset='Score', inplace=True)
sheet['Juniors'] = sheet['Juniors'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'"))

#merged = sheet.merge(sid, how='left', left_on=['First_Name', 'Last_Name'], right_on=['Last_Name','First_Name'])
merged = sheet.merge(sid, how='left', left_on=['Juniors'], right_on=['name'])

datafile = pd.DataFrame()

datafile['Student First Name'] = merged['First_Name'].copy()
datafile['Student Middle Initial'] = ""
datafile['Student Last Name'] = merged['Last_Name'].copy()
datafile['Student ID'] = merged['State_StudentNumber'].copy()
datafile['School Year'] = school_year() #merged['Date Completed'].copy()
datafile['Assessment Name'] = "AFQT" #merged['Level'].copy()
datafile['Score'] = merged['Score'].copy()
datafile['Assessment Group'] = "ASVAB"
datafile['Assessment Window'] = "2021" #merged['Attempt'].copy() 
datafile['Date of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = "11" #merged[''].copy()

datafile['MergeName'] = merged['Juniors'].copy()

now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_excel('ASVAB-Juniors-'+dt+'.xlsx', index=False)


