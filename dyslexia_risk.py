import pandas as pd
from datetime import datetime
from tkinter import filedialog as fd
import os.path
import numpy as np

filepath='9_19_2022 All student Data.txt'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='District PS Data', initialdir='.', filetypes=(('TXT files','*.txt'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')
sid['Last_Name'] = sid['Last_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sid['First_Name'] = sid['First_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sid['Middle_Name'] = sid['Middle_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sid['Name'] = sid['Last_Name'] + ', ' + sid['First_Name']

filepath= fd.askopenfilename(title='Student Data KDG', initialdir='.', filetypes=(('csv files','*.csv'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_csv(filepath, header=0)

sheet['LastName'] = sheet['LastName'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sheet['FirstName'] = sheet['FirstName'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())

#merged = sheet.merge(sid, how='left', left_on=['First_Name', 'Last_Name'], right_on=['Last_Name','First_Name'])
merged = sheet.merge(sid, how='left', left_on=['LastName', 'FirstName'], right_on=['Last_Name', 'First_Name'])

datafile = pd.DataFrame()

datafile['Student First Name'] = merged['First_Name'].copy()
datafile['Student Last Name'] = merged['Last_Name'].copy()
datafile['Student Middle Initial'] = merged['Middle_Name'].copy()

datafile['Date Of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = merged['Grade_Level'].copy()

datafile['Student ID'] = merged['Student_Number'].copy()
datafile['State Student ID'] = merged['State_StudentNumber'].copy()

datafile['RiskIndicator'] = merged['RiskIndicator'].copy()
datafile['Assessment Group'] = 'Mind Play Dyslexia'
datafile['Assessment Name'] = 'Mindplay Risk Indicator'
datafile['Assessment Window'] = 'MOY'

datafile['School Year'] = '2022-2023'

datafile['State Student ID'].replace('', np.nan, inplace=True)
datafile.dropna(subset=['State Student ID'], inplace=True)

datafile = datafile.replace('At risk', '25')
datafile = datafile.replace('Some risk', '50')
datafile = datafile.replace('Not at risk', '100')

now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_csv('mindplay_merged-'+ dt+'.csv', sep=',', index=False)
