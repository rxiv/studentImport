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

filepath='2022_2023 PS.txt'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='District PS Data', initialdir='.', filetypes=(('TXT files','*.txt'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')

filepath= fd.askopenfilename(title='ASVAB Spreadsheet', initialdir='.', filetypes=(('xlsx files','*.xlsx'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_excel(filepath, header=0)
sheet['Last Name'] = sheet['Last Name'].apply(lambda x: str(x).strip().replace(u"\u2019", "'").replace(u"\u2018", "'"))
sheet['First Name'] = sheet['First Name'].apply(lambda x: str(x).strip().replace(u"\u2019", "'").replace(u"\u2018", "'"))

#merged = sheet.merge(sid, how='left', left_on=['First_Name', 'Last_Name'], right_on=['Last_Name','First_Name'])
merged = sheet.merge(sid, how='left', left_on=['Last Name', 'First Name'], right_on=['Last_Name', 'First_Name'])
#print (merged)

datafile = pd.DataFrame()

datafile['Student First Name'] = merged['First Name'].copy()
datafile['Student Middle Initial'] = merged['Middle_Name'].copy()
datafile['Student Last Name'] = merged['Last Name'].copy()
datafile['Student ID'] = merged['Student_Number'].copy()
datafile['School Year'] = school_year() #merged['Date Completed'].copy()
datafile['Assessment Name'] = "AFQT" #merged['Level'].copy()
datafile['Score'] = merged['AFQT'].copy()
datafile['Assessment Group'] = "ASVAB"
datafile['Assessment Window'] = "2022" #merged['Attempt'].copy() 
datafile['Date of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = merged['Grade Level'].copy()


now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_excel('ASVAB-merge-'+dt+'.xlsx', index=False)
datafile.to_csv('ASVAB-merge-'+dt+'.csv', index=False)


