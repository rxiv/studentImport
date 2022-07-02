import pandas as pd
from datetime import datetime
from tkinter import filedialog as fd
import os.path

filepath='PS Big File.txt'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='District PS Data', initialdir='.', filetypes=(('TXT files','*.txt'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')

missing = sid.loc[sid['State_StudentNumber'].isnull()]
missing = missing.sort_values(by=['Last_Name', 'First_Name'])
#print(missing.columns)

now = datetime.now()
dt = now.strftime("%Y%m%d")
missing.to_excel('missing-student_ID-'+dt+'.xlsx', index=False)


