#!/usr/bin/env python
#-*- coding:utf-8 -*-
from __future__ import division
from collections import defaultdict , Counter
import sys
from math import log
import numpy as np
import tagger 
import time
import matplotlib.pyplot as plt

startsym, stopsym = "<s>", "</s>"

def decode(words,dictionary,model,feature_weights):
    def backtrack(i, tag):
        if i == 0:
            return []
        return backtrack(i-1, back[i][tag]) + [tag]

    words = [startsym] + words + [stopsym]

    best = defaultdict(lambda: defaultdict(lambda: float("-inf")))
    best[0][startsym] = 1
    # best[1][startsym] = 1
    back = defaultdict(dict)
    feature_weight = 0
    tags = model
    # print words
    #print " ".join("%s/%s" % wordtag for wordtag in zip(words,tags)[1:-1])
    for i, word in enumerate(words[1:], 1):
        for tag in dictionary[word]:
            for prev in best[i-1]:
                features = get_features(word, tag, prev)
                # print word, features
                feature_weight = sum((feature_weights[x] for x in features))
                # print feature_weight
                # score = best[i-1][prev] + model[prev, tag] + model[tag, word] + feature_weight
                score = best[i-1][prev] + feature_weight
                if score > best[i][tag]:
                    best[i][tag] = score
                    back[i][tag] = prev
        #print i, word, dictionary[word], best[i]
    #print best[len(words)-1][stopsym]
    mytags = backtrack(len(words)-1, stopsym)[:-1]
    #print " ".join("%s/%s" % wordtag for wordtag in mywordtags)
    return mytags

def test(devfile, feature_weights, dictionary, model):
    correct = 0
    total = 0.0

    for i, (words, tags) in enumerate(tagger.readfile(devfile)):
        prediction = decode(words,dictionary,model,feature_weights)

        correct += sum([1 for (predicted, gold) in zip(prediction, tags) if predicted == gold])
        total += len(tags)
    return 1-correct / total


def trainer(trainfile, devfile, iterations, avgon):
    learning_rate = 1
    averaged_weights = Counter()
    best_err_rate = best_err_rate_avg = 1
    feature_weights = defaultdict(float)
    feature_weights_avg = defaultdict(float)
    c = 1
    unat = []
    at = []
    unv = []
    av = []
    # dictionary, model = tagger.mle(trainfile)
    starttime = time.time()
    twfreq = defaultdict(lambda : defaultdict(int))
    ttfreq = defaultdict(lambda : defaultdict(int)) 
    tagfreq = defaultdict(int)    
    dictionary = defaultdict(set)
    # print model
    for iteration in range(iterations):
        correct = 0
        total = 0.0
        update = 0
        fnum = 0

        for i, (words, tags) in enumerate(tagger.readfile(trainfile)):
            # print words
            last = startsym
            tagfreq[last] += 1
            for word, tag in zip(words, tags) + [(stopsym, stopsym)]:
                #if tag == "VBP": tag = "VB" # +1 smoothing
                twfreq[tag][word] += 1            
                ttfreq[last][tag] += 1
                dictionary[word].add(tag)
                tagfreq[tag] += 1
                last = tag 
                fnum +=1
            
            model = defaultdict(float)
            num_tags = len(tagfreq)
            for tag, freq in tagfreq.iteritems(): 
                logfreq = log(freq)
                for word, f in twfreq[tag].iteritems():
                    model[tag, word] = log(f) - logfreq 
                    fid = 'WORD+TAG_%s_%s' % (word, tag)
                    feature_weights[fid] = model[tag, word]
                    if avgon == 1:
                        feature_weights_avg[fid] = model[tag, word]
                logfreq2 = log(freq + num_tags)
                for t in tagfreq: # all tags
                    model[tag, t] = log(ttfreq[tag][t] + 1) - logfreq2 # +1 smoothing
                    fid = 'TAG_BIGRAM_%s_%s' % (tag, t)
                    feature_weights[fid] = model[tag, t]
                    if avgon == 1:
                        feature_weights_avg[fid] = model[tag, t]

            prediction = decode(words,dictionary,model,feature_weights)

            prediction2 = tagger.decode(words,dictionary,model)

            global_gold_features = get_global_features(words, tags)
            global_prediction_features = get_global_features(words, prediction)
            
            # print words
            # print "pred:",prediction
            # print "preM:",prediction2
            # print "tags:",tags

            if tags != prediction:
                update += 1

                for fid, count in global_gold_features.items():
                    feature_weights[fid] += learning_rate * count
                    if avgon == 1:
                        feature_weights_avg[fid] += learning_rate * count * c
                for fid, count in global_prediction_features.items():
                    feature_weights[fid] -= learning_rate * count
                    if avgon == 1:
                        feature_weights_avg[fid] -= learning_rate * count * c
            c += 1
            # print fid, feature_weights[fid]
            correct += sum([1 for (predicted, gold) in zip(prediction, tags) if predicted == gold])
            total += len(tags)

        if avgon == 1:
            for k in feature_weights_avg:
                averaged_weights[k] = feature_weights[k] - feature_weights_avg[k] / c
        

            # feature_weights_avg[k] = feature_weights[k] - feature_weights_avg[k] / c
        dev_err_rate = test(devfile, feature_weights, dictionary, model)
        if avgon == 1:
            dev_err_rate_avg = test(devfile, averaged_weights, dictionary, model)     
        # dev_err_rate_avg = test(devfile, feature_weights_avg, dictionary, model) 
        # epoch_position = i-1 + j/train_size
        if dev_err_rate < best_err_rate:
            best_err_rate = dev_err_rate
            # best_err_pos = epoch_position #(i, j)
            # best_positive = positive
        if avgon == 1 and dev_err_rate_avg < best_err_rate_avg:
            best_err_rate_avg = dev_err_rate_avg
            # best_err_pos_avg = epoch_position #(i, j)
            # best_positive_avg = positive_avg
            # best_avg_model = totmodel


        if avgon == 1:
            averaged_weights.update(feature_weights)
        # print dictionary
        if avgon == 1:
            print "epoch {:2d}, updates {:d}, features {:d}, train_err {:.2%}, dev_err {:.2%}, avg_dev_err {:.2%}".format\
        (iteration+1, update, len(feature_weights), 1.0-correct / total, dev_err_rate, dev_err_rate_avg)
            av.append(dev_err_rate_avg)
            at.append(1.0-correct / total)
        else:
            print "epoch {:2d}, updates {:d}, features {:d}, train_err {:.2%}, dev_err {:.2%}".format\
        (iteration+1, update, len(feature_weights), 1.0-correct / total, dev_err_rate)
            unv.append(dev_err_rate)
            unat.append(1.0-correct / total)
        # feature_weights = averaged_weights
            
    if avgon == 1:
        print "best error rate average {:.2%}".format(best_err_rate_avg)
        print "avg perceptron time {:.2f} sec".format(time.time() - starttime)
    else:
        print "best error rate {:.2%}".format(best_err_rate)
        print "unavg perceptron time {:.2f} sec".format(time.time() - starttime)

    
    testfile = 'test.txt.lower.unk.unlabeled'
    if avgon == 1:
        gentester(testfile,words,dictionary,model,feature_weights)
        gendever(devfile,words,dictionary,model,feature_weights)

    if avgon == 1: 
        return at, av
    else:
        return unat, unv

def gentester(testfile,words,dictionary,model,feature_weights):
    # fread = open(testfile, 'r')
    fout = open('test.lower.unk.best', 'w+')
    for j, line in enumerate(open(testfile)):
        # wordtags = map(lambda x: x.rsplit("/", 1), line.split())
        line = line.strip()
        words = line.split(" ")
        # print words
        prediction = decode(words,dictionary,model,feature_weights)
        wstr = ""
        for i in xrange(len(prediction)):
            wstr += words[i] + "/" + prediction[i] + " "
        fout.write(wstr+"\n")
        # print wstr

def gendever(devfile,words,dictionary,model,feature_weights):
    # fread = open(testfile, 'r')
    fout = open('dev.lower.unk.best', 'w+')
    for i, (words, tags) in enumerate(tagger.readfile(devfile)):
        prediction = decode(words,dictionary,model,feature_weights)
        # wordtags = map(lambda x: x.rsplit("/", 1), line.split())
        # print line
        prediction = decode(words,dictionary,model,feature_weights)
        wstr = ""
        for i in xrange(len(prediction)):
            wstr += words[i] + "/" + prediction[i] + " "
        fout.write(wstr+"\n")
        # print wstr

def get_global_features(words, tags):
    feature_counts = Counter()

    for i, (word, tag) in enumerate(zip(words, tags)):
        pprevious_tag = "<s>" if i <= 1 else tags[i-2]
        previous_tag = "<s>" if i == 0 else tags[i-1]
        feature_counts.update(get_features(word, tag, previous_tag))

    return feature_counts

def get_features(word, tag, previous_tag):
    word_lower = word.lower()
    prefix = word_lower[:3]
    suffix = word_lower[-3:]

    features = [
                    'TAG_%s' % (tag),                       # current tag
                    'TAG_BIGRAM_%s_%s' % (previous_tag, tag),  # tag bigrams
                    # 'TAG_TRIGRAM_%s_%s_%s' % (pprevious_tag,previous_tag, tag),  # tag bigrams
                    'WORD+TAG_%s_%s' % (word, tag),            # word-tag combination
                    # 'WORD_LOWER+TAG_%s_%s' % (word_lower, tag),# word-tag combination (lowercase)
                    # 'UPPER_%s_%s' % (word[0].isupper(), tag),  # word starts with uppercase letter
                    # 'DASH_%s_%s' % ('-' in word, tag),         # word contains a dash
                    # 'PREFIX+TAG_%s_%s' % (prefix, tag),        # prefix and tag
                    'SUFFIX+TAG_%s_%s' % (suffix, tag),        # suffix and tag
                    # 'WORD+TAG_BIGRAM_%s_%s_%s' % (word, tag, previous_tag),
                    'SUFFIX+2TAGS_%s_%s_%s' % (suffix, previous_tag, tag),
                    # 'PREFIX+2TAGS_%s_%s_%s' % (prefix, previous_tag, tag)
    ]
    # print features
    return features

if __name__ == "__main__":
    trainfile, devfile = sys.argv[1:3]
    
    dictionary, model = tagger.mle(trainfile)

    print "train_err {0:.2%}".format(tagger.test(trainfile, dictionary, model))
    print "dev_err {0:.2%}".format(tagger.test(devfile, dictionary, model))
    
    ut, uv = trainer(trainfile, devfile, 10, 0)
    avgon = 1
    at, av= trainer(trainfile, devfile, 10, avgon)
    
    # print ut
    # print uv
    # print at
    # print av