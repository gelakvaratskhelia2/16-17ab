from flask import Flask, render_template, url_for, redirect, session, request, flash, get_flashed_messages
app = Flask(__name__)

# მაგალითისთვის რომელიც იყენებს რეგისტრაციის ფორმას
@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/about")
def about():

@app.route('/login"', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        session['username'] = request.form["username"]
        return redirect(url_for("hello_world"))
    return render_template('login.html')




@app.route('/logout', methods=['POST'])
def logout():
    return render_template('login.html')
@app.route('/login', methods=['GET'])
def login_page():

    return render_template('login.html')
if __name__ == '__main__':
    app.run(debug=True)