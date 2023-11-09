from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name)

@app.route('/')
def login():
    return render_template('tan.html')

@app.route('/neww.html', methods=['POST'])
def login_submit():

    return redirect(url_for('neww'))

@app.route('/neww.html')
def neww():
    return render_template('neww.html')

if __name__ == '__main__':
    app.run(debug=True)
