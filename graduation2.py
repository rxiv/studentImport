import pandas as pd
from datetime import datetime
from tkinter import filedialog as fd
import os.path
import numpy as np

append=''
sheetName='2026'
today = datetime.now().strftime("%Y%m%d-%M%S")

filepath='2022_2023 PS.txt'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='District PS Data', initialdir='.', filetypes=(('TXT files','*.txt'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')
sid['Last_Name'] = sid['Last_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sid['First_Name'] = sid['First_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sid['Middle_Name'] = sid['Middle_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())

filepath= fd.askopenfilename(title='Student Data', initialdir='.', filetypes=(('xlsx files','*.xlsx'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_excel(filepath, header=0, sheet_name=sheetName)

sheet['lastname'] = sheet['Last Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sheet['firstname'] = sheet['First Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())

merged = sheet.merge(sid, how='left', left_on=['firstname', 'lastname'], right_on=['First_Name','Last_Name'])

merged['Middle_Name'].replace('nan', '', inplace=True)
merged.dropna(subset=['First Name'], inplace=True)

datafile = pd.DataFrame()

datafile['Student First Name'] = merged['First Name'].copy()
datafile['Student Last Name'] = merged['Last Name'].copy()
datafile['Student Middle Initial'] = merged['Middle_Name'].copy()

datafile['Student ID'] = merged['Student_Number'].copy()
datafile['Date Of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = merged['Grade'].copy()
datafile['School Year'] = '2022-2023'

#datafile['State Student ID'] = merged['State_StudentNumber'].copy()

datafile['Score'] = merged['Graduation Track Status'].copy()

datafile['Assessment Window'] = 'Semester 2'
datafile['Assessment Group'] = 'On Track Status'
datafile['Assessment Name'] = 'On Track'

datafile.to_csv('OnTrack_'+sheetName+'_merged-'+ today +'.csv', sep=',', index=False)
