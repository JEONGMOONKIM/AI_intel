# -*- coding: utf-8 -*-
"""exam03_keras_xor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IyJOJnpX6-GyjllvsOJABQ93JeLHLE4w

###인공지능의 역사
[링크 텍스트](https://itwiki.kr/w/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5)
"""

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

training_data=np.array(
    [[0,0],[0,1],[1,0],[1,1]],'float32')
target_data=np.array([[0],[1],[1],[0]], 'float32')

"""###경사하강 알고리즘
[링크 텍스트](https://shuuki4.github.io/deep%20learning/2016/05/20/Gradient-Descent-Algorithm-Overview.html)
"""

model=Sequential()
model.add(Dense(32, input_dim=2,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='mse', optimizer='adam', metrics=['binary_accuracy'])
model.summary()

fit_hist = model.fit(training_data, target_data, epochs=500, verbose=1)

plt.plot(fit_hist.history['loss'])
plt.show()

inp=list(map(int, input('두 개의 논리값을 입력하시오.\r').split()))
qwe=np.array(inp)
print('입력 값')
qwe=qwe.reshape(1,2)
print('결과 값', model.predict(qwe)[0][0].round())