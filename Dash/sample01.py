import dash
from dash import dcc
from dash import html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
      options=[
        {'label':'佐藤','value':'sato'},
        {'label':'鈴木','value':'suzuki'},
        {'label':'田中','value':'tanaka'}
      ],
      value='suzuki'
    ),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
      options=[{'label':'佐藤','value':'sato'},
        {'label':'鈴木','value':'suzuki'},
        {'label':'田中','value':'tanaka'}
      ],
      value=['sato','suzuki'],
      multi=True
    ),

    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': '佐藤', 'value': 'sato'},
            {'label': '鈴木', 'value': 'suzuki'},
            {'label': '田中', 'value': 'tanaka'}
        ],
        value='suzuki'
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)