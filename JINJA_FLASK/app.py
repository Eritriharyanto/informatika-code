from flask import Flask, render_template

app = Flask(__name__)

users = [
    {'name': 'Putri', 'age': '30', 'location': 'BANTUL'},
    {'name': 'Nurmala', 'age': '25', 'location': 'PALEMBANG'},
    {'name': 'Haryanto Ihirrr', 'age': '35', 'location': 'Ihiiiiiiiirrrrrrrrrrrrrrr'}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users')
def list_users():
    return render_template('users.html', users=users)

if __name__ == "__main__":
    app.run(debug=True)