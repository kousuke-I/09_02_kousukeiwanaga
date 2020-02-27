 
import dash
import dash_core_components as dcc
import dash_html_components as html

# 外部のstylesheetsを読み込む
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# アプリケーションを宣言
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label':'佐藤','value':'sato'},
            {'label':'鈴木','value':'suzuki'},
            {'label':'田中','value':'tanaka'},
        ],
        value='suzuki'
    ),
    html.Label('Muluti-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label':'佐藤','value':'sato'},
            {'label':'鈴木','value':'suzuki'},
            {'label':'田中','value':'tanaka'},
        ],
        value=['sato','suzuki'],
        multi=True
    ),

    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label':'佐藤','value':'sato'},
            {'label':'鈴木','value':'suzuki'},
            {'label':'田中','value':'tanaka'},
        ],
        value='suzuki'
    ),

    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': '佐藤', 'value': 'sato'},
            {'label': '鈴木', 'value': 'suzuki'},
            {'label': '田中', 'value': 'tanaka'},
        ],
        value=['suzuki', 'tanaka']
    ),

    html.Label('Text Input'),
    dcc.Input(value='佐藤', type='text'),

    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=5,
        marks={i:i for i in range(1,6)},
        value=3
    )
])
# ], style={'columnCount': 2})


if __name__ == '__main__':
    # サーバー内で実行、debug=trueはデバッグモードで実行
    app.run_server(debug=True)

 
 
 
 