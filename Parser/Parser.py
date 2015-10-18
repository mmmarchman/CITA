#!/usr/bin/env python

""": Description of """

import nltk


__author__ = 'McClain Marchman'
__email__ = 'mmmarchman@gmail.com'


class Parser(object):
    list_strings = None
    word_list = []
    dict_top_words = None
    stop_words = []

    def __init__(self, list_strings):
        self.list_strings = list_strings

        # Make a usable list of the words in exclusion_list.txt
        with open('exclusion_list.txt') as file:
            for line in file:
                self.stop_words.append(line.strip())
        print self.stop_words

        # Creates a single list from list_strings
        self.word_list.append(' '.join(self.list_strings))
        #''.join(self.word_list)

        #self.word_list = nltk.wordpunct_tokenize(i for i in self.list_of_strings)
        self.word_list = nltk.sent_tokenize(str(self.word_list[0]))
        for sentence in self.word_list:
            self.word_list = nltk.word_tokenize(sentence)
        print self.word_list




        #self.parse()


    def parse(self):
        # Remove all stop words in big_string
        #self.word_list = [self.word_list for w in self.word_list if w not in self.stop_words]

        print self.word_list

        stemmer = nltk.PorterStemmer()
        fdist = nltk.FreqDist(self.word_list)
        print fdist
        print fdist.most_common(10)


list_string = ['Unable to get credit report/credit score', 'Fraud or scam', 'Credit monitoring or identity protection',
               'Taking out the loan or lease', 'Fraud or scam']
parse = Parser(list_string)





