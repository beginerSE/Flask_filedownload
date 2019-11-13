from flask import Flask, send_from_directory
import os
app = Flask(__name__)


@app.route('/')
def index():
    return "<html><h3>Flaskでファイルダウンロードを実装する</h3><a href='/export'>csvダウンロード</a></html>"


@app.route("/export")
def export_action():
    # 現在のディレクトリを取得
    path = os.path.abspath(__file__)[:-7]
    return send_from_directory(
        directory=path + '\export_temp',
        filename='test.csv',
        as_attachment=True,
        attachment_filename='test.csv',
    )


app.run(debug=True)
