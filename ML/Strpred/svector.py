'''sparse vector based on defaultdict'''

__author__ = "lhuang"

from collections import defaultdict

class svector(defaultdict):

    def __init__(self):
        defaultdict.__init__(self, float)

    def __iadd__(self, other):
        for k, v in other.iteritems():
            self[k] += v
        return self

    def __add__(self, other):
        new = svector()
        for k, v in self.iteritems():
            new[k] = v
        for k, v in other.iteritems():
            new[k] += v
        return new

    def __mul__(self, c): # c is scalar
        new = svector()
        for k, v in self.iteritems():
            new[k] = v * c
        return new
