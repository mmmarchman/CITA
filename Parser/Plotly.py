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

        for j, k in self.word_count_list:
            words.append(j)
            counts.append(k)

        trace_bar1 = go.Bar(
            x=counts,
            y=words,
            # orientation='h',
            marker=go.Marker(color='#E3BA22'))

        # Make Data object
        data = Data([trace1])

        title = 'Word Frequency'  # plot's title

    # Make Layout object
    layout = Layout(
        title=title,       # set plot title
        showlegend=False,  # remove legend
        orientation = 'h',
        yaxis= YAxis(
            title='Temperature [in deg. C]', # y-axis title
            # range=[-15.5,25.5],              # set range
            zeroline=False,                  # remove thick line at y=0
            gridcolor='white'                # set grid color to white
            ),
    paper_bgcolor='rgb(233,233,233)',  # set paper (outside plot)
    plot_bgcolor='rgb(233,233,233)',   #   and plot color to grey
)


# Make Figure object
fig = Figure(data=data, layout=layout)

# (@) Send to Plotly and show in notebook
py.plot(fig, filename='CITA-Bar-Graph')







