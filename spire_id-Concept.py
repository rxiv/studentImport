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
datafile['Assessment Window'] = merged['Attempt'].copy() 
datafile['Date of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = "" #merged[''].copy()

#-------------
datafile['Short a'] = merged['Short a'].copy()
datafile['Short i'] = merged['Short i'].copy()
datafile['Short o'] = merged['Short o'].copy()
datafile['Short u'] = merged['Short u'].copy()
datafile['Short e'] = merged['Short e'].copy()
datafile['sh'] = merged['sh'].copy()
datafile['ch'] = merged['ch'].copy()
datafile['th'] = merged['th'].copy()
datafile['wh'] = merged['wh'].copy()
datafile['ang, ing, ong, ung'] = merged['ang, ing, ong, ung'].copy()
datafile['ank, ink, onk, unk'] = merged['ank, ink, onk, unk'].copy()
datafile['ff,ll,ss'] = merged['ff,ll,ss'].copy()
datafile['al'] = merged['al'].copy()
datafile['wa'] = merged['wa'].copy()
datafile['qu'] = merged['qu'].copy()
datafile['ck'] = merged['ck'].copy()
datafile['tch'] = merged['tch'].copy()
datafile['a-e, i-e, o-e, u-e, e-e, Vowel-se'] = merged['a-e, i-e, o-e, u-e, e-e, Vowel-se'].copy()
datafile['se, he, fly'] = merged['se, he, fly'].copy()
datafile['Exceptions'] = merged['Exceptions'].copy()
datafile['ay'] = merged['ay'].copy()
datafile['(-ed)'] = merged['(-ed)'].copy()
datafile['-s, -es, -ing, -er, -est, -en, -ish, -ly, -y, -ful, -ness, -less'] = merged['-s, -es, -ing, -er, -est, -en, -ish, -ly, -y, -ful, -ness, -less'].copy()
datafile['Twin Consonant Syllable Division'] = merged['Twin Consonant Syllable Division'].copy()
datafile['Non-Twin Consonant Syllable Division'] = merged['Non-Twin Consonant Syllable Division'].copy()
datafile['ou'] = merged['ou'].copy()
#datafile['Soft c'] = merged['Soft c'].copy()
#datafile['Soft g'] = merged['Soft g'].copy()
#datafile['er, ur, ir, ear, wor'] = merged['er, ur, ir, ear, wor'].copy()
#datafile['dge'] = merged['dge'].copy()
#datafile['s (/z/)'] = merged['s (/z/)'].copy()
#datafile['ow'] = merged['ow'].copy()
#datafile['kn, oe'] = merged['kn, oe'].copy()
#datafile['or'] = merged['or'].copy()
#datafile['ar'] = merged['ar'].copy()

datafile['Assessment Name'] = datafile['Assessment Name'].apply(lambda x: "Level " + str(x))
datafile['Assessment Window'] = datafile['Assessment Window'].apply(lambda x: "Attempt " + str(x))

datafile['Score'] = datafile.iloc[:,12:47].mean(axis=1)

now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_csv('spire-merged-concept-'+dt+'.csv', index=False, sep=',')


