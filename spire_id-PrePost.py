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
sid['name'] = sid['First_Name'] + ' ' + sid['Last_Name']

filepath= fd.askopenfilename(title='SPIRE Student Data', initialdir='.', filetypes=(('CSV files','*.csv'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_csv(filepath)
sheet['Student'] = sheet['Student'].fillna("*" + sheet['Teacher'] + "*")
sheet['Student'] = sheet['Student'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'"))
merged = sheet.merge(sid, how='left', left_on=['Student'], right_on=['name'])

datafile = pd.DataFrame()

datafile['Student First Name'] = merged['First_Name'].copy()
datafile['Student Middle Initial'] = ""
datafile['Student Last Name'] = merged['Last_Name'].copy()
datafile['Student'] = merged['Student'].copy()

datafile['Student ID'] = merged['State_StudentNumber'].copy()
datafile['School Year'] = school_year() #merged['Date Completed'].copy()
datafile['Assessment Name'] = merged['Level'].copy()
datafile['Score'] = ""
datafile['Assessment Group'] = "SPIRE"
datafile['Assessment Window'] = "1" 
datafile['Date of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = "" #merged[''].copy()

#-------------
datafile['Pre Test DW'] = merged['Pre Test DW'].copy()
datafile['Pre Test DS'] = merged['Pre Test DS'].copy()
datafile['Pre Test CWPM'] = merged['Pre Test CWPM'].copy()
datafile['Pre Test Comp'] = merged['Pre Test Comp'].copy()
datafile['Post Test DW'] = merged['Post Test DW'].copy()
datafile['Post Test DS'] = merged['Post Test DS'].copy()
datafile['Post Test CWPM'] = merged['Post Test CWPM'].copy()
datafile['Post Test Comp'] = merged['Post Test Comp'].copy()

datafile['Assessment Name'] = datafile['Assessment Name'].apply(lambda x: "Level " + str(x))
datafile['Assessment Window'] = datafile['Assessment Window'].apply(lambda x: "Attempt " + str(x))

datafile['Score'] = datafile.iloc[:,12:47].mean(axis=1)

now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_csv('spire-merged-prepost-'+dt+'.csv', index=False, sep=',')


