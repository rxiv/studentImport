import pandas as pd
from datetime import datetime
from tkinter import filedialog as fd
import os.path

filepath='PS BIG File.txt'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='District PS Data', initialdir='.', filetypes=(('TXT files','*.txt'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')
sid['name'] = sid['Last_Name'] + ', ' + sid['First_Name']

sid['lower_first'] = sid['First_Name'].apply(lambda x: str(x).lower())
sid['lower_last'] = sid['Last_Name'].apply(lambda x: str(x).lower())


filepath= fd.askopenfilename(title='Misc File', initialdir='.', filetypes=(('XLSX files','*.xlsx'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_excel(filepath, header=0)
sheet['First Name'] = sheet['First Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sheet['Last Name'] = sheet['Last Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())

merged = sheet.merge(sid, how='left', left_on=['Last Name', 'First Name'], right_on=['lower_last', 'lower_first'])

datafile = pd.DataFrame()

datafile['Student First Name'] = merged['First_Name'].copy()
datafile['Student Middle Initial'] = ""
datafile['Student Last Name'] = merged['Last_Name'].copy()
datafile['Student [ID'] = merged['State_StudentNumber'].copy()
datafile['School Year'] = '2021-2022' #merged['School Year'].copy()
datafile['Assessment Name'] = 'On Track' #merged['Assessment Name'].copy()
datafile['Score'] = merged['Graduation Track Status'].copy()
datafile['Assessment Group'] = 'On Track Status' #merged['Assessment Group'].copy()
datafile['Assessment Window'] = 'Semester 1' #merged['Assessment Window'].copy()
datafile['Date of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = '' #merged['Student Grade Level'].copy()
datafile['Name Mismatch'] = merged['Last Name'].copy()
datafile['Name Mismatch2'] = merged['First Name'].copy()


now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_excel('OnTrack-merged-'+dt+'.xlsx', index=False)




