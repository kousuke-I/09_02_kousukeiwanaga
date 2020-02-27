

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go
import pandas as pd

df=pd.read_csv('time_series.csv')

# 外部のstylesheetsを読み込む
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# アプリケーションを宣言
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
                  name='Microsf'
                ),
                go.Scatter(
                  x=df['date'],
                  y=df['AAPL'],
                  mode='lines',
                  opacity=0.7,
                  marker={
                      'size':15
                  },
                  name='Apple'
                )
            ],
            'layout':go.Layout(
                xaxis={'title':'x軸'},
                yaxis={'title':'y軸'},
                width=1000,
                height=500
            )

        }
    )
])



if __name__ == '__main__':
    # サーバー内で実行、debug=trueはデバッグモードで実行
    app.run_server(debug=True)
