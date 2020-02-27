
import dash
import dash_core_components as dcc
import dash_html_components as html

# 外部のstylesheetsを読み込む
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# アプリケーションを宣言
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors ={
    'background':'black',
    'text':'white'
}

# htmlをdivで括って、子要素表示
app.layout = html.Div(children=[
    # htmlのH1タグ
    html.H1(
        children='Hello Dash',
        style={
            'textAlign':'center',
            'color':colors['text'],
            # 'background-color':colors['background']
        }
    ),
    # htmlのdivタグ
    html.Div(
        children='''
        Dash: A web application framework for Python.
        ''',
        style={
            'textAlign':'center',
            'color':colors['text'],
            # 'background-color':colors['background']
        }
    ),
    # グラフ部分
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                # x軸、y軸、棒グラフ、name←青い棒グラフ
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                # x軸、y軸、棒グラフ、name←オレンジの棒グラフ
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
            ],
            'layout': {
                # グラフタイトル
                'title': 'Dash Data Visualization',
                'plot_bgcolor':colors['background'],
                'paper_bgcolor':colors['background'],
                'font':colors['text']
            }
        }
    )
])

if __name__ == '__main__':
    # サーバー内で実行、debug=trueはデバッグモードで実行
    app.run_server(debug=True)
