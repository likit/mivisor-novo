from flask import Flask, render_template
from .projects import project_bp
import webview

PORT = 5003

app = Flask(__name__)

app.register_blueprint(project_bp, url_prefix='/projects')

window = webview.create_window('Mivisor Novo', f'http://localhost:{PORT}')

@app.route('/')
def hello_world():
    print('hello, from Flask')
    return render_template('index.html')


@app.route('/projects/new')
def new_project():
    window.create_file_dialog(dialog_type=webview.FOLDER_DIALOG)


def start_server():
    app.run(port=PORT)

