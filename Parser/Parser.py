#!/usr/bin/env python

""": Description of """

import nltk


__author__ = 'McClain Marchman'
__email__ = 'mmmarchman@gmail.com'


class Parser(object):
    list_strings = None
    dict_top_words = None

    def __init__(self, list_strings):
        self.list_of_strings = list_strings


    def parse(self):
        stemmer = nltk.PorterStemmer()


