import dash
from dash import dcc
from dash import html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Markdown('''
# 見出し1
## 見出し2

- 箇条書き
- 箇条書き
- 箇条書き
    ''')
])

if __name__ == '__main__':
    app.run_server(debug=True)
