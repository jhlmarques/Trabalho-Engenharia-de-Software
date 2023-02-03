from flask import Flask, render_template, request, redirect, session
from controller.login_controller import LoginController

app = Flask(__name__)

app.secret_key = 'khjNejV9pKHs8PXXgIJ7R1yMmxgWZyC6'

   
# Handles login attempts
@app.route("/", methods=["GET", "POST"])
def login():
    # Verify login and save to session
    if request.method == "POST":
        controller = LoginController()
        username = request.form.get("username")
        password = request.form.get("password")

        is_authenticated = controller.authenticate_user(username, password)
        if is_authenticated:
            loginInfo = controller.getLoginInfo(username)
            session['username'] = loginInfo.username
            session['realName'] = loginInfo.realName
            session['roleId'] = loginInfo.roleId
            session['roleName'] = loginInfo.roleName
            
            return redirect("/activities")

    # Check if there was a valid login in this session and redirect to the main page
    elif request.method == "GET":
        if('username' in session):
            return redirect("/activities")
       
    return render_template('login.html')


@app.route("/activities", methods=["GET", "POST"])
def activities():
    return render_template('activities.html')

if __name__ == "__main__":
    app.run()
