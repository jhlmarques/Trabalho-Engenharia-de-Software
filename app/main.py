from flask import Flask, render_template, request, redirect, session
from controller.login_controller import LoginController
from controller.schedule_controller import ScheduleController
from model.models import Activity
from typing import List

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
            
            return redirect("/activities")

    # Check if there was a valid login in this session and redirect to the main page
    elif request.method == "GET":
        if('username' in session):
            return redirect("/activities")
       
    return render_template('login.html')


@app.route("/activities", methods=["GET", "POST"])
def activities():
    if request.method == "GET":
        s_controller = ScheduleController()
        l_controller = LoginController()
        loginInfo = l_controller.getLoginInfo(session['username'])

        activities = s_controller.getUserAvaiableActivities(loginInfo)
        
        return render_template('activities.html')

    elif request.method == "POST":
        s_controller = ScheduleController()
        l_controller = LoginController()
        loginInfo = l_controller.getLoginInfo(session['username'])
        
        # Placeholder; using URL arguments
        activity_id = request.args.get('id')
        activity = s_controller.getActivityFromId(activity_id)
        s_controller.subscribeUserToActivity(loginInfo, activity)

        # Placeholder; check if the activity is removed from the table
        activities = s_controller.getUserAvaiableActivities(loginInfo)
        
        return render_template('activities.html')

@app.route("/tutors", methods=["GET"])
def tutors():
    return render_template('tutors.html')


@app.route("/logout", methods=["POST"])
def logout():
    session.pop('username', None)
    return redirect('/')


if __name__ == "__main__":
    app.run()
