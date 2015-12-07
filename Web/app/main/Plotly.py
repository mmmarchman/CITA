#!/usr/bin/env python

__author__ = 'McClain Marchman'

# https://plot.ly/~mmmarchman/31

import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('CITAservice', 'ej6bllje5v')


class TestPlotly:

    word_count_list = None
    title = None
    data = None
    layout = None
    fig = None
    words = []
    counts = []
    words2 = []
    counts2 = []

    def __init__(self, word_count_list, word_count_list2):
        self.word_count_list = word_count_list
        self.word_count_list2 = word_count_list2

    def plot(self):
        for j, k in reversed(self.word_count_list):
            self.words.append(j)
            self.counts.append(k)
        for j, k in reversed(self.word_count_list2):
            self.words2.append(j)
            self.counts2.append(k)

        trace_bar1 = go.Bar(
            x=self.counts,
            y=self.words,
            orientation='h',
            marker=go.Marker(color=u'rgb(222, 113, 88)'))

        trace_bar2 = go.Bar(
            x=self.counts2,
            y=self.words2,
            orientation='h',
            marker=go.Marker(color=u'rgb(84, 172, 234)'))


        # Make Data object
        self.data = go.Data([trace_bar1, trace_bar2])

        self.title = 'Word Frequency'  # plot's title

        # Make Layout object
        self.layout = go.Layout(
            title=self.title,       # set plot title
            showlegend=False,  # remove legend
            orientation = 'h',
            width=500,
            height=500,
            autosize=True,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            yaxis=go.YAxis(title='Words', zeroline=False, gridcolor='white'),
            xaxis=go.XAxis(title='Frequency', gridcolor='white'),
            barmode='group'


            )

        # Make Figure object
        self.fig = go.Figure(data=self.data, layout=self.layout)

        # (@) Send to Plotly and show in notebook
        py.plot(self.fig, filename='CITA-Bar-Graph', auto_open=False)













