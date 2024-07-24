from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'supersecretkey'


# In-memory storage for voters and votes (determine data to the memory)
voters = {}
votes = []
# main route
@app.route('/')
def index():
    return render_template('login.html')
# login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in voters and voters[username] == password:
            session['user_id'] = username
            return redirect(url_for('vote'))
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in voters:
            voters[username] = password
            return redirect(url_for('login'))
        return 'User already exists'
    return render_template('register.html')

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        candidate = request.form['candidate']
        votes.append({'voter': session['user_id'], 'candidate': candidate})
        return redirect(url_for('result'))
    return render_template('vote.html')

@app.route('/result')
def result():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    results = {}
    for vote in votes:
        candidate = vote['candidate']
        if candidate in results:
            results[candidate] += 1
        else:
            results[candidate] = 1
    return render_template('result.html', votes=results.items())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
