#-*- coding: utf-8 -*-

# import matplotlib.pyplot as plt
import numpy as np

def check_error(w, dataset):
    result = None
    error = 0
    for x, s in dataset:
        x = np.array(x)
        if int(np.sign(w.T.dot(x))) != s:
            result =  x, s
            error += 1
    print  "error=%s/%s" % (error, len(dataset))
    return result

def pla(dataset):
    w = np.zeros(9)
    while check_error(w, dataset) is not None:
        x, s = check_error(w, dataset)
        w += s * x
    return w

def pla1(file,w,dictdata):
    error = 0
    f = open(file,'r')
    x = np.zeros(10)
    count = 1
    lines = 1
    for line in f:
        frame = line.split(",")
        elements = 0
        x = np.zeros(10)
        for element in frame:
            if element not in dictdata:
                dictdata[element] = count
                count += 1
            x[elements] = dictdata[element]
            if element == " <=50K\n":
                x[9] = 1
            if element == " >50K\n":
                x[9] = -1
            elements += 1
        # print "x: ",x
        # print "w: ",w
        lines+= 1
        if int(np.sign(w.T.dot(x[:9]))) != x[9]:
            error += 1
        else:
            continue
        
        w += x[9] * x[:9]
    print  "error=%s/%s" % (error, lines), "rate: ", float(error) / lines
    print "w: ",w
    return w

def mira(file,w,dictdata):
    error = 0
    f = open(file,'r')
    x = np.zeros(10)
    count = 1
    lines = 1
    dist = 0.0
    for line in f:
        frame = line.split(",")
        elements = 0
        x = np.zeros(10)
        for element in xrange(1,len(frame):
            if element not in dictdata:
                dictdata[element] = count
                count += 1
            x[elements] = dictdata[element]
            if element == " <=50K\n":
                x[9] = 1
            if element == " >50K\n":
                x[9] = -1
            elements += 1
        # print "x: ",x
        # print "w: ",w
        lines+= 1
        if int(np.sign(w.T.dot(x[:9]))) != x[9]:
            error += 1
        else:
            continue
        dist = np.linalg.norm(x)
        w = w + np.subtract(x[:9], w.T.dot(x[:9])) * (x[9] / dist*dist)
    print  "error=%s/%s" % (error, lines), "rate: ", float(error) / lines
    print "w: ",w
    return w

def main():
    file = 'income.train.txt'
    w = np.zeros(9)
    dictdata = {}
    for x in xrange(0,5):
        w = pla1(file,w,dictdata)
    file = 'income.dev.txt'
    w = pla1(file,w,dictdata)

    file = 'income.train.txt'
    w = np.zeros(9)
    dictdata = {}
    for x in xrange(0,5):
        w = mira(file,w,dictdata)
    file = 'income.dev.txt'
    w = mira(file,w,dictdata)

    

if __name__ == '__main__':
    main()
    
        
    

