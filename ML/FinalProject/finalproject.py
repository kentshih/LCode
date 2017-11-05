#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import division
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
        # print "starting epoch", i
        for j, (vecx, y) in enumerate(train_data, 1):
            s = model.dot(vecx)
            # print error
            # time.sleep(0.01)
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

def test2(data, model):
    errors = sum(model.dot(vecx) * y >= 0 for vecx, y in data)
    # print "error",errors
    positives = sum(model.dot(vecx) < 0 for vecx, _ in data) # stupid!
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
# runSVM(0.01,'linear',train_data_X,train_data_Y,dev_data_X,dev_data_Y)
def runSVM(C,k,trainX,trainY,devX,devY):
    print "C = {}".format(C)
    pos = 0
    # clf = svm.SVC(kernel='linear', C=C)
    clf = svm.SVC(kernel='poly', degree=2, coef0=C)
    t1 = time.time()
    clf.fit(trainX, trainY)
    print "SVM time {:.5f}".format(time.time() - t1)
    print "support vector number {}".format( len(clf.dual_coef_[0]))
    pre = clf.predict(devX)
    tra = clf.predict(trainX)
    terror = 0
    for i,j in enumerate(tra):
        if trainY[i] != j:
            terror += 1
    print "SVM train error rate {:.2%}".format(terror / len(tra))
    serror = 0
    for i,j in enumerate(pre):
        if devY[i] != j:
            serror += 1
        if j == 1:
            pos += 1
    print "SVM dev error rate {:.2%}".format(serror / len(pre))
    # print "support vector number {}".format(clf.n_support_)
    # print clf.support_
    print "SVM positive example {:.2%}".format(pos / len(pre))
    return C, terror / len(tra), serror / len(pre)

def gdata(n,train_data_X,train_data_Y):
    rdataX = []
    rdataY = []
    i = 0
    p = 0
    n2 = 0
    while i < n:
        pick = randint(0, 4999)
        # print i,n,pick, p, n2, train_data_Y[pick]
        if train_data_Y[pick] == 1 and p == 0:
            rdataX.append(train_data_X[pick])
            rdataY.append(train_data_Y[pick])
            i+=1
            p = 1
        if train_data_Y[pick] == -1 and n2 == 0:
            rdataX.append(train_data_X[pick])
            rdataY.append(train_data_Y[pick])
            i+=1
            n2 = 1
        if p != 0 and n2 != 0:
            rdataX.append(train_data_X[pick])
            rdataY.append(train_data_Y[pick])
            i+=1
    return rdataX, rdataY

def pegasos(train_data,dev_data,lam,count,k,check):
    dim = len(train_data[0][0])
    # print train_data
    print "dim",dim
    w = np.zeros(dim)
    w.fill(1)
    wd = np.zeros(dim)
    totmodel = np.zeros(dim)
    train_size = len(train_data)
    rpick = np.zeros(len(train_data))
    si = 0
    best_err_rate = best_err_rate_avg = best_positive = best_err_pos = best_positive_avg = 1
    pick = randint(0,len(train_data)-1)
    np.random.shuffle(train_data)
    train_data_X = np.array(map(lambda x:x[0], train_data))
    train_data_Y = np.array(map(lambda x:x[1], train_data))
    t = time.time()
    error = 0
    for i in xrange(1, count+1):
        np.random.shuffle(train_data)
        error = 0
        for j, (vecx,y) in enumerate(train_data, 1):
            si = 1.0/(lam*t)
            wd = np.zeros(dim)
            if y * w.dot(vecx) < 1:
                w = (1.0-si*lam)* w + si*y * vecx
                error += 1
            else:
                w = (1-si*lam)* w
            if j % check == 0:
                dev_err_rate, positive = test2(dev_data, w)  
                # dev_err_rate = error / len(dev_data) 
                epoch_position = i-1 + j/train_size
                if dev_err_rate < best_err_rate:
                    best_err_rate = dev_err_rate
                    best_err_pos = epoch_position #(i, j)
                    best_positive = positive
        print "e",error
        print "training %d epochs costs %f seconds" % (i, time.time() - t)
        print "pegasos", \
        "err: {:.2%} (+:{:.1%}) at epoch {:.2f}".format(best_err_rate, 
                                                    best_positive, 
                                                    best_err_pos),
    print "train_err {:.2%} (+:{:.1%})".format(*test2(train_data, w))                                          
    return w



def gen(C=1e10):
    file = 'income.train.txt.5k'
    train_file, dev_file = "income.train.txt.5k", "income.dev.txt"
    # X,Y,datas = preprosess(train_file)

    # X2,Y2,datas2 = preprosess(dev_file)

    feature2index = create_feature_map(train_file)
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


    # pyplot.plot(x, (percw[0]*x + percw[2])/-percw[1], "--", linewidth=0.2, label='perc') # PERC
    #pyplot.plot(x, (miraw[0]*x + miraw[2])/-miraw[1], "-.") # MIRA
    #pyplot.plot(x, (miraw2[0]*x + miraw2[2])/-miraw2[1], "-.", label='aggress. MIRA') # agg. MIRA


    # clf = svm.SVC(kernel='linear', C=C)
    clf = svm.SVC(kernel='poly', degree=2, coef0=1)
    t1 = time.time()
    clf.fit(train_data_X, train_data_Y)
    print "SVM time {:.5f}".format(time.time() - t1)
    # print "support vectors"
    # print clf.support_vectors_  
    # svmmodel = np.concatenate((clf.coef_[0], clf.intercept_))
    print "model (primal)"
    # print svmmodel
    # print clf.dual_coef_
    pre = clf.predict(dev_data_X)
    tra = clf.predict(train_data_X)
    terror = 0
    for i,j in enumerate(tra):
        if train_data_Y[i] != j:
            terror += 1
    print "SVM train error rate {:.2%}".format(terror / len(tra))
    serror = 0
    for i,j in enumerate(pre):
        if dev_data_Y[i] != j:
            serror += 1
    print "SVM dev error rate {:.2%}".format(serror / len(pre))
    print "support vector number {}".format(clf.n_support_)
    print clf.support_
    ts = clf.support_[0]
    print len(train_data_X[0])
    tt = train_data_X[0]
    misclass = 0
    tamount = 0
    # print len(clf.coef_[0])
    viodata = []
    porn = []
    # for i,j in enumerate(train_data_X):
    #     # print i, "{:6.3f}".format(clf.coef_[0].dot(j) * train_data_Y[i]) , train_data_Y[i]
    #     viodata.append(abs(clf.coef_[0].dot(j) * train_data_Y[i]))
    #     porn.append(train_data_Y[i])
    #     if clf.coef_[0].dot(j) * train_data_Y[i] < C and clf.coef_[0].dot(j) * train_data_Y[i] >= 0:
    #         misclass += 1
    #         tamount = clf.coef_[0].dot(j) * train_data_Y[i]
    # print "miss {:d}".format(misclass)
    # print "total slack {:.5f}".format(tamount)
    # print "objective {:.5f}".format(1.0/2.0 * clf.coef_[0].dot(clf.coef_[0]) + C * tamount)

    pnum = 0
    nnum = 0
    f = open(train_file,'r')
    parray = []
    narray = []
    pslack = []
    nslack = []
    # while pnum < 5 or nnum < 5:
    #     tempvio = np.min(viodata)
    #     indexvio = np.argmin(viodata)
    #     if porn[indexvio] == 1:
    #         pnum+=1
    #         parray.append(indexvio)
    #         pslack.append(tempvio)
    #     if porn[indexvio] == -1:
    #         nnum+=1
    #         narray.append(indexvio)
    #         nslack.append(tempvio)
    #     viodata[indexvio] = 999
    # for i in xrange(5):
    #     k = parray[i]
    #     f = open(train_file,'r')
    #     for j, line in enumerate(f):
    #         if j == k:
    #             print "top {} positive slack {}".format(i+1,pslack[i])
    #             print line
    # for i in xrange(5):
    #     k = narray[i]
    #     f = open(train_file,'r')
    #     for j, line in enumerate(f):
    #         if j == k:
    #             print "top {} negativeslack {}".format(i+1,nslack[i])
    #             print line


    # print clf.dual_coef_[0][0]
    # print clf.support_[0]
    # print len(clf.dual_coef_[0])
    # print clf.intercept_
    xpl_1 = []
    ypl_1 = []
    ypl_2 = []
    
    # c1 , ty1, ty2 = runSVM(0.001,'poly',train_data_X,train_data_Y,dev_data_X,dev_data_Y)
    # ypl_1.append(ty1)
    # ypl_2.append(ty2)
    # xpl_1.append(c1)

    # c1 , ty1, ty2 = runSVM(0.01,'poly',train_data_X,train_data_Y,dev_data_X,dev_data_Y)
    # ypl_1.append(ty1)
    # ypl_2.append(ty2)
    # xpl_1.append(c1)
    # c1 , ty1, ty2 =runSVM(0.1,'poly',train_data_X,train_data_Y,dev_data_X,dev_data_Y)
    # ypl_1.append(ty1)
    # ypl_2.append(ty2)
    # xpl_1.append(c1)
    # c1 , ty1, ty2 =runSVM(1,'poly',train_data_X,train_data_Y,dev_data_X,dev_data_Y)
    # ypl_1.append(ty1)
    # ypl_2.append(ty2)
    # xpl_1.append(c1)
    # c1 , ty1, ty2 =runSVM(2,'poly',train_data_X,train_data_Y,dev_data_X,dev_data_Y)
    # ypl_1.append(ty1)
    # ypl_2.append(ty2)
    # xpl_1.append(c1)
    # c1 , ty1, ty2 =runSVM(5,'poly',train_data_X,train_data_Y,dev_data_X,dev_data_Y)
    # ypl_1.append(ty1)
    # ypl_2.append(ty2)
    # xpl_1.append(c1)
    # c1 , ty1, ty2 =runSVM(10,'poly',train_data_X,train_data_Y,dev_data_X,dev_data_Y)
    # ypl_1.append(ty1)
    # ypl_2.append(ty2)
    # xpl_1.append(c1)
    # c1 , ty1, ty2 =runSVM(20,'poly',train_data_X,train_data_Y,dev_data_X,dev_data_Y)
    # ypl_1.append(ty1)
    # ypl_2.append(ty2)
    # xpl_1.append(c1)
    # c1 , ty1, ty2 =runSVM(50,'poly',train_data_X,train_data_Y,dev_data_X,dev_data_Y)
    # ypl_1.append(ty1)
    # ypl_2.append(ty2)
    # xpl_1.append(c1)
    c1 , ty1, ty2 =runSVM(100,'poly',train_data_X,train_data_Y,dev_data_X,dev_data_Y)
    ypl_1.append(ty1)
    ypl_2.append(ty2)
    xpl_1.append(c1)
    # c1 , ty1, ty2 =runSVM(200,'poly',train_data_X,train_data_Y,dev_data_X,dev_data_Y)
    # ypl_1.append(ty1)
    # ypl_2.append(ty2)
    # xpl_1.append(c1)

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
    # print xpl_1
    # print ypl_1
    # print ypl_2
    # pyplot.title("SVM C=%s" % C)
    
    # pyplot.xlim(0, 200)
    # pyplot.ylim(0.1, 0.3)
    # pyplot.plot(xpl_1,ypl_1,"--", linewidth=2.0, label='Train') 
    # pyplot.plot(xpl_1,ypl_2,"k-", linewidth=2.0, label='Dev') 
    # pyplot.legend(loc=2)
    # pyplot.xlabel("C")
    # pyplot.ylabel("error rate")
    # pyplot.show()

    # x = np.linspace(-10, 10, 21)
    # pyplot.xticks(xpl_1)
    # pyplot.yticks(ypl_1)
    # print len(train_data_X[:5])
    # print train_data_Y[:5]
    # rdataX = []
    # rdataY = []
    # rdataX, rdataY = gdata(5,train_data_X,train_data_Y)
    # print "hiiiiii" ,rdataY
        
    # xpl_1 = []
    # rdataX = []
    # rdataY = []
    # rdataX, rdataY = gdata(5,train_data_X,train_data_Y)
    # clf = svm.SVC(kernel='linear', C=C)
    # t1 = time.time()
    # clf.fit(rdataX,rdataY)
    # xpl_1.append(1)
    # print time.time() - t1
    # ypl_1.append(time.time() - t1)

    # clf = svm.SVC(kernel='linear', C=C)
    # rdataX, rdataY = gdata(50,train_data_X,train_data_Y)
    # t1 = time.time()
    # clf.fit(rdataX,rdataY)
    # xpl_1.append(2)
    # print time.time() - t1
    # ypl_1.append(time.time() - t1)

    # clf = svm.SVC(kernel='linear', C=C)
    # rdataX, rdataY = gdata(500,train_data_X,train_data_Y)
    # t1 = time.time()
    # clf.fit(rdataX,rdataY)
    # xpl_1.append(3)
    # print time.time() - t1
    # ypl_1.append(time.time() - t1)

    # clf = svm.SVC(kernel='linear', C=C)
    # t1 = time.time()
    # clf.fit(train_data_X, train_data_Y)
    # xpl_1.append(4)
    # print time.time() - t1
    # ypl_1.append(time.time() - t1)
    
    # pyplot.xlim(0, 6)
    # pyplot.ylim(0, 7)
    # pyplot.plot(xpl_1,ypl_1, linewidth=2.0) 
    # pyplot.ylabel("running time")
    # pyplot.show()
    pegaw = pegasos(train_data,dev_data,1,5,5000,1000)
    print "train_err {:.2%} (+:{:.1%})".format(*test2(train_data, pegaw))
    clf = svm.SVC(kernel='linear', C=C)
    clf.fit(train_data_X, train_data_Y)
    print dev_data_X
    return clf

def predi(clf):
    filep = 'income.test.txt'
    train_file, dev_file = "income.train.txt.5k", "income.dev.txt"
    fout = open('income.test.predicted','w')

    feature2index = create_feature_map(train_file)
    train_data = map_data(train_file, feature2index)
    
    test_data = []
    dimension = len(feature2index)
    for j, line in enumerate(open(filep)):
        line = line.strip()
        features = line.split(", ")
        feat_vec = np.zeros(dimension)
        # feat_vec = np.zeros(dimension+1)
        # feat_vec = np.zeros(dimension+5)
        for i, fv in enumerate(features):
            if (i, fv) in feature2index: # ignore unobserved features
                # feat_vec[feature2index[i, fv]] = 1
                # if i == 0:
                #     agebin = int(int(fv) * 0.2) ## binned features
                #     feat_vec[-1-agebin] = 1
                feat_vec[feature2index[i, fv]] = 1
        feat_vec[0] = 1 # bias
        # feat_vec[-1] = educationd[features[2]] ## adding features
        pre = clf.predict([feat_vec])

        for k in features:
            fout.write(k)
            fout.write(", ")
        fout.seek(-2,2)
        if pre == 1:
            fout.write(" >50K\n")
        else:
            fout.write(" <=50K\n")
        
    dev_file = "income.test.predicted"
    dev_data = map_data(dev_file, feature2index)
    dev_data_X = np.array(map(lambda x:x[0], dev_data))
    dev_data_Y = np.array(map(lambda x:x[1], dev_data))
    final = clf.predict(dev_data_X)
    ferror = 0
    for i,j in enumerate(final):
        if dev_data_Y[i] != j:
            ferror += 1
    print "SVM test error rate {:.2%}".format(ferror / len(final))
    print "support vector number {}".format(clf.n_support_)





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
    pyplot.ion()
    hi = gen(C=C)
    predi(hi)
    pyplot.show()
    a = raw_input()
    pyplot.clf()
    # gen(C=C)
    pyplot.show()
    predi(hi)
