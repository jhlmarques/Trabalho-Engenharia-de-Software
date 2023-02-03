from flask import Flask, render_template, request, redirect, session
from controller.login_controller import LoginController, LoginInfo
from controller.schedule_controller import ScheduleController

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
    if request.method == "GET":
        controller = ScheduleController()
        loginInfo = LoginInfo(
        session['username'],
        session['realName'],
        session['roleId'],
        session['roleName']
        )
        
        activities = controller.getUserActivities(loginInfo)
        html_output = ('<table><tr>'
        '<th>Assunto</th>'
        '<th>Tutor</th>'
        '<th>Data</th>'
        '<th>Ocupação</th>'
        '<th>Localização</th>'
        '</tr>')
        for activity in activities:
            html_output += '<tr>'
            html_output += (
                f'<th>{activity.subject}</th>'
                f'<th>{activity.tutor}</th>'
                f'<th>{activity.startDate}</th>'
                f'<th>{activity.slotsOccupied}/{activity.slots}</th>'
                f'<th>{activity.meetingPlace}</th>'
            )
            html_output += '</tr>'
        html_output += '</table>'
        return html_output

    return render_template('activities.html')

if __name__ == "__main__":
    app.run()
