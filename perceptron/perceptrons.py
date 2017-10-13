#-*- coding: utf-8 -*-

# import matplotlib.pyplot as plt
import numpy as np
import time


def pla1(file,w,dictdata,avgw,iteration,mira,p):
    f = open(file,'r')
    smart = 1
    bestw = w
    bestrate = 90.0
    besttime = 0.0
    bestratea = 90.0
    besttimea = 0.0

    f = open(file,'r')
    error = 0
    avgerror = 0
    x = np.zeros(260)
    xx = np.zeros(260)
    count = 0 #diction num
    avgcount = 1
    lines = 1
    sign = 0
    for line in f:  ## set data
        
        frame = line.split(", ")
        x = np.zeros(260)
        if frame[9] == "<=50K\n":
            sign = -1
        if frame[9] == ">50K\n":
            sign = 1
        frame[0] = "Y" +frame[0]
        frame[7] = "Hr"+frame[7]
        x.fill(-1)

        for element in frame[:9]:
            if element not in dictdata:
                dictdata[element] = count
                count += 1
            x[dictdata[element]] = 1    

        if lines == 1000:            
            avgw = w                

        if w.T.dot(x) * sign <= 0:      #PLA
            error += 1            
            if bestrate > (float(error) / lines):                
                bestrate = (float(error) / lines)                
                besttime = (float(lines)/ 1000)            
            w += sign * x
            dist = np.linalg.norm(x)
            # print (sign - w.T.dot(x)),"/", dist*dist,"=", (sign - w.T.dot(x)) / float(dist*dist)
            # time.sleep(1)
            # print mira
            # time.sleep(1)
            if mira >= 1:
                w += x * (sign - w.T.dot(x)) / float(dist*dist)
        
        if w.T.dot(x) * sign > 0 and mira == 2 and w.T.dot(x) * sign <= p:
            w += x * (sign - w.T.dot(x)) / float(dist*dist)
             
        if smart == 0:    #naive avg
            if avgw.T.dot(x) * sign <= 0:                
                avgerror += 1
                avgw += sign * x                
                if bestratea > (float(avgerror) / lines):                    
                    bestratea = (float(avgerror) / lines)                    
                    besttimea = (float(lines)/ 1000)                            
            xx += avgw        
        
        if smart == 1:   #smart avg  
            if avgw.T.dot(x) * sign <= 0:                
                avgerror += 1 
                avgw += sign * x               
                xx += sign * x * avgcount   

                if bestratea > (float(avgerror) / lines):                    
                    bestratea = (float(avgerror) / lines)                    
                    besttimea = (float(lines) / 1000)

        if lines % 1000 == 0:
            if smart == 0:
                avgw = xx / avgcount
            if smart == 1:
                avgw = avgw - (xx / avgcount)

            print  "Iter %5.2f" % (float(lines)/ 1000),\
            "error rate: %.5f" % (float(error) / lines),\
            "avg error rate: %.5f" % (float(avgerror) / lines),
            bt,br,bta,bra = pladev('income.dev.txt',w,dictdata,avgw)
            if bestratea > bra:                    
                bestratea = bra                    
                besttimea = bta
            if bestrate > br:                
                bestrate = br             
                besttime = bt

            if lines % 5000 == 0:
                print ""

            
        avgcount += 1
        lines += 1
             
    print "best"
    print "Iter %5.3f" % besttime,  "error rate: %.5f" % bestrate
    print "Iter %5.3f" % besttimea, "avg error rate: %.5f" % bestratea
    # print "w: ",w

    return w,avgw

def pladev(file,w,dictdata,avgw):
    f = open(file,'r')
    smart = 0
    bestw = w
    bestrate = 90.0
    besttime = 0.0
    bestratea = 90.0
    besttimea = 0.0
    totalline = 0
    for line in f: 
        totalline += 1
    # print totalline

    f = open(file,'r')
    error = 0
    avgerror = 0
    x = np.zeros(260)
    xx = np.zeros(260)
    count = 0 #diction num
    avgcount = 1
    lines = 1
    sign = 0
    for line in f:  ## set data
        
        frame = line.split(", ")
        x = np.zeros(260)
        if frame[9] == "<=50K\n":
            sign = -1
        if frame[9] == ">50K\n":
            sign = 1
        frame[0] = "Y" +frame[0]
        frame[7] = "Hr"+frame[7]
        x.fill(-1)
        # print frame
        # time.sleep(1)
        for element in frame[:9]:
            if element not in dictdata:
                dictdata[element] = count
                count += 1
            x[dictdata[element]] = 1    

        if lines == 1000:            
            avgw = w                

        if w.T.dot(x) * sign <= 0:             
            error += 1            
            if bestrate > (float(error) / lines):                
                bestrate = (float(error) / lines)                
                besttime = (float(lines)/ 1000)            
            w += sign * x    
            
             
        if smart == 0:            
            if avgw.T.dot(x) * sign <= 0:                
                avgerror += 1
                avgw += sign * x                
                if bestratea > (float(avgerror) / lines):                    
                    bestratea = (float(avgerror) / lines)                    
                    besttimea = (float(lines)/ 1000)                            
            xx += avgw        
        
        if smart == 1:            
            if avgw.T.dot(x) * sign <= 0:                
                avgerror += 1 
                avgw += sign * x               
                xx += sign * x * avgcount   

                if bestratea > (float(avgerror) / lines):                    
                    bestratea = (float(avgerror) / lines)                    
                    besttimea = (float(lines) / 1000)

            
        avgcount += 1
        lines += 1

    if smart == 0:
        avgw = xx / avgcount
    if smart == 1:
        avgw = avgw - (xx / avgcount)

    print "dev error rate: %.5f" % (float(error) / lines),\
    "avg rate: %.5f" % (float(avgerror) / lines)

    return besttime,bestrate,besttimea,bestratea

def main():
    file = 'income.train.txt'
    w = np.zeros(260)
    avgw = np.zeros(260)
    dictdata = {}
    iteration = 5
    mira = 2
    p = 0.2
    w,avgw = pla1(file,w,dictdata,avgw,iteration,mira,p)

    print w

    

if __name__ == '__main__':
    main()
    
        
    

