from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    user = {'nick': 'Alex'}
    return render_template('welcome.html', user_name = user['nick'])

@app.route('/about')
def about():
    return "Сайт был сделан Андреем Ситало"

@app.route('/sum', methods = ['POST', 'GET'])
def sum():
    ll = False
    c = 0
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        ll = True
        c = int(a) + int(b)
    return render_template('summator.html', l = ll, res = c)

if __name__ == "__main__":
    app.run(debug = True)