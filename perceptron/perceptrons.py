#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
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
    w = np.zeros(3)
    while check_error(w, dataset) is not None:
        x, s = check_error(w, dataset)
        w += s * x
    return w

def main():
    
    dataset = np.array([
    ((1, -0.4, 0.3), -1),
    ((1, -0.3, -0.1), -1),
    ((1, -0.2, 0.4), -1),
    ((1, -0.1, 0.1), -1),
    ((1, 0.9, -0.5), 1),
    ((1, 0.7, -0.9), 1),
    ((1, 0.8, 0.2), 1),
    ((1, 0.4, -0.6), 1)])
    w = pla(dataset)

    ps = [v[0] for v in dataset]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    #dataset前半後半已經分割好 直接畫就是

    ax1.scatter([v[1] for v in ps[:4]], [v[2] for v in ps[:4]], s=10, c='b', marker="o", label='O')
    ax1.scatter([v[1] for v in ps[4:]], [v[2] for v in ps[4:]], s=10, c='r', marker="x", label='X')
    l = np.linspace(-2,2)
    a,b = -w[1]/w[2], -w[0]/w[2]
    ax1.plot(l, a*l + b, 'b-')
    plt.legend(loc='upper left');
    plt.show()

if __name__ == '__main__':
    dictdata = {}
    f = open('income.test.txt','r')
    z = f.readline()
    x = []
    w = np.zeros(9)
    count = 1
    for line in f:
        frame = line.split(",")
        for element in frame:
            if element not in dictdata:
                dictdata[element] = count
                count += 1
            x.append(dictdata[element])
        print x[:9]
        x = []
        
    # x = np.array(f.readline())
    # y = np.array(f.readline())
    # x = f.readline()
    # print dictdata
    # print x
    # print x.T.dot(y)
    # for line in f:
    #  print line

