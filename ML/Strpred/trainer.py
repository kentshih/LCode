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
    back = defaultdict(dict)

    N = len(words)
    M = len(model)
    tags = model

    Q = np.ones((len(tags), N)) * float('-Inf')
    backp = np.ones((len(tags), N), dtype=np.int16) * -1 #backpointers

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
        else:
            print "epoch {:2d}, updates {:d}, features {:d}, train_err {:.2%}, dev_err {:.2%}".format\
        (iteration+1, update, len(feature_weights), 1.0-correct / total, dev_err_rate)
        # feature_weights = averaged_weights
            
    if avgon == 1:
        print "best error rate average {:.2%}".format(best_err_rate_avg)
        print "avg perceptron time {:.2f} sec".format(time.time() - starttime)
    else:
        print "best error rate {:.2%}".format(best_err_rate)
        print "unavg perceptron time {:.2f} sec".format(time.time() - starttime)

    x = np.arange(0,180)
    y = np.sin(x * np.pi / 180.0)
    return x, y


def get_global_features(words, tags):
    """
    count how often each feature fired for the whole sentence
    :param words:
    :param tags:
    :return:
    """
    feature_counts = Counter()

    for i, (word, tag) in enumerate(zip(words, tags)):
        previous_tag = "<s>" if i == 0 else tags[i-1]
        feature_counts.update(get_features(word, tag, previous_tag))

    return feature_counts

def get_features(word, tag, previous_tag):
    """
    get all features that can be derived from the word and tags
    :param word:
    :param tag:
    :param previous_tag:
    :return:
    """
    word_lower = word.lower()
    prefix = word_lower[:3]
    suffix = word_lower[-3:]

    features = [
                    'TAG_%s' % (tag),                       # current tag
                    'TAG_BIGRAM_%s_%s' % (previous_tag, tag),  # tag bigrams
                    'WORD+TAG_%s_%s' % (word, tag),            # word-tag combination
                    # 'WORD_LOWER+TAG_%s_%s' % (word_lower, tag),# word-tag combination (lowercase)
                    # 'UPPER_%s_%s' % (word[0].isupper(), tag),  # word starts with uppercase letter
                    # 'DASH_%s_%s' % ('-' in word, tag),         # word contains a dash
                    # 'PREFIX+TAG_%s_%s' % (prefix, tag),        # prefix and tag
                    # 'SUFFIX+TAG_%s_%s' % (suffix, tag),        # suffix and tag

                    #########################
                    # ADD MOAAAAR FEATURES! #
                    #########################
                    # ('WORDSHAPE', self.shape(word), tag),
                    # 'WORD+TAG_BIGRAM_%s_%s_%s' % (word, tag, previous_tag),
                    # 'SUFFIX+2TAGS_%s_%s_%s' % (suffix, previous_tag, tag),
                    # 'PREFIX+2TAGS_%s_%s_%s' % (prefix, previous_tag, tag)
    ]
    return features

if __name__ == "__main__":
    trainfile, devfile = sys.argv[1:3]
    
    dictionary, model = tagger.mle(trainfile)

    print "train_err {0:.2%}".format(tagger.test(trainfile, dictionary, model))
    print "dev_err {0:.2%}".format(tagger.test(devfile, dictionary, model))
    
    # trainer(trainfile, devfile, 10, 0)
    avgon = 1
    x, y = trainer(trainfile, devfile, 10, avgon)

    x1 = np.arange(0,360,5)
    y1 = np.sin(x1 * np.pi / 180.0)

    x2 = x1
    y2 = np.cos(x2 * np.pi / 180.0)

    x3 = x1
    y3 = np.tan(x3 * np.pi / 180.0)

    plt.plot(x1,y1,lw=3)
    plt.plot(x2,y2,"ro")
    plt.plot(x3,y3,"y--",lw=5)

    plt.ylabel("y_label")
    plt.xlabel("x_label")
    plt.title("Title")

    plt.xlim(-30,390)
    plt.ylim(-5,5)

    plt.show()
    