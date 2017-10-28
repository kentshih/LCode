#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import os
import math
import numpy as np
from random import random, randint
from collections import defaultdict
from matplotlib import pyplot
from sklearn import svm
import time

from perc import sign, perc

dim = 259
N = 5000

def map_data(filename, feature2index):
    data = [] # list of (vecx, y) pairs
    dimension = len(feature2index)
    for j, line in enumerate(open(filename)):
        line = line.strip()
        features = line.split(", ")
        feat_vec = np.zeros(dimension)
        # feat_vec = np.zeros(dimension+1)
        # feat_vec = np.zeros(dimension+5)
        for i, fv in enumerate(features[:-1]): # last one is target
            if (i, fv) in feature2index: # ignore unobserved features
                # feat_vec[feature2index[i, fv]] = 1
                # if i == 0:
                #     agebin = int(int(fv) * 0.2) ## binned features
                #     feat_vec[-1-agebin] = 1
                feat_vec[feature2index[i, fv]] = 1
        feat_vec[0] = 1 # bias
        # feat_vec[-1] = educationd[features[2]] ## adding features

        data.append((feat_vec, 1 if features[-1] == ">50K" else -1))

    return data

def preprosess(file):
    f = open(file,'r')
    x = np.zeros(260)
    dictdata = {}
    count = 0
    data = [[],[]]
    datas = []
    X = []
    Y = []

    for line in f:  ## set data
        frame = line.split(", ")
        x = np.zeros(260)
        if frame[9] == "<=50K\n":
            sign = -1
        if frame[9] == ">50K\n":
            sign = 1
        frame[0] = "Y" +frame[0]
        frame[7] = "Hr"+frame[7]
        x.fill(0)

        for element in frame[:9]:
            if element not in dictdata:
                dictdata[element] = count
                count += 1
            x[dictdata[element]] = 1
            X.append(x)
            Y.append(sign)
            datas.append((x,sign))
    return X,Y,datas

def train(train_data, dev_data, it=1, MIRA=False, check_freq=1000, aggressive=0.9, verbose=True):
    train_size = len(train_data)
    dimension = len(train_data[0][0])
    model = np.zeros(dimension)
    totmodel = np.zeros(dimension)
    best_err_rate = best_err_rate_avg = best_positive = best_positive_avg = 1
    t = time.time()
    error = 0

    for i in xrange(1, it+1):
        print "starting epoch", i
        for j, (vecx, y) in enumerate(train_data, 1):
            s = model.dot(vecx)
            if not MIRA: # perceptron
                if s * y <= 0:
                    error += 1
                    # model += y * vecx * (1. / (error+1.) + .5) ## variable learning rate
                    model += y * vecx
            else: # MIRA
                if s * y <= aggressive:
                    model += (y - s)  / vecx.dot(vecx) * vecx
            totmodel += model # stupid!
            if j % check_freq == 0:
                dev_err_rate, positive = test(dev_data, model)
                dev_err_rate_avg, positive_avg = test(dev_data, totmodel)        
                epoch_position = i-1 + j/train_size
                if dev_err_rate < best_err_rate:
                    best_err_rate = dev_err_rate
                    best_err_pos = epoch_position #(i, j)
                    best_positive = positive
                if dev_err_rate_avg < best_err_rate_avg:
                    best_err_rate_avg = dev_err_rate_avg
                    best_err_pos_avg = epoch_position #(i, j)
                    best_positive_avg = positive_avg
                    best_avg_model = totmodel

    print "training %d epochs costs %f seconds" % (it, time.time() - t)
    print "MIRA" if MIRA else "perceptron", aggressive if MIRA else "", \
        "unavg err: {:.2%} (+:{:.1%}) at epoch {:.2f}".format(best_err_rate, 
                                                              best_positive, 
                                                              best_err_pos), \
        "avg err: {:.2%} (+:{:.1%}) at epoch {:.2f}".format(best_err_rate_avg, 
                                                            best_positive_avg, 
                                                            best_err_pos_avg)

    return best_avg_model

def test(data, model):
    errors = sum(model.dot(vecx) * y <= 0 for vecx, y in data)
    positives = sum(model.dot(vecx) > 0 for vecx, _ in data) # stupid!
    return errors / len(data), positives / len(data)

def create_feature_map(train_file):

    column_values = defaultdict(set)
    for line in open(train_file):
        line = line.strip()
        features = line.split(", ")[:-1] # last field is target
        for i, fv in enumerate(features):
            column_values[i].add(fv)

    feature2index = {(-1, 0): 0} # bias
    for i, values in column_values.iteritems():
        for v in values:
            feature2index[i, v] = len(feature2index)

    dimension = len(feature2index)
    print "dimensionality: ", dimension
    return feature2index


def gen(C=1e10):
    # a, b, c = (random()-0.5) *10, (random()-0.5) *10, (random()+1) *5  # 0 for no bias
    # norm = math.sqrt(a*a+b*b)

    # w = np.array([a/norm, b/norm, c/norm])

    # prec=1e-2
    # data = [[], []]
    # datas = []
    # X = []
    # Y = []
    # while not all(len(d)>=20 for d in data):
    #     xy = np.array( [(random()-0.5) * 20, (random()-0.5) * 20, 1] )
    #     c = w.dot(xy)
    #     if c >= 1:
    #         i = 0 
    #     elif c <= -1:
    #         i = 1 
    #     else:
    #         i = 2
    #     if i < 2 and len(data[i]) <= 20:
    # ##         if random()<0.99:
    # ##             i = 1-i; c = -c
    #         data[i].append((xy[0], xy[1]))
    #         datas.append(((xy[0], xy[1]), sign(c)))
    #         X.append(xy[:-1])
    #         Y.append(sign(c))

    # markers = ["ro", "bs"]
    # for i, d in enumerate(data):
    #     ps = np.array(d).transpose()
    #     pyplot.plot(ps[0], ps[1], markers[i], ms=5)

    # x = np.linspace(-10, 10, 21)
    file = 'income.train.txt.5k'
    train_file, dev_file = "income.train.txt.5k", "income.dev.txt"
    X,Y,datas = preprosess(train_file)

    X2,Y2,datas2 = preprosess(dev_file)

    feature2index = create_feature_map("income.train.txt.5k")
    train_data = map_data(train_file, feature2index)
    dev_data = map_data(dev_file, feature2index)


    train_data_X = np.array(map(lambda x:x[0], train_data))
    train_data_Y = np.array(map(lambda x:x[1], train_data))
    dev_data_X = np.array(map(lambda x:x[0], dev_data))
    dev_data_Y = np.array(map(lambda x:x[1], dev_data))

    model = train(train_data, dev_data, it=5, MIRA=False, check_freq=1000, verbose=False)
    print "train_err {:.2%} (+:{:.1%})".format(*test(train_data, model))

    model = train(train_data, dev_data, it=5, MIRA=True, check_freq=1000, verbose=False, aggressive=.9)
    print "train_err {:.2%} (+:{:.1%})".format(*test(train_data, model))



#     pyplot.plot(x, (w[0]*x + w[2])/-w[1])
#     pyplot.plot(x, (w[0]*x + w[2] + 1)/-w[1])
#     pyplot.plot(x, (w[0]*x + w[2] - 1)/-w[1])

#    percw, _ = perc(datas, MIRA=False, aggressive=False)
    # e1, percw, avgw, errp, marginp = perc(datas, MIRA=False, aggressive=False, margin=0)
    # e2, miraw, _, erra, margina = perc(datas, MIRA=True, aggressive=False, margin=0.2)
    # e3, miraw2, _, erra2, margina2 = perc(datas, MIRA=True, aggressive=True, margin=0.5)
    # print e1, e2, e3
    # print percw
    # print avgw
    # print np.linalg.norm(percw)
    # print np.linalg.norm(avgw)
    # print marginp, margina
    # print errp, erra
    # print "perceptron avg: train_err {}".format(errp)

    # pyplot.plot(x, (percw[0]*x + percw[2])/-percw[1], "--", linewidth=0.2, label='perc') # PERC
    #pyplot.plot(x, (miraw[0]*x + miraw[2])/-miraw[1], "-.") # MIRA
    #pyplot.plot(x, (miraw2[0]*x + miraw2[2])/-miraw2[1], "-.", label='aggress. MIRA') # agg. MIRA


    # clf = svm.SVC(kernel='linear', C=C)
    # clf.fit(X, Y)
    # print "support vectors"
    # print clf.support_vectors_  
    # svmmodel = np.concatenate((clf.coef_[0], clf.intercept_))
    # print "model (primal)"
    # print svmmodel
    # print clf.dual_coef_

    # pyplot.plot(x, (svmmodel[0]*x + svmmodel[2])/-svmmodel[1], "k-", linewidth=2.0, label='svm') # SVM
    # pyplot.plot(x, (svmmodel[0]*x + 1 + svmmodel[2])/-svmmodel[1], "-.", linewidth=1.0)
    # pyplot.plot(x, (svmmodel[0]*x - 1 + svmmodel[2])/-svmmodel[1], "-.", linewidth=1.0)
    
    # for ps, alpha in zip(clf.support_vectors_, clf.dual_coef_[0]):
    #     if abs(alpha) == C: # violating support vectors: alpha == C
    #         pyplot.plot(ps[0], ps[1], "D", ms=10, markeredgecolor='g', markerfacecolor='None')
    #         pyplot.text(ps[0]+0.2, ps[1]-0.8, "%.1f" % (1-sign(alpha) * (svmmodel.dot([ps[0],ps[1],1]))), color='red') # show slack
    #     else: # good support vectors: 0 < alpha < C
    #         pyplot.plot(ps[0], ps[1], "o", ms=12, markeredgecolor='g', markerfacecolor='None')
    #         pyplot.text(ps[0]+0.2, ps[1]+0.2, "%.4f" % abs(alpha), color='gray') # show alpha

    # pyplot.title("SVM C=%s" % C)
    # pyplot.legend(loc=2)
    # pyplot.xlim(-10, 10)
    # pyplot.ylim(-10, 10)
    # pyplot.xticks(x)
    # pyplot.yticks(x)

if __name__ == "__main__":

    # C = float(sys.argv[1]) if len(sys.argv) > 1 else 0.01 
    # pyplot.ion()
    # while True:
    #     gen(C=C)
    #     pyplot.show()
    #     try:
    #         a = raw_input()
    #     except:
    #         break
    #     pyplot.clf()
    # file = 'income.train.txt.5k'
    # dataset = preprosess(file)

    
    

    C = float(sys.argv[1]) if len(sys.argv) > 1 else 0.01
    # pyplot.ion()
    gen(C=C)
    # pyplot.show()
    # a = raw_input()
    # pyplot.clf()
    # gen(C=C)
    # pyplot.show()
