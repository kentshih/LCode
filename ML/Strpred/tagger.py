#!/usr/bin/env python

from __future__ import division
from collections import defaultdict,Counter
import sys
from math import log
import time
import numpy as np
startsym, stopsym = "<s>", "</s>"

def readfile(filename):
    for line in open(filename):
        wordtags = map(lambda x: x.rsplit("/", 1), line.split())
        yield [w for w,t in wordtags], [t for w,t in wordtags] # (word_seq, tag_seq) pair
    
def mle(filename): # Max Likelihood Estimation of HMM
    twfreq = defaultdict(lambda : defaultdict(int))
    ttfreq = defaultdict(lambda : defaultdict(int)) 
    tagfreq = defaultdict(int)    
    dictionary = defaultdict(set)

    for words, tags in readfile(filename):
        last = startsym
        tagfreq[last] += 1
        for word, tag in zip(words, tags) + [(stopsym, stopsym)]:
            #if tag == "VBP": tag = "VB" # +1 smoothing
            twfreq[tag][word] += 1            
            ttfreq[last][tag] += 1
            dictionary[word].add(tag)
            tagfreq[tag] += 1
            last = tag            
    
    model = defaultdict(float)
    num_tags = len(tagfreq)
    for tag, freq in tagfreq.iteritems(): 
        logfreq = log(freq)
        for word, f in twfreq[tag].iteritems():
            model[tag, word] = log(f) - logfreq 
        logfreq2 = log(freq + num_tags)
        for t in tagfreq: # all tags
            model[tag, t] = log(ttfreq[tag][t] + 1) - logfreq2 # +1 smoothing


    # print dictionary
    # print model        
    return dictionary, model

def decode(words, dictionary, model):

    def backtrack(i, tag):
        if i == 0:
            return []
        return backtrack(i-1, back[i][tag]) + [tag]

    words = [startsym] + words + [stopsym]

    best = defaultdict(lambda: defaultdict(lambda: float("-inf")))
    best[0][startsym] = 1
    back = defaultdict(dict)

    # print " ".join("%s/%s" % wordtag for wordtag in zip(words,tags)[1:-1])
    for i, word in enumerate(words[1:], 1):
        for tag in dictionary[word]:
            for prev in best[i-1]:
                score = best[i-1][prev] + model[prev, tag] + model[tag, word]
                if score > best[i][tag]:
                    print word, tag, "? prev:",prev
                    print score
                    best[i][tag] = score
                    back[i][tag] = prev
        # print i, word, dictionary[word], best[i]
        # print i, word
    # print best[len(words)-1][stopsym]
    mytags = backtrack(len(words)-1, stopsym)[:-1]
    # print " ".join("%s/%s" % wordtag for wordtag in mywordtags)
    print "words ",words
    print "mytags",mytags

    return mytags

def test(filename, dictionary, model):    
    
    errors = tot = 0
    for words, tags in readfile(filename):
        # print words
        # print "anstags",tags
        mytags = decode(words, dictionary ,model)
        # print "mytags:",mytags
        errors += sum(t1!=t2 for (t1,t2) in zip(tags, mytags))
        tot += len(words) 
        
    return errors/tot

def map_data(words, data2w, model):
    dimension = len(model)
    count = 0
    feat_vec = np.zeros(dimension)
    for word in words:
        if word in data2w:
            feat_vec[feature2index[i]] = 1
        else:
            # data2w.add(word)
            data2w[word] = count
            count+=1
    return feat_vec

def get_global_features(self, words, tags):
    """
    count how often each feature fired for the whole sentence
    :param words:
    :param tags:
    :return:
    """
    feature_counts = Counter()

    for i, (word, tag) in enumerate(zip(words, tags)):
        previous_tag = "<s>" if i == 0 else tags[i-1]
        feature_counts.update(self.get_features(word, tag, previous_tag))

    return feature_counts

def get_features(self, word, tag, previous_tag):
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
                    'WORD_LOWER+TAG_%s_%s' % (word_lower, tag),# word-tag combination (lowercase)
                    'UPPER_%s_%s' % (word[0].isupper(), tag),  # word starts with uppercase letter
                    'DASH_%s_%s' % ('-' in word, tag),         # word contains a dash
                    'PREFIX+TAG_%s_%s' % (prefix, tag),        # prefix and tag
                    'SUFFIX+TAG_%s_%s' % (suffix, tag),        # suffix and tag

                    #########################
                    # ADD MOAAAAR FEATURES! #
                    #########################
                    ('WORDSHAPE', self.shape(word), tag),
                    'WORD+TAG_BIGRAM_%s_%s_%s' % (word, tag, previous_tag),
                    'SUFFIX+2TAGS_%s_%s_%s' % (suffix, previous_tag, tag),
                    'PREFIX+2TAGS_%s_%s_%s' % (prefix, previous_tag, tag)
    ]
    return features

def train(train_data, dev_data, it=1, MIRA=False, check_freq=1000, aggressive=0.9, verbose=True):
    dictionary, model2 = mle(train_data)
    data2w = defaultdict(int)
    train_size = 0
    for words, tags in readfile(train_data):

        train_size += len(words)
    print train_size ##3668
    dimension = len(dictionary)
    print dimension ## 252
    print dictionary
    print model2[('VB','DT')]
    model = np.zeros(dimension)
    totmodel = np.zeros(dimension)
    averaged_weights = Counter()
    correct = 0
    total = 0.0
    best_err_rate = best_err_rate_avg = best_positive = best_positive_avg = 1
    t = time.time()
    error = 0
    for i in xrange(1, it+1):
        print "starting epoch", i
        # for j, (vecx, y) in enumerate(train_data, 1):
        for j, (words, tags) in enumerate(readfile(train_data), 1):
            print j, words, tags
            mytags = decode(words, dictionary ,model2) ## z
            # for k in tags:
            vecx = map_data(words,data2w,model)
            vexy = 
            s = model.dot(vecx)
            if not MIRA: # perceptron
                if mytags != tags:
                    error += 1
                    # model += y * vecx * (1. / (error+1.) + .5) ## variable learning rate
                    model += vecx - 
            else: # MIRA
                if s * y <= aggressive:
                    model += (y - s)  / vecx.dot(vecx) * vecx
            totmodel += model # stupid!
            if j % check_freq == 0:
                dev_err_rate, positive = test(dev_data, model)
                dev_err_rate_avg, positive_avg = test(dev_data, totmodel)        
                epoch_position = i-1 + j/train_size
                if dev_err_rate < best_err_rate:
                    best_err_rate = dev_err_rate
                    best_err_pos = epoch_position #(i, j)
                    best_positive = positive
                if dev_err_rate_avg < best_err_rate_avg:
                    best_err_rate_avg = dev_err_rate_avg
                    best_err_pos_avg = epoch_position #(i, j)
                    best_positive_avg = positive_avg
                    best_avg_model = totmodel

    print "training %d epochs costs %f seconds" % (it, time.time() - t)
    print "MIRA" if MIRA else "perceptron", aggressive if MIRA else "", \
        "unavg err: {:.2%} (+:{:.1%}) at epoch {:.2f}".format(best_err_rate, 
                                                              best_positive, 
                                                              best_err_pos), \
        "avg err: {:.2%} (+:{:.1%}) at epoch {:.2f}".format(best_err_rate_avg, 
                                                            best_positive_avg, 
                                                            best_err_pos_avg)

    return best_avg_model
        
if __name__ == "__main__":
    trainfile, devfile = sys.argv[1:3]
    
    # dictionary, model = mle(trainfile)

    

    # print "train_err {0:.2%}".format(test(trainfile, dictionary, model))
    # print "dev_err {0:.2%}".format(test(devfile, dictionary, model))
    # for i in dictionary:
    #     print i
    model = train(trainfile, devfile, it=5, MIRA=False, check_freq=1000, verbose=False)
    # print "train_err {:.2%} (+:{:.1%})".format(*test(train_data, model))
