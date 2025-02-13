import pandas as pd
import os
#Df = pd.read_csv(os.path.join("e:/", "Downloads", "CSV_FILES", "student_data.csv"))
#di=pd.read_csv(home//rgukt123//Downloads//CSV_FILES//student_data.csv)
'''absolute_path = os.path.abspath(os.path.dirname('student_data.csv'))
d=pd.read_csv(absolute_path + '/student_data.csv')'''

os.chdir("/home/rgukt123/CSV_FILES")
d = pd.read_csv("student_data.csv")
df=pd.DataFrame(d)
#print(df)
#print(df.head(4))
#print(df.tail(4))
#print(df.describe())
#print(df.shape)
#print(df[0:4:1])
#print(df[0:10:2])
#print(df['school'])
#print(df[['school','health']])#-->to columns
#print(df[['school','health']][0:10:2])#even records from with the given colums
#for rec in df.iterrows():
    #print(rec)
#print(df.loc[1])
#print(df.loc[19,['school','health']])
#print(df.loc[0:5])
#print(df.loc[0:5,['school','health']])
#print(df.loc[0:5,'school':'address'])
#print(df.iloc[2,0])#-->cell data
#print(df.iloc[0:5,0:3])
#print(df.iloc[0:5,2])
#print(df.iloc[[1,2,3]])
#print(df.iloc[[1,5,6,10]])
#print(df.iloc[:,[1,2,5]])
#print(df.iloc[0:3,[1,2,3]])
#print(df.sort_values('age'))
#print(df.sort_values('age')[0:3])
#print(df.sort_values('age',ascending=False)[0:3])
#print(df.sort_values(['age','school'])[0:3])
#print(df.sort_values(['age','school'],ascending=[0,1])[0:3])
df['total']=0
df['total']=5+df['age']
#print(df)
#df.drop(columns='total',inplace=True)
#print(df)
#print(df.duplicated())
df.dropna()
df.dropna(inplace=True)
df.fillna(10)
df['age'].fillna(10)
#print(df.loc[df['age']>20])
#print(df.loc[(df['age']>20) & (df['age']<22)])
#print(df.loc[df['school'].str.startswith('M')])
#print(df.loc[df['school'].str.endswith('M')])
df.loc[df['sex']=='M',['sex']]='Male'
#print(df)
os.chdir("/home/rgukt123/CSV_FILES")#to save
df.to_csv('studentnew.csv')#save as this file name

