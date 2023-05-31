import pandas as pd
from datetime import datetime
from tkinter import filedialog as fd
import os.path
import numpy as np

append=''
sheetName='2024'
today = datetime.now().strftime("%Y%m%d-%M%S")

filepath='9_19_2022 All student Data.txt'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='District PS Data', initialdir='.', filetypes=(('TXT files','*.txt'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')
sid['Last_Name'] = sid['Last_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sid['First_Name'] = sid['First_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sid['Middle_Name'] = sid['Middle_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sid['ShortName'] = sid['Last_Name'] + ', ' + sid['First_Name']
sid['LongName'] = sid['Last_Name'] + ', ' + sid['First_Name'] + ' ' + sid['Middle_Name']

filepath= fd.askopenfilename(title='Student Data', initialdir='.', filetypes=(('xlsx files','*.xlsx'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_excel(filepath, header=0, sheet_name=sheetName)

sheet['lower_name'] = sheet['Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())

#merged = sheet.merge(sid, how='left', left_on=['First_Name', 'Last_Name'], right_on=['Last_Name','First_Name'])

mergedShort = pd.DataFrame()
mergedLong = pd.DataFrame()

mergedShort = sheet.merge(sid, how='left', left_on=['lower_name'], right_on=['ShortName'])
mergedShort.dropna(subset=['ShortName'], inplace=True)

mergedLong = sheet.merge(sid, how='left', left_on=['lower_name'], right_on=['LongName'])
mergedLong.dropna(subset=['LongName'], inplace=True)

merged = pd.concat([mergedShort, mergedLong])
merged['Middle_Name'].replace('nan', '', inplace=True)
merged.sort_values(by=['Name'], inplace=True)


datafile = pd.DataFrame()

datafile['Student First Name'] = merged['First_Name'].copy()
datafile['Student Last Name'] = merged['Last_Name'].copy()
datafile['Student Middle Initial'] = merged['Middle_Name'].copy()

datafile['Student ID'] = merged['Student_Number'].copy()
datafile['Date Of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = merged['Grade_Level'].copy()
datafile['School Year'] = '2022-2023'

#datafile['State Student ID'] = merged['State_StudentNumber'].copy()

datafile['Score'] = merged['Graduation Track Status'].copy()

datafile['Assessment Window'] = 'Semester 2'
datafile['Assessment Group'] = 'On Track Status'
datafile['Assessment Name'] = 'On Track'

datafile.to_csv('OnTrack_'+sheetName+'_merged-'+ today +'.csv', sep=',', index=False)
