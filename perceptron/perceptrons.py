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

def pla1(file,w,dictdata,binfea,avgw):
    error = 0
    avgerror = 0
    f = open(file,'r')
    x = np.zeros(261)
    xx = np.zeros(261)
    count = 1
    lines = 1
    bias = 0
    sign = 0
    smart = 0
    avgcount = 1
    for line in f:
        frame = line.split(", ")
        elements = 0
        x = np.zeros(261)
        # print frame
        if frame[9] == "<=50K\n":
            sign = -1
        if frame[9] == ">50K\n":
            sign = 1
        frame[0] = "Y" +frame[0]
        frame[7] = "Hr"+frame[7]
        x.fill(-1)
        for element in frame:
            if element not in dictdata:
                dictdata[element] = count
                binfea[element] = 0
                count += 1
            
            if sign == 1:
                binfea[element] += 1
            else:
                binfea[element] -= 1
            
            # x[elements] = dictdata[element]
            x[dictdata[element]] = 1
            print "x: ", dictdata[element], "= 1"
            # if binfea[element] > 0:
            #     x[elements] = 1
            # if binfea[element] < 0:
            #     x[elements] = 0
            
            elements += 1
        print "---"
        print x
        # x[0] = dictdata[frame[0]]
        # x[7] = dictdata[frame[7]]
        # x[9] = 1
        # x[9] = np.linalg.norm(x)
        np.set_printoptions(formatter={'float': '{: 6.1f}'.format})
        # print "x: ",x , sign
        # print "avgw: ",avgw
        # print "xx: ",xx

        if lines == 100:
            avgw = w
        
        if int(np.sign(w.T.dot(x))) != sign: 
            error += 1
            w += sign * x
        if smart == 0:
            if int(np.sign(avgw.T.dot(x))) != sign:
                avgerror += 1
            xx += w
        if smart == 1:
            if int(np.sign(avgw.T.dot(x))) != sign:
                avgerror += 1
                xx += sign * x * avgcount
        
        if lines % 1000 == 0:
            if smart == 0:
                avgw = (avgw + (xx / avgcount) ) / 2
            if smart == 1:
                # print "before: ",avgw
                # print "avgcount", xx / avgcount
                avgw = avgw - (xx / avgcount)
                # print "after",avgw
            print  "error= %5s/%5s" % (error, lines), "rate: %.5f" % (float(error) / lines), "avg error= %5s/%5s" % (avgerror, lines), "rate:", float(avgerror) / lines
            avgcount = 0
            xx = np.zeros(261)
        avgcount += 1
        lines+= 1
        
    if smart == 0:
        avgw = (avgw + (xx / 1000) ) / 2
    if smart == 1:
        print avgcount
        avgw = avgw - xx / avgcount   
    print  "error= %5s/%5s" % (error, lines), "rate: %.5f" % (float(error) / lines), "avg error= %5s/%5s" % (avgerror, lines), "rate:", float(avgerror) / lines
    print "w: ",w
    # print "avgw: ",avgw
    # print ""
    return w,avgw

def mira(file,w,dictdata,binfea,avgw):
    error = 0
    avgerror = 0
    f = open(file,'r')
    x = np.zeros(261)
    xx = np.zeros(261)
    count = 1
    lines = 1
    bias = 0
    sign = 0
    smart = 1
    avgcount = 1
    dist = 0.0
    aggr = 1
    p = 0.2
    for line in f:
        frame = line.split(", ")
        elements = 0
        x = np.zeros(261)
        # print frame
        if frame[9] == "<=50K\n":
            sign = -1
        if frame[9] == ">50K\n":
            sign = 1
        frame[0] = "Y" +frame[0]
        frame[7] = "Hr"+frame[7]

        for element in frame:
            if element not in dictdata:
                dictdata[element] = count
                binfea[element] = 0
                count += 1
            
            if sign == 1:
                binfea[element] += 1
            else:
                binfea[element] -= 1
            x[dictdata[element]] = 1
            # if binfea[element] > 0:
            #     x[elements] = 1
            # if binfea[element] < 0:
            #     x[elements] = 0
            
            elements += 1


        # x[0] = dictdata[frame[0]]
        # x[7] = dictdata[frame[7]]
        # x[9] = 1
        # x[9] = np.linalg.norm(x)
        np.set_printoptions(formatter={'float': '{: 6.1f}'.format})
        # print "x: ",x , sign
        # print "avgw: ",avgw
        # print "xx: ",xx

        if lines == 100:
            avgw = w
        
        if int(np.sign(w.T.dot(x))) != sign:
            error += 1
            dist = np.linalg.norm(x)
            w += x * (sign - w.T.dot(x)) / dist*dist 
            # print "xb:",x
            # print "xa:",x * (sign - w.T.dot(x)) / dist*dist 
        if int(np.sign(w.T.dot(x))) == sign and aggr == 1 and w.T.dot(x) * sign <= p:
            # error += 1
            
            dist = np.linalg.norm(x)
            print dist
            w += x * (sign - w.T.dot(x)) / dist*dist 
        
        if smart == 0:
            if int(np.sign(avgw.T.dot(x))) != sign:
                avgerror += 1
            xx += w
        if smart == 1:
            if int(np.sign(avgw.T.dot(x))) != sign:
                avgerror += 1
                xx += sign * x * avgcount * (sign - avgw.T.dot(x)) / dist*dist
        
        if lines % 1000 == 0:
            if smart == 0:
                avgw = (avgw + (xx / avgcount) ) / 2
            if smart == 1:
                # print "before: ",avgw
                # print "avgcount", xx / avgcount
                avgw = avgw - (xx / avgcount)
                # print "after",avgw
            print  "mira error= %5s/%5s" % (error, lines), "rate: %.5f" % (float(error) / lines), "avg error= %5s/%5s" % (avgerror, lines), "rate:", float(avgerror) / lines
            avgcount = 0
            xx = np.zeros(261)
            
        avgcount += 1
        lines+= 1
        
    if smart == 0:
        avgw = (avgw + (xx / 1000) ) / 2
    if smart == 1:
        print avgcount
        avgw = avgw - xx / avgcount   
    print  "mira error= %5s/%5s" % (error, lines), "rate: %.5f" % (float(error) / lines), "avg error= %5s/%5s" % (avgerror, lines), "rate:", float(avgerror) / lines
    # print "w: ",w
    # print "avgw: ",avgw
    # print ""
    xx = np.zeros(261)
    return w,avgw

def main():
    # file = 'income.train.txt'
    # w = np.zeros(10)
    # avgw = np.zeros(10)
    # dictdata = {}
    # binfea = {}
    # for x in xrange(0,5):
    #     w,avgw = pla1(file,w,dictdata,binfea,avgw)
    # file = 'income.dev.txt'
    # print "dev"
    # w,avgw = pla1(file,w,dictdata,binfea,avgw)

    file = 'income.train.txt'
    w = np.zeros(10)
    avgw = np.zeros(10)
    dictdata = {}
    binfea = {}
    for x in xrange(0,5):
        w,avgw = mira(file,w,dictdata,binfea,avgw)
    file = 'income.dev.txt'
    # print "dev"
    # w,avgw = mira(file,w,dictdata,binfea,avgw)
    

if __name__ == '__main__':
    # main()
    file = 'income.train.txt'
    w = np.zeros(261)
    avgw = np.zeros(261)
    dictdata = {}
    binfea = {}
    w, avgw = pla1(file,w,dictdata,binfea,avgw)
    # w, avgw = mira(file,w,dictdata,binfea,avgw)
    # print binfea
    
        
    

