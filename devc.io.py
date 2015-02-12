from flask import Flask, url_for, render_template, request


app = Flask(__name__)


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
            todo = Todo(request.form['title'], request.form['text'])
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('new.html')

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