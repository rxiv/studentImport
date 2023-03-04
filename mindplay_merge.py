import pandas as pd
from datetime import datetime
from tkinter import filedialog as fd
import os.path
import numpy as np

append='set_1'
assessment = 'MOY'

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

datafile['Student First Name'] = merged['First_Name'].copy()
datafile['Student Last Name'] = merged['Last_Name'].copy()
datafile['Student Middle Initial'] = merged['Middle_Name'].copy()

datafile['Date Of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = merged['Grade_Level'].copy()

datafile['Student ID'] = merged['Student_Number'].copy()
datafile['State Student ID'] = merged['State_StudentNumber'].copy()

datafile['Score'] = merged['Risk Indicator'].copy()
datafile['Score Detail 1 Phoneme Association'] = merged['Phoneme Association'].copy()
datafile['Score Detail 2 Phoneme Segmentation'] = merged['Phoneme Segmentation'].copy()
datafile['Score Detail 3 Alphabet Knowledge'] = merged['Alphabet Knowledge'].copy()
datafile['Score Detail 4 Sound Symbol Recognition'] = merged['Sound Symbol Recognition'].copy()
# datafile['Score Detail 5 Encoding (Nonsense)'] = '' #merged['Encoding (Nonsense)'].copy()
# datafile['Score Detail 6 Encoding (Real)'] = '' #merged['Encoding (Nonsense)'].copy()
# datafile['Score Detail 7 Letter Discrimination'] = '' #merged['Letter Discrimination'].copy()
# datafile['Score Detail 8 Fluency (Words/Min)'] = '' #merged['Fluency (Words/Min)'].copy()

datafile['Assessment Group'] = 'Mind Play Dyslexia'
datafile['Assessment Name'] = 'Mindplay Risk Indicator'
datafile['Assessment Window'] = assessment

datafile['School Year'] = '2022-2023'

datafile['State Student ID'].replace('', np.nan, inplace=True)
datafile.dropna(subset=['State Student ID'], inplace=True)

datafile = datafile.replace('C', '1')
datafile = datafile.replace('A', '51')
datafile = datafile.replace('M', '101')
datafile = datafile.replace('E', '125')

datafile = datafile.replace('At Risk', '25')
datafile = datafile.replace('Some Risk', '50')
datafile = datafile.replace('No Risk', '100')

now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_csv('mindplay_Grade_K_merged-'+ append + '-' + dt+'.csv', sep=',', index=False)


sheet = pd.read_excel(filepath, header=0, sheet_name='1st')

sheet['lower_name'] = sheet['Student'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())

#merged = sheet.merge(sid, how='left', left_on=['First_Name', 'Last_Name'], right_on=['Last_Name','First_Name'])
merged = sheet.merge(sid, how='left', left_on=['lower_name'], right_on=['Name'])

datafile = pd.DataFrame()

datafile['Student First Name'] = merged['First_Name'].copy()
datafile['Student Last Name'] = merged['Last_Name'].copy()
datafile['Student Middle Initial'] = merged['Middle_Name'].copy()

datafile['Date Of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = merged['Grade_Level'].copy()

datafile['Student ID'] = merged['Student_Number'].copy()
datafile['State Student ID'] = merged['State_StudentNumber'].copy()

datafile['Score'] = merged['Risk Indicator'].copy()
# datafile['Score Detail 1 Phoneme Association'] = '' #merged['Phoneme Association'].copy()
# datafile['Score Detail 2 Phoneme Segmentation'] = '' #merged['Phoneme Segmentation'].copy()
datafile['Score Detail 3 Alphabet Knowledge'] = merged['Alphabet Knowledge'].copy()
datafile['Score Detail 4 Sound Symbol Recognition'] = merged['Sound Symbol Recognition'].copy()
datafile['Score Detail 5 Encoding (Nonsense)'] = merged['Encoding (Nonsense)'].copy()
datafile['Score Detail 6 Encoding (Real)'] = merged['Encoding (Nonsense)'].copy()
# datafile['Score Detail 7 Letter Discrimination'] = '' #merged['Letter Discrimination'].copy()
# datafile['Score Detail 8 Fluency (Words/Min)'] = '' #merged['Fluency (Words/Min)'].copy()

datafile['Assessment Group'] = 'Mind Play Dyslexia'
datafile['Assessment Name'] = 'Mindplay Risk Indicator'
datafile['Assessment Window'] = assessment

datafile['School Year'] = '2022-2023'

datafile['State Student ID'].replace('', np.nan, inplace=True)
datafile.dropna(subset=['State Student ID'], inplace=True)

datafile = datafile.replace('C', '1')
datafile = datafile.replace('A', '51')
datafile = datafile.replace('M', '101')
datafile = datafile.replace('E', '125')

datafile = datafile.replace('At Risk', '25')
datafile = datafile.replace('Some Risk', '50')
datafile = datafile.replace('No Risk', '100')

now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_csv('mindplay_Grade_1_merged-'+ append + '-' + dt+'.csv', sep=',', index=False)

sheet = pd.read_excel(filepath, header=0, sheet_name='2nd')

sheet['lower_name'] = sheet['Student'].apply(lambda x: str(x).replace(u"\u2019", "'").replace(u"\u2018", "'").lower())

#merged = sheet.merge(sid, how='left', left_on=['First_Name', 'Last_Name'], right_on=['Last_Name','First_Name'])
merged = sheet.merge(sid, how='left', left_on=['lower_name'], right_on=['Name'])

datafile = pd.DataFrame()

datafile['Student First Name'] = merged['First_Name'].copy()
datafile['Student Last Name'] = merged['Last_Name'].copy()
datafile['Student Middle Initial'] = merged['Middle_Name'].copy()

datafile['Date Of Birth'] = merged['DOB'].copy()
datafile['Student Grade Level'] = merged['Grade_Level'].copy()

datafile['Student ID'] = merged['Student_Number'].copy()
datafile['State Student ID'] = merged['State_StudentNumber'].copy()

datafile['Score'] = merged['Risk Indicator'].copy()
# datafile['Score Detail 1 Phoneme Association'] = '' #merged['Phoneme Association'].copy()
# datafile['Score Detail 2 Phoneme Segmentation'] = '' #merged['Phoneme Segmentation'].copy()
# datafile['Score Detail 3 Alphabet Knowledge'] = '' #merged['Alphabet Knowledge'].copy()
# datafile['Score Detail 4 Sound Symbol Recognition'] = '' #merged['Sound Symbol Recognition'].copy()
datafile['Score Detail 5 Encoding (Nonsense)'] = merged['Encoding (Nonsense)'].copy()
datafile['Score Detail 6 Encoding (Real)'] = merged['Encoding (Nonsense)'].copy()
datafile['Score Detail 7 Letter Discrimination'] = merged['Letter Discrimination'].copy()
datafile['Score Detail 8 Fluency (Words/Min)'] = merged['Fluency (Words/Min)'].copy()

datafile['Assessment Group'] = 'Mind Play Dyslexia'
datafile['Assessment Name'] = 'Mindplay Risk Indicator'
datafile['Assessment Window'] = assessment

datafile['School Year'] = '2022-2023'

datafile['State Student ID'].replace('', np.nan, inplace=True)
datafile.dropna(subset=['State Student ID'], inplace=True)

datafile = datafile.replace('C', '1')
datafile = datafile.replace('A', '51')
datafile = datafile.replace('M', '101')
datafile = datafile.replace('E', '125')

datafile = datafile.replace('At Risk', '25')
datafile = datafile.replace('Some Risk', '50')
datafile = datafile.replace('No Risk', '100')

now = datetime.now()
dt = now.strftime("%Y%m%d-%M%S")
datafile.to_csv('mindplay_Grade_2_merged-'+ append + '-' + dt+'.csv', sep=',', index=False)


