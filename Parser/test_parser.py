#!/usr/bin/env python

""" Tests Parser.py"""

from Parser import Parser
import test_plotly


__author__ = 'McClain Marchman'
__email__ = 'mmmarchman@gmail.com'


list_string = ['Unable to get credit report/credit score', 'Fraud or scam', 'Credit monitoring or identity protection',
               'Taking out the loan or lease', 'Fraud or scam']
parse = Parser(list_string, 10)
freq_dist = parse.parse()

print freq_dist

plot = test_plotly(freq_dist)