from flask import Flask, render_template, request, redirect, session, url_for
from flask import jsonify, send_from_directory

app = Flask(__name__)

@app.route("/")
def indec():
    render_template('index.html')

@app.route('/csv_export')
def export_template():
    render_template('export.html')

@app.route("/export_action/<file_name>")
def export_action(file_name):
    return send_from_directory(
        directory='/export_tmp',
        filename=file_name,
        as_attachment=True,
        attachment_filename=file_name,
        mimetype='XLSX_MIMETYPE')
    
