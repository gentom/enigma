#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import shuffle, randint, choice
from copy import copy


def shift(l, n):
    return l[n:] + l[:n]


class Scrumbler:
    def create(self, alphabet):
        self.transformation = copy(alphabet)
        shuffle(self.transformation)
        return

    def passthrough(self, i):
        return self.transformation[i]

    def passthrough_rev(self, i):
        return self.transformation.index(i)

    def rotate(self):
        self.transformation = shift(self.transformation, 1)

    def setcog(self, a):
        self.transformation = a
