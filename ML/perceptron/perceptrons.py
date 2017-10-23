#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
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

    xaxis = []
    yaxis1 = []
    yaxis2 = []
    yaxis3 = []
    yaxis4 = []

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

        if lines == 0:            
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

        # if smart == 0:
        #     avgw = xx / avgcount
        # if smart == 1:
        #     avgw = avgw - (xx / avgcount)
        if lines % 200 == 0:
            xaxis.append(float(lines))
            yaxis1.append(float(error) / lines)
            yaxis2.append(float(avgerror) / lines)
            bt,br,bta,bra,temp1,temp2 = pladev('income.dev.txt',w,dictdata,avgw,mira,p)
            yaxis3.append(temp1)
            yaxis4.append(temp2)

        if lines % 1000 == 0:
            if smart == 0:
                avgw = xx / avgcount
            if smart == 1:
                avgw = avgw - (xx / avgcount)
            # xaxis.append(lines)
            # yaxis1.append(float(error) / lines)
            # yaxis2.append(float(avgerror) / lines)
            
            print  "Iter %5.2f" % (float(lines)/ 1000),\
            "error rate: %.5f" % (float(error) / lines),\
            "avg error rate: %.5f" % (float(avgerror) / lines),
            bt,br,bta,bra,temp1,temp2 = pladev('income.dev.txt',w,dictdata,avgw,mira,p)
            # yaxis3.append(temp1)
            # yaxis4.append(temp2)
            if bestratea > bra:                    
                bestratea = bra                    
                besttimea = bta
            if bestrate > br:                
                bestrate = br             
                besttime = bt

            if lines % 5000 == 0:
                print "best"
                print "Iter %5.3f" % besttime,  "error rate: %.5f" % bestrate
                print "Iter %5.3f" % besttimea, "avg error rate: %.5f" % bestratea
                print ""

            
        avgcount += 1
        lines += 1
             
    print "best dev"
    print "Iter %5.3f" % besttime,  "error rate: %.5f" % bestrate
    print "Iter %5.3f" % besttimea, "avg error rate: %.5f" % bestratea
    # print "w: ",w

    plt.plot(xaxis,yaxis1,color = "blue",linewidth = 2.5,linestyle = "-",label = "mira")
    plt.plot(xaxis,yaxis2,color = "green",linewidth = 2.5,linestyle = "-",label = "avg mira")
    plt.plot(xaxis,yaxis3,color = "red",linewidth = 2.5,linestyle = "-",label = "dev mira")
    plt.plot(xaxis,yaxis4,color = "black",linewidth = 2.5,linestyle = "-",label = "dev avg mira")
    # plt.plot(xaxis,yaxis1,color = "blue",linewidth = 2.5,linestyle = "-",label = "perceptron")
    # plt.plot(xaxis,yaxis2,color = "green",linewidth = 2.5,linestyle = "-",label = "avg perceptron")
    # plt.plot(xaxis,yaxis3,color = "red",linewidth = 2.5,linestyle = "-",label = "dev perceptron")
    # plt.plot(xaxis,yaxis4,color = "black",linewidth = 2.5,linestyle = "-",label = "dev avg perceptron")
    plt.legend(loc='upper left')
    plt.xlim(0, 5000)
    plt.ylim(0.1, 0.4)
    plt.title('AMIRA 0.1')
    # plt.show()

    return w,avgw

def pladev(file,w,dictdata,avgw,mira,p):
    f = open(file,'r')
    smart = 1
    bestw = w
    bestrate = 90.0
    besttime = 0.0
    bestratea = 90.0
    besttimea = 0.0
    totalline = 0

    for line in f: 
        totalline += 1
    # print totalline
    xaxis = []
    yaxis3 = []
    yaxis4 = []

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

        if lines % 1000 == 0:            
            avgw = w                
        dist = np.linalg.norm(x)
        if w.T.dot(x) * sign <= 0:             
            error += 1            
            if bestrate > (float(error) / lines):                
                bestrate = (float(error) / lines)                
                besttime = (float(lines)/ 1000)            
            w += sign * x
            
            if mira >= 1:
                w += x * (sign - w.T.dot(x)) / float(dist*dist)    
        
        if w.T.dot(x) * sign > 0 and mira == 2 and w.T.dot(x) * sign <= p:
            w += x * (sign - w.T.dot(x)) / float(dist*dist)    
             
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

        if lines % 200 == 0:
            xaxis.append(float(lines))
            yaxis3.append(float(error) / lines)
            yaxis4.append(float(avgerror) / lines)
            
        avgcount += 1
        lines += 1

    if smart == 0:
        avgw = xx / avgcount
    if smart == 1:
        avgw = avgw - (xx / avgcount)

    print "dev error rate: %.5f" % (float(error) / lines),\
    "avg rate: %.5f" % (float(avgerror) / lines)

    return besttime,bestrate,besttimea,bestratea,(float(error) / lines),(float(avgerror) / lines)

def main():
    file = 'income.train.txt'
    w = np.zeros(260)
    avgw = np.zeros(260)
    dictdata = {}
    iteration = 5
    mira = 0
    p = 0.1
    w,avgw = pla1(file,w,dictdata,avgw,iteration,mira,p)

    # print w
    # print dictdata

    # temp1 = np.argmax(avgw)
    # temp2 = np.max(avgw)
    # for c in xrange(0,5):
    #     temp1 = np.argmax(avgw)
    #     temp2 = np.max(avgw)
    #     for a,b in dictdata.iteritems():
    #         if b == temp1:
    #             print a, temp2
    #             avgw[temp1] = 0
    # for c in xrange(0,5):
    #     temp1 = np.argmin(avgw)
    #     temp2 = np.min(avgw)
    #     for a,b in dictdata.iteritems():
    #         if b == temp1:
    #             print a, temp2
    #             avgw[temp1] = 0
    # rankd = 
    for a in dictdata:
        if 'Hr' in a:
            b = dictdata[a]
            print a, avgw[b]
        # if 'Black' in a:
        #     b = dictdata[a]
        #     print a, avgw[b]
        # if 'Asian-Pac-Islander' in a:
        #     b = dictdata[a]
        #     print a, avgw[b]
        # if 'Amer-Indian-Eskimo' in a:
        #     b = dictdata[a]
        #     print a, avgw[b]
        # if 'Other' in a:
        #     b = dictdata[a]
        #     print a, avgw[b]
        # if 'Sales' in a:
        #     b = dictdata[a]
        #     print a, avgw[b]
        # if 'Transport-moving' in a:
        #     b = dictdata[a]
        #     print a, avgw[b]
        # if 'Farming-fishing' in a:
        #     b = dictdata[a]
        #     print a, avgw[b] 
        # if 'Machine-op-inspct' in a:
        #     b = dictdata[a]
        #     print a, avgw[b]
        # if 'Tech-support' in a:
        #     b = dictdata[a]
        #     print a, avgw[b]
        # if 'Craft-repair' in a:
        #     b = dictdata[a]
        #     print a, avgw[b]
        # if 'Protective-serv' in a:
        #     b = dictdata[a]
        #     print a, avgw[b]
        # if 'Armed-Forces' in a:
        #     b = dictdata[a]
        #     print a, avgw[b]
        # if 'Priv-house-serv' in a:
        #     b = dictdata[a]
        #     print a, avgw[b]
        # if 'Masters' in a:
        #     b = dictdata[a]
        #     print a, avgw[b]
        # if 'Doctorate' in a:
        #     b = dictdata[a]
        #     print a, avgw[b]
        # if '12th' in a:
        #     b = dictdata[a]
        #     print a, avgw[b]   
    # rankd.

    

if __name__ == '__main__':
    main()
    
        
    

