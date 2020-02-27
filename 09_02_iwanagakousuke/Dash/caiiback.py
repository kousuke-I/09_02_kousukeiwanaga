
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output

# 外部のstylesheetsを読み込む
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# アプリケーションを宣言
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout=html.Div([
    dcc.Input(id='input-div',value='initial value',type='text'),
    html.Div(id='output-div')
])
@app.callback(
    Output(component_id='output-div',component_property='children'),
    [Input(component_id='input-div',component_property='value')]
)
def update(input_value):
    return 'You entered{}'.format(input_value)

if __name__ == '__main__':
    # サーバー内で実行、debug=trueはデバッグモードで実行
    app.run_server(debug=True)