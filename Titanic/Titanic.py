#!/usr/bin/env python
#-*- coding:utf-8 -*-
import csv
import os
from sklearn import svm

def readData(fileName):
    result = {}
    with open(fileName,'rb') as f:
        rows = csv.reader(f)
        for row in rows:
            if result.has_key('attr_list'):
                for i in range(len(result['attr_list'])):
                    key = result['attr_list'][i]
                    if not result.has_key(key):
                        result[key] = []
                    result[key].append(row[i])
            else:
                result['attr_list'] = row
    return result

def main():
    filename = 'train.csv'

    print readData(filename)

if __name__ == '__main__':
    main()