#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    dictdata = {}
    result = None
    error = 0
    f = open('income.dev.txt','r')
    # z = f.readline()
    x = np.zeros(10)
    w = np.array ([-133.0,-284.0,-58.0,318.0,37.0,9.0,168.0,53.0,52.0])
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
        print "x: ",x
        print "w: ",w
        lines+= 1
        if int(np.sign(w.T.dot(x[:9]))) != x[9]:
            error += 1
        else:
            continue
        print  "error=%s/%s" % (error, lines) , "rate: ", float(error) / lines
        w += x[9] * x[:9]