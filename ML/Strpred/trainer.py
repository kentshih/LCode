#!/usr/bin/env python
from __future__ import division
from collections import defaultdict , Counter
import sys
from math import log
import tagger 

def decode(words,dictionary,model):
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

    Q = np.ones((len(self.tags), N)) * float('-Inf')
    backp = np.ones((len(self.tags), N), dtype=np.int16) * -1 #backpointers

    #print " ".join("%s/%s" % wordtag for wordtag in zip(words,tags)[1:-1])
    for i, word in enumerate(words[1:], 1):
        for tag in dictionary[word]:
            for prev in best[i-1]:
                features = get_features(word, tag, previous_tag)
                score = best[i-1][prev] + model[prev, tag] + model[tag, word] + feature_weights
                if score > best[i][tag]:
                    best[i][tag] = score
                    back[i][tag] = prev
        #print i, word, dictionary[word], best[i]
    #print best[len(words)-1][stopsym]
    mytags = backtrack(len(words)-1, stopsym)[:-1]
    #print " ".join("%s/%s" % wordtag for wordtag in mywordtags)
    return mytags

def ptest(devfile, feature_weights):
    correct = 0
    total = 0.0

    for i, (words, tags) in enumerate(tagger.readfile(trainfile)):
        prediction = tagger.decode

def trainer(trainfile, devfile, iterations=5):
    learning_rate = 1
    averaged_weights = Counter()
    print averaged_weights
    feature_weights = defaultdict(float)
    dictionary, model = tagger.mle(trainfile)
    print model
    for iteration in range(iterations):
        correct = 0
        total = 0.0
        update = 0

        for i, (words, tags) in enumerate(tagger.readfile(trainfile)):
            prediction = tagger.decode(words,dictionary,model)

            global_gold_features = get_global_features(words, tags)
            global_prediction_features = get_global_features(words, prediction)

            if tags != prediction:
                update += 1

            for fid, count in global_gold_features.items():
                feature_weights[fid] += learning_rate * count
            for fid, count in global_prediction_features.items():
                feature_weights[fid] -= learning_rate * count

            
        dev_err_rate, positive = test(dev_data, model)
        dev_err_rate_avg, positive_avg = tagger.test(devfile, totmodel)        
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

            correct += sum([1 for (predicted, gold) in zip(prediction, tags) if predicted == gold])
            total += len(tags)
        averaged_weights.update(feature_weights)
        print update

    feature_weights = averaged_weights

    print 1-correct / total



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
                    'WORD_LOWER+TAG_%s_%s' % (word_lower, tag),# word-tag combination (lowercase)
                    'UPPER_%s_%s' % (word[0].isupper(), tag),  # word starts with uppercase letter
                    'DASH_%s_%s' % ('-' in word, tag),         # word contains a dash
                    'PREFIX+TAG_%s_%s' % (prefix, tag),        # prefix and tag
                    'SUFFIX+TAG_%s_%s' % (suffix, tag),        # suffix and tag

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

    trainer(trainfile, devfile, 5)