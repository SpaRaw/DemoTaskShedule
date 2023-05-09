from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('auth.html')

@app.route('/auth')
def login():
    if request.method == 'POST':
        return("post")
    if request.method == 'GET':
        return("get")

@app.route('/auth/content')
def auth_content():
    pass

@app.route('/auth/api', methods=['SEND'])
def auth_api():
    pass

@app.route('/api', methods=['SEND'])
def api():

    return redirect("/")




if __name__ == '__main__':
    app.run(debug=True)
