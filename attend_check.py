import pandas as pd
from datetime import datetime
from tkinter import filedialog as fd
import os.path

filepath='attend-merged-20220913-5049.xlsx'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='District PS Data', initialdir='.', filetypes=(('XLSX files','*.xlsx'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_excel(filepath,header=0)
sid['lower_first'] = sid['First_Name'].apply(lambda x: str(x).lower())
sid['lower_last'] = sid['Last_Name'].apply(lambda x: str(x).lower())


filepath= fd.askopenfilename(title='Attendance File', initialdir='.', filetypes=(('XLSX files','*.xlsx'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_excel(filepath, header=0)

merged = sheet.merge(sid, how='left', left_on=['STN'], right_on=['State_StudentNumber'])

#print (merged)
datafile = pd.DataFrame()


now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
merged.to_excel('attend-check-'+dt+'.xlsx', index=False)




