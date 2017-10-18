# python 2.7.13
# coding : UTF-8
from __future__ import division
from __future__ import absolute_import
import numpy as np
import random
from io import open
from itertools import izip


def opendata(filename, makeeven=False):
    f = open(filename)
    lines = f.readlines()
    f.close()

    data = []
    for line in lines:
        elems = line.strip().strip(u",").split(u", ")
        data.append(elems)
    if makeeven:
        ndata = []
        for line in data:
            ndata.append(line)
            if line[-1] == u">50K":
                ndata.append(line)
                ndata.append(line)
        return ndata
    else:
        return data


def reorder(data):
    dim = len(data[0])
    negative = []
    positive = []
    for line in data:
        if line[dim-1] == u"<=50K":
            negative.append(line)
        else:
            positive.append(line)
    # for i in range(len(negative) - len(positive)):
    #     positive.append(positive[0])
    ro = positive + negative
    return ro


def shuffle(data):
    random.shuffle(data)
    return data


def standarize(tdata):
    newtdata = []
    for x in tdata:
        newx = np.array(x)
        stdx = (newx - newx.mean()/newx.std())
        newtdata.append(stdx)
    return newtdata


def bindata(data, edu, numer, replace, binned, combine, test=False):
    dim = len(data[0]) - 1
    if test:
        dim += 1
    num = len(data)

    # create dictionary mapping features to binaries
    list = []

    list.append({u'0': -1, u'1': -1, u'2': -1, u'3': -1, u'4': -1, u'5': -1, u'6': -1, u'7': -1, u'8': -1, u'9': -1, u'10': -1,\
                 u'11': -1, u'12': -1, u'13': -1, u'14': -1, u'15': -1, u'16': -1, u'17': -1, u'18': -1, u'19': -1, u'20': -1,\
                 u'21': -1, u'22': -1, u'23': -1, u'24': -1, u'25': -1, u'26': -1, u'27': -1, u'28': -1, u'29': -1, u'30': -1,\
                 u'31': -1, u'32': -1, u'33': -1, u'34': -1, u'35': -1, u'36': -1, u'37': -1, u'38': -1, u'39': -1, u'40': -1,\
                 u'41': 1, u'42': 1, u'43': 1, u'44': 1, u'45': 1, u'46': 1, u'47': 1, u'48': 1, u'49': 1, u'50': 1,\
                 u'51': 1, u'52': 1, u'53': 1, u'54': 1, u'55': 1, u'56': 1, u'57': 1, u'58': 1, u'59': 1, u'60': 1,\
                 u'61': 1, u'62': 1, u'63': 1, u'64': 1, u'65': 1, u'66': 1, u'67': 1, u'68': 1, u'69': 1, u'70': 1,\
                 u'71': 1, u'72': 1, u'73': 1, u'74': 1, u'75': 1, u'76': 1, u'77': 1, u'78': 1, u'79': 1, u'80': 1,\
                 u'81': 1, u'82': 1, u'83': 1, u'84': 1, u'85': 1, u'86': 1, u'87': 1, u'88': 1, u'89': 1, u'90': 1,\
                 u'91': 1, u'92': 1, u'93': 1, u'94': 1, u'95': 1, u'96': 1, u'97': 1, u'98': 1, u'99': 1, u'100': 1})

    list.append({u'Self-emp-not-inc': -1, u'Private': 1, u'State-gov': 1, u'Federal-gov': 1, u'Local-gov': -1, u'Self-emp-inc': 1,
     u'Without-pay': -1})

    list.append({u"Preschool": -1, u"1st-4th": -1, u"5th-6th": -1, u"7th-8th": -1, u"9th": -1, u"10th": -1, \
                u"11th": -1, u"12th": -1, u"HS-grad": -1, u"Prof-school": 1, u"Assoc-acdm": 1, u"Assoc-voc": 1, \
                u"Some-college": 1, u"Bachelors": 1, u"Masters": 1, u"Doctorate": 1})

    list.append({u'Married-civ-spouse': 1, u'Divorced': -1, u'Married-spouse-absent': 1, u'Never-married': -1, u'Married-AF-spouse': 1,
     u'Separated': -1, u'Widowed': -1})

    list.append({u'Exec-managerial': 1, u'Handlers-cleaners': -1, u'Prof-specialty': 1, u'Other-service': -1, u'Adm-clerical': -1,
     u'Sales': 1, u'Transport-moving': -1, u'Farming-fishing': 1, u'Machine-op-inspct': 1, u'Tech-support': 1,
     u'Craft-repair': -1, u'Protective-serv': -1, u'Armed-Forces': 1, u'Priv-house-serv': -1})

    list.append({u'White': 1, u'Black': 1, u'Asian-Pac-Islander': 1, u'Amer-Indian-Eskimo': -1, u'Other': -1})

    list.append({u'Male': -1, u'Female': 1})

    list.append({u'0': -1, u'1': -1, u'2': -1, u'3': -1, u'4': -1, u'5': -1, u'6': -1, u'7': -1, u'8': -1, u'9': -1, u'10': -1,\
                 u'11': -1, u'12': -1, u'13': -1, u'14': -1, u'15': -1, u'16': -1, u'17': -1, u'18': -1, u'19': -1, u'20': -1,\
                 u'21': -1, u'22': -1, u'23': -1, u'24': -1, u'25': -1, u'26': -1, u'27': -1, u'28': -1, u'29': -1, u'30': -1,\
                 u'31': -1, u'32': -1, u'33': -1, u'34': -1, u'35': -1, u'36': -1, u'37': -1, u'38': -1, u'39': -1, u'40': -1,\
                 u'41': -1, u'42': -1, u'43': -1, u'44': -1, u'45': -1, u'46': -1, u'47': -1, u'48': -1, u'49': -1, u'50': -1,\
                 u'51': 1, u'52': 1, u'53': 1, u'54': 1, u'55': 1, u'56': 1, u'57': 1, u'58': 1, u'59': 1, u'60': 1,\
                 u'61': 1, u'62': 1, u'63': 1, u'64': 1, u'65': 1, u'66': 1, u'67': 1, u'68': 1, u'69': 1, u'70': 1,\
                 u'71': 1, u'72': 1, u'73': 1, u'74': 1, u'75': 1, u'76': 1, u'77': 1, u'78': 1, u'79': 1, u'80': 1,\
                 u'81': 1, u'82': 1, u'83': 1, u'84': 1, u'85': 1, u'86': 1, u'87': 1, u'88': 1, u'89': 1, u'90': 1,\
                 u'91': 1, u'92': 1, u'93': 1, u'94': 1, u'95': 1, u'96': 1, u'97': 1, u'98': 1, u'99': 1, u'100': 1})

    list.append({u'United-States': 1, u'Cuba': -1, u'Jamaica': -1, u'India': -1, u'Mexico': 1, u'Puerto-Rico': -1, u'Honduras': -1,
     u'England': 1, u'Canada': 1, u'Germany': 1, u'Iran': -1, u'Philippines': -1, u'Poland': -1, u'Columbia': -1, u'Cambodia': -1,
     u'Thailand': -1, u'Ecuador': -1, u'Laos': -1, u'Taiwan': 1, u'Haiti': -1, u'Portugal': 1, u'Dominican-Republic': -1,
     u'France': 1, u'El-Salvador': -1, u'Guatemala': 1, u'Italy': 1, u'China': 1, u'South': -1, u'Japan': 1, u'Yugoslavia': -1,
     u'Peru': -1, u'Scotland': 1, u'Trinadad&Tobago': -1, u'Greece': 1, u'Nicaragua': -1, u'Vietnam': -1, u'Hong': 1, u'Ireland': 1,
     u'Outlying-US(Guam-USVI-etc)': -1, u'Hungary': 1, u'Holand-Netherlands': 1})

    if edu:
        edic = {u"Preschool": 1, u"1st-4th": 2, u"5th-6th": 3, u"7th-8th": 4, u"9th": 5, u"10th": 6, \
                u"11th": 7, u"12th": 8, u"HS-grad": 9, u"Prof-school": 10, u"Assoc-acdm": 11, u"Assoc-voc": 12, \
                u"Some-college": 13, u"Bachelors": 14, u"Masters": 15, u"Doctorate": 16}
        list.append(edic)

    # translates data from feature array to integer array
    #  xs matrix:
    #  |----------- number of samples -------------
    #  |
    #  9
    #  |
    #  |
    ndata = [[0 for i in xrange(num)] for j in xrange(dim)]
    ys = [1 for i in xrange(num)]
    for i in xrange(num):
        for j in xrange(dim):
            dic = list[j]
            ndata[j][i] = dic[data[i][j]]
        if not test and data[i][dim] == u"<=50K":
            ys[i] = -1
    if edu:
        edurow = []
        for i in xrange(num):
            edurow.append(edic[data[i][2]])
        if replace:
            ndata[2] = edurow
        else:
            ndata.append(edurow)
    if numer:
        numrow1 = []
        numrow2 = []
        for i in xrange(num):
            val1 = int(data[i][0])
            val2 = int(data[i][7])
            if binned:
                val1 = 10*round(val1/10)
                val2 = 10*round(val2/10)
            numrow1.append(val1)
            numrow2.append(val2)
        if replace:
            ndata[0] = numrow1
            ndata[7] = numrow2
        else:
            ndata.append(numrow1)
            ndata.append(numrow2)
    if combine:
        combrow1 = []
        combrow2 = []
        for i in xrange(num):
            combrow1.append(ndata[3][i] * ndata[6][i])
            combrow2.append(ndata[5][i] * ndata[8][i])
        else:
            ndata.append(combrow1)
            ndata.append(combrow2)


    return ndata, ys

def getx(tdata):
    # xs:
    # |----- 9 ------
    # |
    # num. of samples
    # |
    # |
    # .
    # .
    # .
    dnum = len(tdata[0])
    dim = len(tdata)
    xs = []
    for i in xrange(dnum):
        # get x_i
        x = [1]
        for j in xrange(dim):
            x.append(tdata[j][i])
        xs.append(x)
    return xs


def eval(w, xs, gt):
    dnum = len(xs)
    error = 0

    for (x, y) in izip(xs, gt):
        wx = np.dot(w, x)
        if y * wx <= 0:
            error += 1
    err = error/dnum
    # print("error rate =", err)
    return err


def MIRA(epoch, p=0., output=False, MIRA=True, reord=False, shuf=False,\
         edu=False, numer=False, replace=False, std=False, print1000=False,\
         reord_even=False, binned=False, combine=False, varlr=False):
    if reord_even:
        data = opendata(u'income.train.txt', makeeven=True)
    else:
        data = opendata(u'income.train.txt')
    dev = opendata(u'income.dev.txt')
    if reord:
        data = reorder(data)
    if shuf:
        data = shuffle(data)

    tdata, ys = bindata(data, edu, numer, replace, binned, combine)
    ddata, gt = bindata(dev, edu, numer, replace, binned, combine)
    if std:
        tdata = standarize(tdata)
        ddata = standarize(ddata)
    devxs = getx(ddata)
    dnum = len(tdata[0])
    dim = len(tdata)
    xs = getx(tdata)

    # initialize w
    w = []
    for i in xrange(dim+1):
        w.append(0.)
    w = np.array(w)
    # for average MIRA
    wa = []
    for i in xrange(dim + 1):
        wa.append(0.)
    wa = np.array(wa)

    counter = 0
    minerr = 1
    minaerr = 1
    bestn = 0
    bestan = 0
    upd = 0
    bestw = np.array(w)
    bestaw = np.array(w)

    for i in xrange(epoch):
        for (x, y) in izip(xs, ys):
            # evaluate w at each 1000 training
            if counter > 0 and counter % 1000 == 0:
                tempaw = w - wa/upd
                aerr = eval(tempaw, devxs, gt)
                err = eval(w, devxs, gt)
                if minerr > err:
                    bestn = counter
                    minerr = err
                    bestw = w
                if minaerr > aerr:
                    bestan = counter
                    minaerr = aerr
                    bestaw = tempaw
                if print1000:
                    print u"epoch", u'%03.3f' % (counter/dnum), u", error=", u'%03.3f' % (err*100),\
                          u"%, avg. error=", u'%03.3f' % (aerr*100), u"%"

            counter += 1
            # update w
            x = np.array(x)
            wx = np.dot(w, x)

            if varlr:
                lr = 1000 / (1000 + counter)
            else:
                lr = 1.
            if y * wx <= p:
                upd += 1
                if MIRA:
                    nor = np.linalg.norm(x)
                    temp = (y - wx)/(nor*nor)
                    w = w + lr * temp * x
                    wa = wa + lr * upd * temp * x
                else:
                    w = w + lr * y * x
                    wa = wa + lr * upd * y * x
    print u"MIRA=", MIRA, u", p=", p, u", (best error rate)=", u'%03.3f' % (minerr * 100), u"% in epoch", u'%03.3f' % (bestn / dnum)
    print u"MIRA=", MIRA, u", p=", p, u", (best avg. error rate)=", u'%03.3f' % (minaerr * 100), u"% in epoch", u'%03.3f' % (bestan / dnum)
    # finerr = eval(w, devxs, gt)
    # print("final error rate = ", finerr)

    if output:
        testd = opendata(u'income.test.txt')
        testdata, _tmp = bindata(testd, edu, numer, replace, binned, combine, test=True)
        if std:
            testdata = standarize(testdata)
        testxs = getx(testdata)
        return bestw, bestaw, testxs


def genprediction(w, xs, filename):
    f = open(u"income.test.txt")
    lines = f.readlines()
    f.close()

    wlines = []
    for (line, x) in izip(lines, xs):
        # update w
        x = np.array(x)
        wx = np.dot(w, x)
        if wx <= 0:
            unicode = line.strip() + u" <=50K\n"
        else:
            unicode = line.strip() + u" >50K\n"
        wlines.append(unicode)

    f = open(filename, u'w')
    f.writelines(wlines)
    f.close()

def countpositive(filename):
    data = opendata(filename)
    pos = 0
    neg = 0
    for line in data:
        if line[-1] == u">50K":
            pos += 1
        if line[-1] == u"<=50K":
            neg += 1
    rate = pos/len(data)
    print u"positive rate of " + filename + u" =", u'%03.3f' % (rate * 100), u"%, ", pos, u"/", pos+neg



# # 2.1
# MIRA(5)
# print
#
# # 2.2
# MIRA(5, p=0.1, print1000=True)
# MIRA(5, p=0.5, print1000=True)
# MIRA(5, p=0.9, print1000=True)
# print
#
# # 3.1
# MIRA(5, p=0.5)
# print
# MIRA(5, reord=True)
# MIRA(5, p=0.5, reord=True)
# MIRA(5, p=0.5, reord=True, reord_even=True)
# print
# MIRA(5, shuf=True)
# MIRA(5, p=0.5, shuf=True)
#
# # 3.2
# # (a)
# print u"replace numerical features"
# MIRA(5, p=0.5, numer=True, replace=True)
# # (b)
# print u"add numerical features"
# MIRA(5, p=0.5, numer=True)
# # (c)
# print u"add binned numerical features"
# MIRA(5, p=0.5, numer=True, binned=True)
# # (d)
# print u"add numerical feature \'educational-level\'"
# MIRA(5, p=0.5, edu=True)
# # (e)
# print u"add combined feature {marrage} x {gender} and {race} x {nationality}"
# MIRA(5, p=0.5, combine=True)
# # combination of (a) and (e)
# print u"combination of (a) and (e)"
# MIRA(5, p=0.5, numer=True, replace=True, combine=True)
# # combination of (d) and (e)
# print u"combination of (d) and (e)"
# MIRA(5, p=0.5, edu=True, combine=True)
# # combination of (a) and (d)
# print u"combination of (a) and (d)"
# MIRA(5, p=0.5, numer=True, replace=True, edu=True)
# # combination of (a), (d) and (e)
# print u"combination of (a), (d) and (e)"
# MIRA(5, p=0.5, numer=True, replace=True, edu=True, combine=True)
#
# # 3.3
# # (a)
# print u"variable learning rate 1000/(1000 + t)"
# MIRA(5, p=0.5, varlr=True)
# # (b)
# print u"standarize input"
# MIRA(5, p=0.5, std=True)
# # (a) and (b)
# print u"variable learning rate and standarize input"
# MIRA(5, p=0.5, std=True, varlr=True)
#
#
# # 3.4
# # combination of 3.2 best and 3.3 best
# MIRA(5, p=0.5, numer=True, replace=True, combine=True, varlr=True)
# # create prediction
# bestw, bestaw, test = MIRA(5, p=0.5, varlr=True, output=True)
# genprediction(bestaw, test, u'income.test.predicted')
# countpositive(u'income.train.txt')
# countpositive(u'income.dev.txt')
# countpositive(u'income.test.predict')
#
# bestw, bestaw, test = MIRA(5, p=0.5, varlr=True, output=True)
# genprediction(bestw, test, u'income.test.predicted.nonavg')
# countpositive(u'income.train.txt')
# countpositive(u'income.dev.txt')
# countpositive(u'income.test.predicted.nonavg')
