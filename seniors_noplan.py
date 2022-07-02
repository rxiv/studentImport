import pandas as pd
from datetime import datetime
from tkinter import filedialog as fd
import os.path

filepath='PS Big File.txt'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='District PS Data', initialdir='.', filetypes=(('TXT files','*.txt'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')

filepath= fd.askopenfilename(title='Senior No Plan', initialdir='.', filetypes=(('xlsx files','*.xlsx'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_excel(filepath, header=0)
sheet['First Name'] = sheet['First Name'].apply(lambda x: x.rstrip())
sheet['Last Name'] = sheet['Last Name'].apply(lambda x: x.rstrip())

#merged = sheet.merge(sid, how='left', left_on=['First_Name', 'Last_Name'], right_on=['Last_Name','First_Name'])
merged = sheet.merge(sid, how='left', left_on=['Last Name', 'First Name'], right_on=['Last_Name','First_Name'])

now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
merged.to_excel('SeniorPlan-'+dt+'.xlsx', index=False)




