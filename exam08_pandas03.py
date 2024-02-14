# -*- coding: utf-8 -*-
"""exam08_pandas03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AHrAXeAUfFtRL12hlVzxWIGrw_2cL51-
"""

import pandas as pd

df=pd.DataFrame({'ten':[10,20,30,40,50],
                 'one':[1,-2,-4,5,6]})
df

# for i in range(len(df)):
#   if df.iloc[i,1]<0:
#     df.iloc[i,1]=0
# df

def relu(value):
  if value<0: value=0
  return value

sr1=df.one.apply(relu)
sr1

sr1=df.ten.apply(lambda x: x*3-4) #lambda: 함수 이름을 만들지 않을 때 함수 선언 방법. 간단한 함수, 한 번 쓰고 버릴 경우 사용.
sr1

df1=pd.DataFrame({'a':['a0','a1','a2','a3'],
                  'b':['b0','b1','b2','b3'],
                  'c':['c0','c1','c2','c3']},
                 index=[0,1,2,3])
df1

df2=pd.DataFrame({'a':['a2','a3','a4','a5'],
                  'b':['b2','b3','b4','b5'],
                  'c':['c2','c3','c4','c5'],
                  'd':['d2','d3','d4','d5']},
                 index=[2,3,4,5])
df2

result1=pd.concat([df1, df2])
result1.reset_index(drop=True, inplace=True)
result1

# result1=pd.concat([df1, df2], ignore_index=True)
# result1

result2=pd.concat([df1, df2], axis='columns', join='inner') #outer join: 합집합, inner join: 교집합
result2

df=pd.read_csv('./datasets/titanic.csv')
df

df=df.loc[:, ['Age','Sex','Pclass','Fare','Survived']]
df.head()

print(df['Pclass'].unique())
print(df['Pclass'].value_counts())

grouped=df.groupby(['Pclass'])
print(grouped)

grouped_df={}
for key, group in grouped:
  print('key', key)
  print('length', len(group))
  grouped_df[key]=group
  print(group.head())

grouped_df.keys()

grouped_df[1]

average=grouped.mean() #그룹별 평균
average

min=grouped.min()
min

max=grouped.max()
max

grouped_two=df.groupby(['Pclass','Sex'])
for key, group in grouped_two:
  print('key', key)
  print('length', len(group))
  print(group.head())

grouped_two.mean()

group3f=grouped_two.get_group((3, 'female'))
group3f

dfg=grouped_two.mean()
print(type(dfg))

dfg.loc[(1,'male')] #다중인덱스일 경우 튜플로

dfg.loc[1]

#dfg.loc[('female')] #이중 인덱스 중 차순위 인덱스를 기준으로 인덱싱 하려면 .xs() 사용햐야함.

dfg.xs('female', level='Sex')

dfg.xs('male', level='Sex')

pdf1=pd.pivot_table(df,
                    index='Pclass',
                    columns='Sex',
                    values='Age',
                    aggfunc='mean')
pdf1
#pivot_table

pdf2=pd.pivot_table(df,
                    index='Pclass',
                    columns='Sex',
                    values='Age',
                    aggfunc=['mean','sum','std'])
pdf2

pdf3=pd.pivot_table(df,
                    index='Pclass',
                    columns='Sex',
                    values=['Survived'],
                    aggfunc='mean')
pdf3

pdf3=pd.pivot_table(df,
                    index=['Pclass','Sex'],
                    columns='Survived',
                    values=['Age','Fare'],
                    aggfunc=['mean', 'max'])
pdf3

print(pdf3.index)

print(pdf3.columns)

df_teenage=df.loc[(df.Age>=10) & (df.Age<20)] #&: 비트연산-> 논리연산 하면 안됨.
df_teenage.head(30)

df_teenage.info()

df_teenage.Survived.sum()

df_teenage.Survived.mean()

df.Survived.mean()

df_teenage=df.loc[df.Age<10]

df_teenage.Survived.mean()

df_adult=df.loc[df.Age>=60]

df_adult.Survived.mean()

df_adult=df.loc[df.Age>=60]

df_female_under_10=df.loc[(df.Age<10)&(df.Sex=='female')]
df_female_under_10.head(5)

df_female_under_10.Survived.mean()

titanic=pd.read_csv('./datasets/titanic.csv')
titanic.info()

isin_filter=titanic['SibSp'].isin([2,4,5])
isin_filter

df_isin=titanic[isin_filter]
df_isin

df_Sibsp245=titanic[(titanic.SibSp==2)|(titanic.SibSp==4)|(titanic.SibSp==5)]
df_Sibsp245

df_male_under_30=df.loc[(df.Age>=20)&(df.Age<30)&(df.Sex=='male')]

df_male_under_30.Survived.mean()

df_Sibsp136=titanic[(titanic.SibSp==1)|(titanic.SibSp==3)|(titanic.SibSp==6)]
df_Sibsp136