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
        for j, k in self.word_count_list:
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
            yaxis= go.YAxis(
            title='Words', # y-axis title
            # range=[-15.5,25.5],              # set range
            zeroline=False,                  # remove thick line at y=0
            gridcolor='white'                # set grid color to white
            ),
            paper_bgcolor='rgb(233,233,233)',  # set paper (outside plot)
            plot_bgcolor='rgb(233,233,233)',   #   and plot color to grey
            )
                # Make Figure object
        self.fig = go.Figure(data=self.data, layout=self.layout)

        # (@) Send to Plotly and show in notebook
        py.plot(self.fig, filename='CITA-Bar-Graph')










