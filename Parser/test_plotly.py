#!/usr/bin/env python

__author__ = 'McClain Marchman'

# https://plot.ly/~mmmarchman/31

import plotly.plotly as py
import plotly.graph_objs as go


class TestPlotly:

    word_count_list = None

    def __init__(self, word_count_list):
        self.word_count_list = word_count_list
        words = []
        counts = []

        for j,k in self.word_count_list:
            words.append(j)
            counts.append(k)
        data = [
        go.Bar(
            x=counts,
            y=words, # ['Red', 'Green', 'Blue']
            orientation='h',
                )
        ]
        plot_url = py.plot(data, filename='horizontal-bar')





