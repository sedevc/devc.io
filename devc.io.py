from flask import Flask, abort, url_for, render_template, request, flash, redirect
from forms import LoginForm

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    pagename = "Start"
    return render_template('tpl.html', pagename=pagename)

@app.route('/about')
def about():
    pagename = "Om"
    return render_template('tpl.html', pagename=pagename)

@app.route('/cv')
def cv():
    pagename = "CV"
    return render_template('tpl.html', pagename=pagename)

@app.route('/contact')
def contact():
    pagename = "Kontakt"
    return render_template('tpl.html', pagename=pagename)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/')
    return render_template('login.html',
                           title='Sign In',
                           form=form)


if __name__ == '__main__':
    app.debug = True
    app.run()





with app.test_request_context():
    print url_for('hello_world')
