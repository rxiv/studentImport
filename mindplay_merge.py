import pandas as pd
from datetime import datetime
from tkinter import filedialog as fd
import os.path

append='set_1'

filepath='9_19_2022 All student Data.txt'
if not os.path.exists(filepath):
    filepath = fd.askopenfilename(title='District PS Data', initialdir='.', filetypes=(('TXT files','*.txt'),('All files','*.*')))
    if filepath == '': exit()

sid = pd.read_csv(filepath,delimiter='\t')
sid['Last_Name'] = sid['Last_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sid['First_Name'] = sid['First_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sid['Middle_Name'] = sid['Middle_Name'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())
sid['Name'] = sid['Last_Name'] + ', ' + sid['First_Name']

filepath= fd.askopenfilename(title='Student Data', initialdir='.', filetypes=(('xlsx files','*.xlsx'),('All files','*.*')))
if filepath == '': exit()

sheet = pd.read_excel(filepath, header=0, sheet_name='KDG')

sheet['lower_name'] = sheet['Student'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())

#merged = sheet.merge(sid, how='left', left_on=['First_Name', 'Last_Name'], right_on=['Last_Name','First_Name'])
merged = sheet.merge(sid, how='left', left_on=['lower_name'], right_on=['Name'])

datafile = pd.DataFrame()

datafile['First Name'] = merged['First_Name'].copy()
datafile['Last Name'] = merged['Last_Name'].copy()
datafile['Birth'] = merged['DOB'].copy()
datafile['Grade'] = merged['Grade_Level'].copy()

datafile['Phoneme Association'] = merged['Phoneme Association'].copy()
datafile['Phoneme Segmentation'] = merged['Phoneme Segmentation'].copy()
datafile['Alphabet Knowledge'] = merged['Alphabet Knowledge'].copy()
datafile['Sound Symbol Recognition'] = merged['Sound Symbol Recognition'].copy()
datafile['Risk Indicator'] = merged['Risk Indicator'].copy()
datafile['Student_Number'] = merged['Student_Number'].copy()
datafile['SSN'] = merged['State_StudentNumber'].copy()

datafile['Assessment Group'] = 'Mind Play Dyslexia'
datafile['Assessment Name'] = 'Mindplay Risk Indicator'
datafile['Year'] = '2022-2023'



now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_csv('mindplay_Grade_K_merged-'+ append + '-' + dt+'.txt', sep='\t', index=False)


sheet = pd.read_excel(filepath, header=0, sheet_name='1st')

sheet['lower_name'] = sheet['Student'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())

#merged = sheet.merge(sid, how='left', left_on=['First_Name', 'Last_Name'], right_on=['Last_Name','First_Name'])
merged = sheet.merge(sid, how='left', left_on=['lower_name'], right_on=['Name'])

datafile = pd.DataFrame()

datafile['First Name'] = merged['First_Name'].copy()
datafile['Last Name'] = merged['Last_Name'].copy()
datafile['Birth'] = merged['DOB'].copy()
datafile['Grade'] = merged['Grade_Level'].copy()

datafile['Student'] = merged['Student'].copy()
datafile['Alphabet Knowledge'] = merged['Alphabet Knowledge'].copy()
datafile['Sound Symbol Recognition'] = merged['Sound Symbol Recognition'].copy()
datafile['Encoding (Nonsense)'] = merged['Encoding (Nonsense)'].copy()
datafile['Encoding (Real)'] = merged['Encoding (Nonsense)'].copy()
datafile['Risk Indicator'] = merged['Risk Indicator'].copy()
datafile['Student_Number'] = merged['Student_Number'].copy()
datafile['SSN'] = merged['State_StudentNumber'].copy()

datafile['Assessment Group'] = 'Mind Play Dyslexia'
datafile['Assessment Name'] = 'Mindplay Risk Indicator'
datafile['Year'] = '2022-2023'

now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_csv('mindplay_Grade_1_merged-'+ append + '-' + dt+'.txt', sep='\t', index=False)

sheet = pd.read_excel(filepath, header=0, sheet_name='2nd')

sheet['lower_name'] = sheet['Student'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())

#merged = sheet.merge(sid, how='left', left_on=['First_Name', 'Last_Name'], right_on=['Last_Name','First_Name'])
merged = sheet.merge(sid, how='left', left_on=['lower_name'], right_on=['Name'])

datafile = pd.DataFrame()

datafile['First Name'] = merged['First_Name'].copy()
datafile['Last Name'] = merged['Last_Name'].copy()
datafile['Birth'] = merged['DOB'].copy()
datafile['Grade'] = merged['Grade_Level'].copy()

datafile['Student'] = merged['Student'].copy()
datafile['Encoding (Nonsense)'] = merged['Encoding (Nonsense)'].copy()
datafile['Encoding (Real)'] = merged['Encoding (Nonsense)'].copy()
datafile['Letter Discrimination'] = merged['Letter Discrimination'].copy()
datafile['Fluency (Words/Min)'] = merged['Fluency (Words/Min)'].copy()
datafile['Risk Indicator'] = merged['Risk Indicator'].copy()
datafile['Student_Number'] = merged['Student_Number'].copy()
datafile['SSN'] = merged['State_StudentNumber'].copy()

datafile['Assessment Group'] = 'Mind Play Dyslexia'
datafile['Assessment Name'] = 'Mindplay Risk Indicator'
datafile['Year'] = '2022-2023'

now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_csv('mindplay_Grade_2_merged-'+ append + '-' + dt+'.txt', sep='\t', index=False)