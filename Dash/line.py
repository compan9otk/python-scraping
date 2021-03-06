import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(r'C:\git\python-scraping\Dash\time_series.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout=html.Div([
  dcc.Graph(
    id='sample-line',
    figure={
      'data':[
        go.Scatter(
          x=df['date'],
          y=df['MSFT'],
          mode='lines',
          opacity=0.7,
          marker={
            'size':15
          },
          name='Microsoft'
        ),
        go.Scatter(
            x=df['date'],
            y=df['AAPL'],
            mode='lines',
            opacity=0.7,
            marker={
                'size': 15
            },
            name='Apple'
        )
      ],
      'layout': go.Layout(
        xaxis={'title':'x軸'},
        yaxis={'title':'y軸'},
        width=1000,
        height=500
      )
    }
  )
])

if __name__ == '__main__':
    app.run_server(debug=True)
