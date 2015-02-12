from flask import Flask, abort, url_for, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('tpl.html')

@app.route('/about')
def about():
    return render_template('tpl.html')

@app.route('/cv')
def cv():
    return render_template('tpl.html')

@app.route('/contact')
def contact():
    return render_template('tpl.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    abort(401)
    if request.method == 'POST':
        return render_template('tpl.html')
    else:
        return render_template('tpl.html')


if __name__ == '__main__':
    app.debug = True
    app.run()




"""
with app.test_request_context():
    print url_for('hello_world')
"""