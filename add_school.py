import pandas as pd
from datetime import datetime
from tkinter import filedialog as fd
import os.path


filepath='schools.text'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='School Listing', initialdir='.', filetypes=(('TXT files','*.text'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')
sid['name'] = sid['Last_Name'] + ', ' + sid['First_Name']

filepath= fd.askopenfilename(title='IREAD data', initialdir='.', filetypes=(('XLSX files','*.xlsx'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_excel(filepath, header=0)
sheet['Student'] = sheet['Student'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'"))
sheet.columns = sheet.columns.str.strip()

merged = sheet.merge(sid, how='left', left_on=['Student'], right_on=['name'])

datafile = pd.DataFrame()

datafile['Student'] = merged['Student'].copy()
datafile['State ID'] = merged['State ID'].copy()
datafile['DOB'] = merged['DOB'].copy()
datafile['EL Status'] = merged['EL Status'].copy()
datafile['Special Ed'] = merged['Special Ed'].copy()
datafile['Tags'] = merged['Tags'].copy()
datafile['Spring'] = merged['Spring'].copy()
datafile['Summer'] = merged['Summer'].copy()

datafile['S_IN_STU_X.PrimarySchoolEnrollment'] = merged['S_IN_STU_X.PrimarySchoolEnrollment'].copy()
datafile['Enrollment_SchoolID'] = merged['Enrollment_SchoolID'].copy()

now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
#datafile.to_excel('iread-merged-'+dt+'.xlsx', index=False)
datafile.to_csv('iread-merged-'+dt+'.csv', index=False, sep=',')

