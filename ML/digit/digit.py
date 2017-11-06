#-*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt, matplotlib.image as mpimg
from sklearn.model_selection import train_test_split
from sklearn import svm
# %matplotlib inline
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

labeled_images = pd.read_csv('train.csv')
#取前5000条数据（为了节省时间，只取小部分数据进行测试）
images = labeled_images.iloc[0:5000,1:]
labels = labeled_images.iloc[0:5000,:1]
#划分测试集与验证集
train_images, test_images,train_labels, test_labels = train_test_split(images, labels, train_size=0.8, random_state=0)


#取第一张图片
i=1
img=train_images.iloc[i].as_matrix()
img=img.reshape((28,28))
#打印第一张图片及其统计信息
plt.imshow(img,cmap='gray')
plt.title(train_labels.iloc[i,0])

