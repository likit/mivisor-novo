from flask import Flask, render_template

PORT = 5003

app = Flask(__name__)


@app.route('/')
def hello_world():
    print('hello, from Flask')
    return render_template('index.html')


def start_server():
    app.run(port=PORT)


if __name__ == '__main__':
    app.run(debug=True)

