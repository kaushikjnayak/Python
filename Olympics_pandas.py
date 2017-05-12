__author__ = 'kaushik'

import pandas as pd

df = pd.read_csv('D:/KAUSHIK/kjn/workspace/Python/FILES/olympics.csv', index_col=0, skiprows=1)

#print (df)
for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='N':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)


#print (df)
names_ids = df.index.str.split('\s\(') # split the index by '('

#print (names_ids)
df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

#print (df)
#print (df['Gold'].idxmax())
#print (df.loc[df['Total'].idxmax()])


#print (df.iloc[:,4:5] - df.iloc[:,])
#print ( df.loc[df['Total'].idxmax])

print (df ['Gold'] * 3 + df ['Silver'] * 2)

def answer_four():
    df2 = df['Gold'] * 3 + df ['Silver'] * 2  + df['Bronze']
    df3 = pd.DataFrame(df2)
   # df3.columns = ['Points']
    return df3.iloc[:,0]

answer_four()


