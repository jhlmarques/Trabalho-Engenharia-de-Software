from flask import Flask, render_template, request, redirect, session
from controller.login_controller import LoginController
from controller.schedule_controller import ScheduleController
from model.models import Activity
from typing import List

app = Flask(__name__)

app.secret_key = 'khjNejV9pKHs8PXXgIJ7R1yMmxgWZyC6'

MENTORSHIP='0'
WORKSHOP='1'
NO_ID=0

def isLoggedIn():
    return 'username' in session

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
            session['role'] = loginInfo.roleName
            
            return redirect("/activities")

    # Check if there was a valid login in this session and redirect to the main page
    elif request.method == "GET":
        if('username' in session):
            return redirect("/activities")

    return render_template('login.html')


@app.route("/activities", methods=["GET"])
def activities():
    if request.method == "GET":
        if not isLoggedIn():
            return redirect('/')

        s_controller = ScheduleController()
        l_controller = LoginController()
        loginInfo = l_controller.getLoginInfo(session['username'])

        avaiable_activities = s_controller.getUserAvailableActivities(loginInfo)
        subscribed_activities = s_controller.getUserSubscribedActivities(loginInfo)
        
        filter = request.args.get('filter')
        activities = subscribed_activities if filter == "subscribed" else avaiable_activities
        
        return render_template('activities.html', activities=activities, filter=filter)
    
    
@app.route("/activities/<activity_id>", methods=["GET", "POST"])
def activity_details(activity_id):
    if request.method == "GET":
        if not isLoggedIn():
            return redirect('/')

        s_controller = ScheduleController()
        l_controller = LoginController()
        loginInfo = l_controller.getLoginInfo(session['username'])
        activity = s_controller.getActivityFromId(int(activity_id))
        is_subscribed = s_controller.isUserSubscribed(loginInfo, activity)

        return render_template('activity_details.html', isSubscribed=is_subscribed, activityDetails=activity)

    elif request.method == "POST":
        if not isLoggedIn():
            return redirect('/')

        s_controller = ScheduleController()
        l_controller = LoginController()
        loginInfo = l_controller.getLoginInfo(session['username'])
        activity = s_controller.getActivityFromId(int(activity_id))

        subscribing = int(request.args.get('subscribing'))
        if subscribing:
            s_controller.subscribeUserToActivity(loginInfo, activity)
        else:
            s_controller.unsubscribeUserFromActivity(loginInfo, activity)

        return redirect('/activities')
    

@app.route("/activities/create", methods=["GET", "POST"])
def activity_creation():
    activity_type = request.args.get('activityType')
    
    if request.method == "GET":
        if not isLoggedIn():
            return redirect('/')

        s_controller = ScheduleController()
        l_controller = LoginController()
        loginInfo = l_controller.getLoginInfo(session['username'])
        
        if loginInfo.roleName != 'Mentor':
            return redirect('/activities')

        possible_subject = s_controller.getTutorSubjects(loginInfo)
        return render_template('activity_creation.html', activityType=activity_type, availableSubjects=possible_subject)
    
    elif request.method == "POST":
        if not isLoggedIn():
            return redirect('/')

        s_controller = ScheduleController()
        l_controller = LoginController()
        loginInfo = l_controller.getLoginInfo(session['username'])

        if loginInfo.roleName != 'Mentor':
            return redirect('/activities')
            
        subject = request.form.get('subject')
        datetime = request.form.get('date') + ' ' + request.form.get('time')

        # Get the activity type; Determines default values for the activity
        if activity_type == MENTORSHIP:
            s_controller.addNewMentorship(loginInfo, subject, datetime)
        else:
            meeting_place = request.form.get('meetingPlace')
            slots = request.form.get('slots')
            s_controller.addNewWorkshop(loginInfo, subject, datetime, meeting_place, slots)

        return redirect('/activities')



@app.route("/tutors", methods=["GET"])
def tutors():
    return render_template('tutors.html')


@app.route("/logout", methods=["POST"])
def logout():
    session.pop('username', None)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
