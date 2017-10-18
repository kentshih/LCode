from __future__ import division
import csv
import numpy as np
# import matplotlib.pyplot as plt
import time
from operator import itemgetter
from pprint import pprint
# from collections import defaultdict

train = 'income.train_shuffled.txt'
dev = 'income.dev.txt'
MIN_AGE = 17
MAX_AGE = 90
MIN_HRS = 1
MAX_HRS = 99

def featurize(data):
	num_label = {0: 'age', 7: 'hours'}
	if data == train:
		with open(data, "r") as csvfile:
			reader = csv.reader(csvfile)
			c = 1 # feature count
			index_of_field = dict()
			seen = set()
			for i, column in enumerate(zip(*reader)):
				if i == 0: # age
					for num in range(MIN_AGE, MAX_AGE + 1):
						index_of_field['age', num] = c
						c += 1
				elif i == 7: # hours
					for num in range(MIN_HRS, MAX_HRS + 1):
						index_of_field['hours', num] = c
						c += 1
				elif i <= 8:
					for field in column:
						if field not in seen:
							seen.add(field)
							index_of_field[field] = c
							c += 1
	elif data == dev:
		index_of_field = iof

	x = [] # 2D nested lists of feature vectors, indexed as x[i][j]
	y = [] # 1D list of class labels, indexed as y[i]
	veclen = len(index_of_field)

	def wage_to_bin(field):
		if field == ' >50K':
			return 1
		elif field == ' <=50K':
			return -1
		else:
			assert False, 'invalid wage field encounted'

	with open(data, "r") as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			vec = [1] + [0] * veclen
			for k, field in enumerate(row):
				if k == 0 or k == 7: # age or hours
					j = index_of_field[num_label[k], int(field)]
					vec[j] = 1
				elif k <= 8:
					j = index_of_field[field]
					vec[j] = 1
				else: # class labels
					y.append(wage_to_bin(field))
			x.append(vec)	
	return x, y, index_of_field

xt, yt, iof = featurize(train)  # training data
assert len(xt) == len(yt)
len_t = len(xt)  # number of examples in training
xd, yd, _ = featurize(dev)  # dev data
assert len(xd) == len(yd)
len_d = len(xd)  # number of examples in dev


def dev_test(w):
	err = 0
	for i in range(len_d):
		if yd[i] * np.dot(xd[i], w) <= 0:
			err += 1
	return err / len_d


def train_n_mock_vanilla():
	t0 = time.time()
	w = np.zeros(1 + len(iof))
	eg = 0
	err_rate_calc, err_rate_plot = [], []
	NUM_EPOCHS = 5
	for epoch in range(NUM_EPOCHS):
		for i in range(len_t):
			eg += 1
			if yt[i] * np.dot(xt[i], w) <= 0: 
				w += yt[i] * np.array(xt[i])
			if epoch == 0 and eg % 200 == 0:
				err_rate_plot.append(dev_test(w))
			if eg % 1000 == 0:
				err_rate_calc.append((dev_test(w), (eg / len_t)))
	t1 = time.time()
	# plt.plot(np.arange(200, len_t * 1  + 1, 200) / len_t, err_rate_plot)
	# plt.show()
	print('vanilla perceptron min error rate of {} at {}'.format(*min(err_rate_calc)))
	return w,    t1 - t0


def train_n_mock_naive_avg():
	t0 = time.time()
	w = np.zeros(1 + len(iof))
	w_sum = np.zeros(1 + len(iof))
	eg = 0
	err_rate_calc, err_rate_plot = [], []
	NUM_EPOCHS = 5
	for epoch in range(NUM_EPOCHS):
		for i in range(len_t):
			eg += 1
			if yt[i] * np.dot(xt[i], w) <= 0: 
				w += yt[i] * np.array(xt[i])
			w_sum += w
			if epoch == 0 and eg % 200 == 0:
				err_rate_plot.append(dev_test(w_sum/eg))
			if eg % 1000 == 0:
				err_rate_calc.append((dev_test(w_sum/eg), (eg / len_t)))
	t1 = time.time()
	# plt.plot(np.arange(200, len_t * 1 + 1, 200) / len_t, err_rate_plot)
	# plt.show()
	print('naive averaged perceptron min error rate of {} at {}'.format(*min(err_rate_calc)))
	# print(eg)
	return w_sum / eg,    t1 - t0


def train_n_mock_smart_avg():
	t0 = time.time()
	w = np.zeros(1 + len(iof))
	w_add = np.zeros(1 + len(iof))
	eg = 0
	err_rate_calc, err_rate_plot = [], []
	NUM_EPOCHS = 5
	for epoch in range(NUM_EPOCHS):
		for i in range(len_t):
			eg += 1
			if yt[i] * np.dot(xt[i], w) <= 0: 
				delta = yt[i] * np.array(xt[i])
				w += delta
				w_add += (eg - 1) * delta
			if epoch == 0 and eg % 200 == 0:
				err_rate_plot.append(dev_test(w - w_add / eg)) # this line accounts for more time consumption
			if eg % 1000 == 0:
				err_rate_calc.append((dev_test(w - w_add / eg), (eg / len_t))) # this line accounts for more time consumption
	t1 = time.time()
	# plt.plot(np.arange(200, len_t * 1  + 1, 200) / len_t, err_rate_plot)
	# plt.show()
	print('smart averaged perceptron min error rate of {} at {}'.format(*min(err_rate_calc)))
	# print('smart averaged perceptron min error rate of {} at 13000'.format(err_rate_calc[12][0]))
	# print(eg, ud)
	return w - w_add / eg,    t1 - t0


w_vanilla, td_vanilla = train_n_mock_vanilla()
w_naive_avg, td_naive_avg = train_n_mock_naive_avg()
w_smart_avg, td_smart_avg = train_n_mock_smart_avg()
print('vanilla model norm = {}, naive avg model norm = {}, smart avg model norm = {}'.format(np.linalg.norm(w_vanilla), np.linalg.norm(w_naive_avg), np.linalg.norm(w_smart_avg)))
print('vanilla/avg model difference norm = {}'.format(np.linalg.norm(w_vanilla - w_smart_avg)))
print('naive/smart avg model difference norm = {}'.format(np.linalg.norm(w_naive_avg - w_smart_avg)))
print('vanilla took {}, naive avg took {}, smart avg took {}'.format(td_vanilla, td_naive_avg, td_smart_avg))

w_smart_avg_sorted = sorted(enumerate(w_smart_avg), key=itemgetter(1))
# pprint(w_smart_avg_sorted)
# print(iof)
foi = {v: k for k, v in iof.items()}
foi[0] = ' Bias'
print('\n***Top 5 negative features are:***')
for i, _ in w_smart_avg_sorted[0:5]:
	print(foi[i])
print('\n***Top 5 positive features are:***')
for i, _ in w_smart_avg_sorted[:-6:-1]:
	print(foi[i])

print('\n***Male score = {}'.format(w_smart_avg[124]))
print(' Female score = {}***'.format(w_smart_avg[125]))


# vanilla analysis: not good engough, missing BIAS on the negative side and MASTERS on the positive
w_vanilla_sorted = sorted(enumerate(w_vanilla), key=itemgetter(1))
print('\n***Top 5 vanilla negative features are:***')
for i, _ in w_vanilla_sorted[0:5]:
	print(foi[i])
print('\n***Top 5 vanilla positive features are:***')
for i, _ in w_vanilla_sorted[:-6:-1]:
	print(foi[i])


### experimentations




