#!/usr/bin/env python

__author__ = 'McClain Marchman'

# https://plot.ly/~mmmarchman/31

import plotly.plotly as py
import plotly.graph_objs as go


class TestPlotly:

    word_count_list = None
    title = None
    data = None
    layout = None
    fig = None
    words = []
    counts = []

    def __init__(self, word_count_list):
        self.word_count_list = word_count_list

    def plot(self):
        for j, k in reversed(self.word_count_list):
            self.words.append(j)
            self.counts.append(k)

        trace_bar1 = go.Bar(
            x=self.counts,
            y=self.words,
            orientation='h',
            marker=go.Marker(color='#E3BA22'))

        # Make Data object
        self.data = go.Data([trace_bar1])

        self.title = 'Word Frequency'  # plot's title

        # Make Layout object
        self.layout = go.Layout(
            title=self.title,       # set plot title
            showlegend=False,  # remove legend
            orientation = 'h',
            width=700,
            height=700,
            autosize=False,
            yaxis=go.YAxis(title='Words', zeroline=False, gridcolor='white'),
            xaxis=go.XAxis(title='Frequency', gridcolor='white'),

            paper_bgcolor='rgb(233,233,233)',  # set paper (outside plot)
            plot_bgcolor='rgb(233,233,233)',   # and plot color to grey
            )

        # Make Figure object
        self.fig = go.Figure(data=self.data, layout=self.layout)

        # (@) Send to Plotly and show in notebook
        py.plot(self.fig, filename='CITA-Bar-Graph', auto_open=False)













