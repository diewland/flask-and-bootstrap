from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/one', methods=['GET'])
def one():
    return render_template('one.html')


@app.route('/two', methods=['GET'])
def two():
    return render_template('two.html')

if __name__ == '__main__':
    app.run(debug=True)
