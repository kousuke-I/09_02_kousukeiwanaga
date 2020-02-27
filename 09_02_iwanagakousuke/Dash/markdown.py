
import dash
import dash_core_components as dcc
import dash_html_components as html

# 外部のstylesheetsを読み込む
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# アプリケーションを宣言
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout =html.Div([
    dcc.Markdown('''
# 見出し1
## 見出し2
    
- 箇条書き
- 箇条書き
- 箇条書き
    ''')
])

if __name__ == '__main__':
    # サーバー内で実行、debug=trueはデバッグモードで実行
    app.run_server(debug=True)
