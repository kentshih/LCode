#!/usr/bin/env python

from __future__ import division

__author__ = "lhuang"

from collections import defaultdict
import sys
import tagger
from svector import svector

def train(trainfile, devfile, dictionary, epochs=5):
    model = svector()
    amodel = svector()
    trainset = list(tagger.readfile(trainfile))
    N = len(trainset)
    c = 0.
    whole = sum(map(lambda (x,y): len(x), trainset))
    for epoch in xrange(1, epochs+1):
        errors = errorwords = 0
        for j, (wordseq, tagseq) in enumerate(trainset):
            c += 1
            zseq = tagger.decode(wordseq, dictionary, model, gold=tagseq)

            if zseq != tagseq:
                errors += 1
                delta = svector()
                #print "update"
                tagseq = [startsym] + tagseq + [stopsym]
                wordseq = [startsym] + wordseq + [stopsym]
                zseq = [startsym] + zseq + [stopsym]
                for i, (w, t1, t2) in enumerate(zip(wordseq, tagseq, zseq)[1:], 1):
                    if t1 != t2:
                        delta[t1, w] += 1
                        delta[t2, w] -= 1
                        errorwords += 1
                    if t1 != t2 or tagseq[i-1] != zseq[i-1]:                    
                        delta[tagseq[i-1], t1] += 1
                        delta[zseq[i-1], t2] -= 1
                model += delta
                amodel += delta * c

        dev_err = tagger.test(devfile, dictionary, model)
        dev_avg_err = tagger.test(devfile, dictionary, model + amodel * (-1/c)) 

        print "epoch %d updates %d, |W|=%d, train_err %.2f%%, dev_err %.2f%%" % (epoch, errors, len(model), errorwords/whole*100, dev_err*100),
        print "avg_err %.2f%%" % (dev_avg_err*100)
            
if __name__ == "__main__":
    trainfile, devfile = sys.argv[1:3]
    startsym, stopsym = "<s>", "</s>"
    
    dictionary, _ = tagger.mle(trainfile)

    train(trainfile, devfile, dictionary)
