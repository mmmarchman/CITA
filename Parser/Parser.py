#!/usr/bin/env python

""" Creates a Parser object which takes in a list of strings and returns a frequency dist list"""

import nltk

__author__ = 'McClain Marchman'
__email__ = 'mmmarchman@gmail.com'


class Parser(object):
    list_strings = None
    word_list = []
    dict_top_words = None
    stop_words = []
    top_n = None

    # Takes in a list of strings and the number top results to return
    def __init__(self, list_strings, top_n):
        self.list_strings = list_strings
        self.top_n = top_n

        # Make a usable list of the words in exclusion_list.txt
        with open('exclusion_list.txt') as excl_file:
            for line in excl_file:
                self.stop_words.append(line.strip())

    def parse(self):
        # Creates a single list from list_strings
        self.word_list.append(' '.join(self.list_strings))

        # Divides the single list string into substrings representing a word
        self.word_list = nltk.sent_tokenize(str(self.word_list[0]))

        # Separates punctuation
        for sentence in self.word_list:
            self.word_list = nltk.wordpunct_tokenize(sentence.lower())

        # Remove all stop words in big_string
        self.word_list = [w for w in self.word_list if w not in self.stop_words]

        # print "List with stopwords removed: " + str(self.word_list)

        stemmer = nltk.PorterStemmer()

        # Stemmer is used to normalize adjective, adverbs, and verbs as well as making sure
        # that plural and singular words become the same
        self.word_list = [stemmer.stem(word) for word in self.word_list]

        # Removes the unicode formatting produced by the stemmer
        self.word_list = [str(word) for word in self.word_list]

        # Creates a frequency distribution based on words in self.word_list
        fdist = nltk.FreqDist(self.word_list)
        fdist = fdist.most_common(self.top_n)

        return fdist

