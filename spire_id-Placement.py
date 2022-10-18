import pandas as pd
from datetime import datetime
from tkinter import filedialog as fd
import os.path
import numpy as np

append='set_1'

filepath='9_19_2022 All student Data.txt'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='District PS Data', initialdir='.', filetypes=(('TXT files','*.txt'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')
sid['Last_Name'] = sid['Last_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sid['First_Name'] = sid['First_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sid['Middle_Name'] = sid['Middle_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sid['Name'] = sid['First_Name'] + ' ' + sid['Last_Name']

filepath= fd.askopenfilename(title='Student Data', initialdir='.', filetypes=(('xlsx files','*.xlsx'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_excel(filepath, header=0)

sheet['lower_name'] = sheet['Student'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())

#merged = sheet.merge(sid, how='left', left_on=['First_Name', 'Last_Name'], right_on=['Last_Name','First_Name'])
merged = sheet.merge(sid, how='left', left_on=['lower_name'], right_on=['Name'])

datafile = pd.DataFrame()

datafile['Teacher'] = merged['Teacher'].copy()
datafile['Email'] = merged['Email'].copy()
datafile['Class'] = merged['Class'].copy()

datafile['Student First Name'] = merged['First_Name'].copy()
datafile['Student Last Name'] = merged['Last_Name'].copy()
datafile['Student Middle Initial'] = merged['Middle_Name'].copy()

datafile['Date Of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = merged['Grade_Level'].copy()
datafile['School Year'] = '2022-2023'
datafile['Student ID'] = merged['Student_Number'].copy()
datafile['State Student ID'] = merged['State_StudentNumber'].copy()

datafile['Level'] = merged['Level'].copy()
datafile['Date'] = merged['Date'].copy()
datafile['Errors'] = merged['Errors'].copy()
datafile['Teacher Comment'] = merged['Teacher Comment'].copy()

now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_csv('spire-merged-Placement-' + dt+'.csv', sep=',', index=False)