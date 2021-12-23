from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return redirect('https://goo.su/aLtG')


@app.route('/ya')
def index():
    return redirect('https://ya.ru')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
