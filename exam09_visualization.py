# -*- coding: utf-8 -*-
"""exam09_visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o9kS3j8ZCpHmdXHTRCn6w_SVUFEaCc78
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

point = 100
#x = list(range(-50, 50))
#y = list(map(lambda x: 3 * x + 4, x)) #list로 x값을 주면 y는 lambda로 준다.
#y = list(map(lambda x: 3 * x * x+ 4, x))
#print(x)
#print(y)
#y = list(map(np.sin, x))
x = np.linspace(-4, 4, point)
y1 = np.sqrt(1 - np.square(np.abs(x)-1))
y2 = list(-2.5 * np.sqrt(1-np.sqrt(np.abs(x)/2)))
y = np.sin(x)
z = np.cos(x)
fig, axes = plt.subplots(1,2) # fig:밑바탕, axes:표, axis:축, (1,2): axes 2개(1행2열), #figsize=(10,10)
axes[0].plot(x, y1, '-d', markersize=1, color = 'mediumvioletred', linewidth=2) #-:실선, --:점선, -.:일점쇄선 #점의 형태 - d:다이아, ^:삼각형, *:별, o:동그라미, s:사각형 #선그래프에서는 점의 모양과 markersize는 안주는게 좋음.
axes[1].plot(x, y2, '-d', markersize=1, color = 'purple', linewidth=2) #axes의 개수가 2개이므로 인덱싱 해줘야함.
plt.axhline(color = 'black', linewidth=1)
plt.axvline(color = 'black', linewidth=1)
plt.show()

point = 100
x = np.linspace(-2, 2, point)
y = np.sin(x)
fig, axes = plt.subplots(figsize=(7,4)) # fig:밑바탕, axes:표, axis:축, (1,2): axes 2개(1행2열), #figsize=(10,10)
axes.scatter(x, y, marker='^', color = 'skyblue',s=1, linewidth=2) #-:실선, --:점선, -.:일점쇄선 #점의 형태 - d:다이아, ^:삼각형, *:별, o:동그라미, s:사각형 #선그래프에서는 점의 모양과 markersize는 안주는게 좋음.
plt.axhline(color = 'black', linewidth=1)
plt.axvline(color = 'black', linewidth=1)
plt.show()

labels='Frogs', 'Hogs', 'Logs'
size=[15,15,45]
explode=(0, 0.1, 0) #특정 부분을 강조해서 보여줄 때 사용
fig, axes=plt.subplots()
wedges, texts, autotexts=axes.pie(size, labels=labels, shadow=True, startangle=90, autopct='%1.1f%%', explode=explode) #size는 전체값의 백분율값으로 표시됨.(%)
wedges[1].set(hatch='///')
wedges[0].set_radius(1.1) #약간의 강조를 위해 사용. 과사용시 데이터 왜곡 발생.
wedges[1].set_theta1(90) #theta1:시작 각도
wedges[1].set_theta2(180) #끝각도. 시작각도, 끝각도 설정시 데이터 왜곡 발생. 주의 요함.
plt.show()

size=0.3
vals1=[40,35,25]
vals2=[11,29,12,23,12,13]

cmap=plt.get_cmap('Dark2')
outer_colors=cmap([0,4,12])
inner_colors=cmap([1,2,5,6,13,14])

fig, ax=plt.subplots()
ax.pie(vals1, radius=1, colors=outer_colors,
       labels=['male','female','pet'],
       autopct='%1.1f%%', pctdistance=0.83,
       wedgeprops={'width':size, 'edgecolor':'mediumvioletred', 'linewidth':5},
       startangle=0, counterclock=False) #원의 바깥쪽부터 0.3 #'edgecolor':'w','linewidth':5 테두리의 색상과 두께 설정.
ax.pie(vals2, radius=1-size, colors=inner_colors,
       autopct='%1.1f%%', pctdistance=0.8,
       wedgeprops={'width':size,'edgecolor':'mediumvioletred', 'linewidth':5},
       startangle=0, counterclock=False)

plt.show()

from matplotlib import colormaps #matplotlib cmap에서 볼 수 있음. 코드 복사해옴.
list(colormaps)

cmaps = {}

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))


def plot_color_gradients(category, cmap_list):
    # Create figure and adjust figure height to number of colormaps
    nrows = len(cmap_list)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows + 1, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh,
                        left=0.2, right=0.99)
    axs[0].set_title(f'{category} colormaps', fontsize=14)

    for ax, name in zip(axs, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=mpl.colormaps[name])
        ax.text(-0.01, 0.5, name, va='center', ha='right', fontsize=10,
                transform=ax.transAxes)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()

    # Save colormap list for later.
    cmaps[category] = cmap_list

plot_color_gradients('Perceptually Uniform Sequential',
                     ['viridis', 'plasma', 'inferno', 'magma', 'cividis'])

plot_color_gradients('Sequential',
                     ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                      'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                      'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'])

plot_color_gradients('Sequential (2)',
                     ['binary', 'gist_yarg', 'gist_gray', 'gray', 'bone',
                      'pink', 'spring', 'summer', 'autumn', 'winter', 'cool',
                      'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper'])

plot_color_gradients('Diverging',
                     ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu',
                      'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic'])

plot_color_gradients('Cyclic', ['twilight', 'twilight_shifted', 'hsv'])

plot_color_gradients('Qualitative',
                     ['Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2',
                      'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b',
                      'tab20c'])

plot_color_gradients('Miscellaneous',
                     ['flag', 'prism', 'ocean', 'gist_earth', 'terrain',
                      'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap',
                      'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet',
                      'turbo', 'nipy_spectral', 'gist_ncar'])

plt.show()

color={}
for name, hex_value in mpl.colors.cnames.items():
  print(name, hex_value)

plt.style.available

#plt.style.use('seaborn-v0_8')

n=10 #0~9
x=list(range(n))
y1=np.random.uniform(1,7,n) #1부터 7사이의 값을 랜덤하게 n개 만듬.
y2=np.random.uniform(1,7,n)

fig, ax=plt.subplots(figsize=(5,3))
ax.bar(x,y1, 0.8, facecolor='olive', alpha=0.7) #alpha: 투명도
ax.bar(x,-y2, 0.8, facecolor='#7777ff', alpha=0.7) #값이 겹쳐보이지 않도록 y2값을 뒤집어줌
ax.set_title('Bar plot', fontdict={'fontsize':15})
plt.show()

width=0.35 #x축의 간격이 1이기 때문에 폭을 1로 설정하면 값이 붙어보임.
fig, ax=plt.subplots()

ax.bar(list(map(lambda x:x-width/2, x)), y1, width)
ax.bar(list(map(lambda x:x+width/2, x)), y2, width)
plt.show()

n=5
ind=np.arange(n)
menMeans=(20,35,30,30,-2)
womenMeans=(25,32,34,20,-25)
menStd=(2,3,4,1,2)
womenStd=(3,5,2,3,3)
width=0.35
fig, ax=plt.subplots()
ax.bar(ind, menMeans, width, label='Men', yerr=menStd)
ax.bar(ind, womenMeans, width, label='Women', bottom=menMeans, yerr=womenStd)
ax.set_title('Scores by group and gender')
ax.legend()
plt.show()

import pandas as pd

df=pd.read_csv('./datasets/titanic.csv')
df

titanic_age=df[['Age','Survived']].dropna()
titanic_age

def age_band(num):
  for i in range(1,10):
    if num<10*i:
      return f'under{i*10}'
titanic_age['age_band']=titanic_age['Age'].apply(age_band)
titanic_age

titanic_age=titanic_age[['age_band','Survived']]
titanic_group_age=titanic_age.groupby('age_band')['Survived'].value_counts().sort_index() #age_band로 groupby한 것의 Survived의 값
print(titanic_group_age)
titanic_group_age=titanic_group_age.unstack().fillna(0) #unstack():값을 옆으로 펼침. fillna(0):없어서 NaN이 된 경우 0으로 채움.
titanic_group_age['Survival rate']=titanic_group_age[1]/(titanic_group_age[0]+titanic_group_age[1])*100
titanic_group_age

from matplotlib.ticker import FuncFormatter

fig, ax=plt.subplots(1,2,figsize=(12,5))
#bar1
ax[0].bar(titanic_group_age.index, titanic_group_age['Survival rate'], color='orange')
ax[0].set_title('Age Band & Survival rate')

with plt.xkcd(5): #with plt.xkcd(): 미역으로 출력
  color_map=['purple']*9
  color_map[0]=color_map[8]='#3caea3'

  ax[1].bar(titanic_group_age.index, titanic_group_age['Survival rate'], color= color_map, edgecolor='gray', linewidth=1.2, alpha=0.9)
  ax[1].set_title('Age Band & Survival rate', fontsize=15, fontweight='bold', position=(0.5,1.1))
  for i, rate in enumerate(titanic_group_age['Survival rate']):
    ax[1].annotate(f'{rate:.2f}%', xy=(i, rate+2), va='center', ha='center', fontsize=10, fontweight='bold', color='#383838')
    #f formatting #annotate:그림주석 #va:수직정렬, ha:수평정렬
  ax[1].yaxis.set_major_formatter(FuncFormatter(lambda y, _:f'{y:}%'))
  ax[1].set_xticklabels(titanic_group_age.index, rotation=40, size=10) #xticklabels:x축 눈금의 라벨 #rotation: 각도




plt.tight_layout()
plt.show()

from sklearn.datasets import load_iris
iris=load_iris()
iris_df=pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species']=[iris.target_names[i] for i in iris.target]
iris_df.info()
iris_df.head()

iris

a=[1,2,3,4,5]
b=[]
for i in a:
  b.append(i*1.8+32)
b

c=list(map(lambda x:x*1.8+32, a))
c

d=[i*1.8+32 for i in a]
da=[1,2,3,4,5]

cmap=plt.get_cmap('Reds')
inner_colors=cmap([0.75,0.5,0.35,0.25])

fig, ax=plt.subplots(1,2,figsize=(15,7))

ax[0].scatter(x='petal length (cm)', y='petal width (cm)', data=iris_df, color='gray', alpha=0.5)
ax[0].set_title('Iris')

ax[1].scatter(x='petal length (cm)', y='petal width (cm)',
              data=iris_df[iris_df['species']=='versicolor'],
              color='brown', label='versicolor', s=70, alpha=0.5)
ax[1].scatter(x='petal length (cm)', y='petal width (cm)',
              data=iris_df[iris_df['species']=='setosa'],
              color='olive', label='setosa', s=70, alpha=0.5)
ax[1].scatter(x='petal length (cm)', y='petal width (cm)',
              data=iris_df[iris_df['species']=='virginica'],
              color='navy', label='virginica', s=70, alpha=0.5)
ax[1].legend()

plt.show()

import seaborn as sns

sns.FacetGrid(iris_df, hue='species').map(plt.scatter,
                                          'petal length (cm)', 'petal width (cm)').add_legend()
fig=plt.gcf()
fig.set_size_inches(10,6)
plt.show()

#pairplot
sns.pairplot(iris_df, hue='species') #축의 값이 같은 경우, 확률밀도함수로 보여짐.
plt.show()

from plotly.express import scatter_3d

fig=scatter_3d(iris_df, x='sepal length (cm)', y='petal length (cm)',
               z='petal width (cm)', color='sepal width (cm)',
               symbol='species')
fig.show()

import warnings
warnings.filterwarnings(action='ignore')

#boxplot
plt.figure(figsize=(10,7))
plt.subplot(2,2,1)
sns.boxplot(x='species', y='petal length (cm)', data=iris_df) #boxplot: max,min,75%,50%,25%의 값 #확률과 분포 알 수 없음.
sns.swarmplot(x='species', y='petal length (cm)', data=iris_df, color='k', alpha=0.4) #swarmplot: 데이터 갯수 만큼의 분포를 알 수 있음.
plt.subplot(2,2,2)
sns.boxplot(x='species', y='petal width (cm)', data=iris_df)
sns.swarmplot(x='species', y='petal width (cm)', data=iris_df, color='k', alpha=0.4)
plt.subplot(2,2,3) #(2,2,3)==(223)
sns.boxplot(x='species', y='sepal length (cm)', data=iris_df)
sns.swarmplot(x='species', y='sepal length (cm)', data=iris_df, color='k', alpha=0.4)
plt.subplot(2,2,4)
sns.boxplot(x='species', y='sepal width (cm)', data=iris_df)
sns.swarmplot(x='species', y='sepal width (cm)', data=iris_df, color='k', alpha=0.4)

plt.show()

#violinplot
#violinplot은 swarmplot이 필요없음.
plt.figure(figsize=(10,7))
plt.subplot(2,2,1)
sns.violinplot(x='species', y='petal length (cm)', data=iris_df)
plt.subplot(2,2,2)
sns.violinplot(x='species', y='petal width (cm)', data=iris_df)
plt.subplot(2,2,3) #(2,2,3)==(223)
sns.violinplot(x='species', y='sepal length (cm)', data=iris_df)
plt.subplot(2,2,4)
sns.violinplot(x='species', y='sepal width (cm)', data=iris_df)

plt.show()

n_point=1000000 #시행 횟수. 횟수를 늘리면 확률밀도함수와 같은 모양을 띔.
n_bins=50 #구간을 50개로 나눔

#Generate two normal distributions
dist1=np.random.normal(0,2,n_point) #np.random.normal: 정규분포함수(Parameter:평균, 표준편차, 데이터 개수)
dist2=np.random.normal(0,10,n_point)

fig, axes=plt.subplots(1,2,sharey=True, tight_layout=True, figsize=(7,4))

axes[0].hist(dist1, bins=n_bins)
axes[1].hist(dist2, bins=n_bins) #표준편차가 크면 데이터가 넓게 퍼짐. 스케일이 큼.

plt.show()

fig, axes=plt.subplots(2,1,figsize=(5,15), tight_layout=True)
axes[0].hist2d(dist1, dist2, bins=40) #hist2d: 막대가 길수록 검은색 #가로축: dist1의 분포, 세로축: dist2의 분포
axes[0].axis('equal') #가로축과 세로축의 표의 길이를 동일하게. 스케일이 다르므로 축의 길이를 다르게 했을때 구형의 분포를 볼 수 있음. 자료를 비교하기에는 축의 길이를 동일하게 하는것이 보기 좋음.

axes[1].hist2d(dist1, dist2, bins=40)

plt.show()

fig=plt.figure(figsize=(16,10))
ax=fig.add_subplot(projection='3d')

hist, xedges, yedges= np.histogram2d(dist1, dist2, bins=n_bins,
                                     range=[[-7,7],[-30,30]])
xpos, ypos=np.meshgrid(xedges[:-1]+0.25, yedges[:-1]+0.25, indexing='ij')
xpos=xpos.ravel()
ypos=ypos.ravel()
zpos=0
dx=dy=0.3*np.ones_like(zpos)
dz=hist.ravel()

ax.bar3d(xpos, ypos, zpos,dx, dy, dz, zsort='average')
ax.view_init(elev=30, azim=45) #elev:높이, azim:각도
plt.show()

x=[0,1]
y=[0,1]

fig, axes=plt.subplots(2,3,figsize=(8,5))
axes[0,0].scatter(x='petal length (cm)', y='petal width (cm)',
              data=iris_df[iris_df['species']=='versicolor'],
              color='brown', label='versicolor', s=70, alpha=0.5)
axes[0,0].scatter(x='petal length (cm)', y='petal width (cm)',
              data=iris_df[iris_df['species']=='setosa'],
              color='olive', label='setosa', s=70, alpha=0.5)
axes[0,0].scatter(x='petal length (cm)', y='petal width (cm)',
              data=iris_df[iris_df['species']=='virginica'],
              color='navy', label='virginica', s=70, alpha=0.5)
axes[0,0].legend()
axes[1,2].plot(x,y)
plt.show()

fig=plt.figure(figsize=(8,5))
ax=fig.add_axes([0,0,1,1])#(0,0):시작좌표, 폭:1, 높이:1
ax.set_title('figure')
plt.show()

fig=plt.figure(figsize=(8,5))
ax=[None, None, None] #
ax[0]=fig.add_axes([0.1,0.1,0.4,0.8])
ax[1]=fig.add_axes([0.55,0.15,0.35,0.4])
ax[2]=fig.add_axes([0.65,0.6,0.2,0.3])
ax[0].scatter(x='petal length (cm)', y='petal width (cm)',
              data=iris_df[iris_df['species']=='versicolor'],
              color='brown', label='versicolor', s=70, alpha=0.5)
ax[0].scatter(x='petal length (cm)', y='petal width (cm)',
              data=iris_df[iris_df['species']=='setosa'],
              color='olive', label='setosa', s=70, alpha=0.5)
ax[0].scatter(x='petal length (cm)', y='petal width (cm)',
              data=iris_df[iris_df['species']=='virginica'],
              color='navy', label='virginica', s=70, alpha=0.5)
ax[0].legend()
for i in range(3):
  ax[i].set_title('ax[{}]'.format(i))
  ax[i].set_xticks([])
  ax[i].set_yticks([])

plt.show()

fig=plt.figure(figsize=(8,5))
ax=[]
#ax.append(plt.subplot2grid((2,3), (0,0))) #subplot2grid: 특정 자리의 그래프만 출력 가능
ax.append(plt.subplot2grid((2,3), (0,1)))
#ax.append(plt.subplot2grid((2,3), (0,2)))
ax.append(plt.subplot2grid((2,3), (1,0)))
#ax.append(plt.subplot2grid((2,3), (1,1)))
ax.append(plt.subplot2grid((2,3), (1,2)))
plt.show()

fig=plt.figure(figsize=(8,5))
ax=[]
ax.append(plt.subplot2grid((3,4),(0,0), colspan=2, rowspan=2))
ax.append(plt.subplot2grid((3,4),(0,2)))
ax.append(plt.subplot2grid((3,4),(0,3), rowspan=3))
ax.append(plt.subplot2grid((3,4),(1,2)))
ax.append(plt.subplot2grid((3,4),(2,0), colspan=3))

for i in range(5):
  ax[i].set_title('ax[{}]'.format(i))
  ax[i].set_xticks([])
  ax[i].set_yticks([])

fig.tight_layout()
plt.show()

fig=plt.figure(figsize=(8,5))
gs=fig.add_gridspec(3,4)
axes=[None for _ in range(5)]


axes[0]=fig.add_subplot(gs[0:2, 0:2])
axes[1]=fig.add_subplot(gs[0, 2])
axes[2]=fig.add_subplot(gs[:, -1])
axes[3]=fig.add_subplot(gs[1, 2])
axes[4]=fig.add_subplot(gs[2, :-1])

for i in range(5):
  axes[i].set_title('ax[{}]'.format(i))
  axes[i].set_xticks([])
  axes[i].set_yticks([])

plt.show()