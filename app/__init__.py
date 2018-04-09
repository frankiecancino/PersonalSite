from flask import Flask, render_template, request


app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run()