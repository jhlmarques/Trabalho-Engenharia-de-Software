from controller.database_controller import DatabaseController
from model.models import Activity, LoginInfo
from controller.queries_sql import Queries

from typing import NamedTuple

class ScheduleController:
    def __init__(self):
        self.database = DatabaseController()

    def getActivityFromId(self, activityId : int):
        query = Queries.query_getActivityFromId(activityId)
        table_rows = self.database.execute_query(query)
        return Activity(*table_rows[0])

    def getUserSubscribedActivities(self, login : LoginInfo):
        query = Queries.query_getUserSubscribedActivities(login)
        table_rows = self.database.execute_query(query)
        activities = [
            Activity(*table_rows[i])
            for i in range(len(table_rows[:]))
        ]
        return activities

    def getUserAvailableActivities(self, login : LoginInfo):
        query = Queries.query_getUserAvailableActivities(login)
        table_rows = self.database.execute_query(query)
        activities = []
        for i in range(len(table_rows[:])):
            # Tutors can't see their own activities, and full activities can't be subscribed
            if (login.realName != table_rows[i][4]) and (table_rows[i][7] < table_rows[i][6]):
                activities.append(Activity(*table_rows[i]))

        return activities

    def subscribeUserToActivity(self, login : LoginInfo, activity : Activity):
        if activity.slotsOccupied < activity.slots:
            query = Queries.query_subscribeUserToActivity(login, activity)
            self.database.execute_insert(query)
            return True
        else:
            return False

    def unsubscribeUserFromActivity(self, login : LoginInfo, activity : Activity):
        query = (
            'DELETE FROM ActivityAllocation '
            F'WHERE ActivityId = {activity.id} AND EmployeeId = {login.userId}'
        )
        self.database.execute_insert(query)        

    def isUserSubscribed(self, login : LoginInfo, activity : Activity):
        query = (
            'SELECT * FROM ActivityAllocation '
            f'WHERE ActivityId = {activity.id} AND EmployeeId = {login.userId}'
        )
        table_rows = self.database.execute_query(query)
        return len(table_rows) > 0

    def addNewMentorship(self, login: LoginInfo, subject : str, date : str):
        query = (
            'SELECT Subjects.SubjectId FROM Subjects '
            f"WHERE SubjectName = '{subject}'"
        )
        table_rows = self.database.execute_query(query)
        subject_id = table_rows[0][0]
        
        query = (
            'INSERT INTO Activities (TutorId, SubjectId, MeetingPlace, StartDate, SlotsAmount, Finished) '
            'VALUES '
            f"({login.userId}, {subject_id}, 'Online', '{date}', 1, 0)"
        )
        self.database.execute_insert(query)

    def addNewWorkshop(self, login: LoginInfo, subject : str, date : str, meeting_place : str, slots : int):
        query = (
            'SELECT Subjects.SubjectId FROM Subjects '
            f"WHERE SubjectName = '{subject}'"
        )
        table_rows = self.database.execute_query(query)
        subject_id = table_rows[0][0]
        
        query = (
            'INSERT INTO Activities (TutorId, SubjectId, MeetingPlace, StartDate, SlotsAmount, Finished) '
            'VALUES '
            f"({login.userId}, {subject_id}, '{meeting_place}', '{date}', {slots}, 0)"
        )
        self.database.execute_insert(query)


    def getTutorSubjects(self, login : LoginInfo):
        query = (
            'SELECT * FROM Subjects '
            'JOIN TutorSubjects ON (Subjects.SubjectId = TutorSubjects.SubjectId) '
            f'WHERE TutorSubjects.TutorId = {login.userId}'
        )
        table_rows = self.database.execute_query(query)
        r_list = []
        for i in range(len(table_rows[:])):
            subject = NamedTuple('Subject', id=int, name=str)
            subject.id, subject.name = table_rows[i][0], table_rows[i][1]
            r_list.append(subject)

        return r_list

    def get_tutors_info(self):
        query = (
            'SELECT CompleteName, SubjectName '
            'FROM Employees JOIN TutorSubjects ON (Employees.EmployeeId = TutorSubjects.TutorId) '
            'JOIN Subjects ON (TutorSubjects.SubjectId = Subjects.SubjectId)'
        )
        table_rows = self.database.execute_query(query)
        tutor_subject_dict = {}
        for tutor_name, subject in table_rows:
            if tutor_name not in tutor_subject_dict:
                tutor_subject_dict[tutor_name] = [subject]
            else:
                tutor_subject_dict[tutor_name].append(subject)
        return tutor_subject_dict
