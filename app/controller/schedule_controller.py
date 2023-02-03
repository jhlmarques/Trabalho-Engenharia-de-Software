from controller.database_controller import DatabaseController
from model.models import Activity, LoginInfo


class ScheduleController:
    def __init__(self):
        self.database = DatabaseController()

    def getUserSubscribedActivities(self, login : LoginInfo):
        query = (
        'SELECT '
        'Activities.ActivityId as Id, '
        'Subjects.SubjectName as Subject, '
        'Employees.CompleteName as Tutor, '
        'Activities.StartDate as StartDate, '
        'Activities.SlotsAmount as Slots, '
        'count(ActivityAllocation.ActivityId) as OccupiedSlots, '
        'Activities.MeetingPlace as MeetingPlace '
        'FROM Activities '
        'JOIN Subjects ON (Subjects.SubjectId = Activities.SubjectId) '
        'JOIN Employees ON (Activities.TutorId = Employees.EmployeeId) '
        'JOIN ActivityAllocation ON (Activities.ActivityId = ActivityAllocation.ActivityId) '
        'WHERE ActivityAllocation.ActivityId in '
        '( '
        '    SELECT ActivityAllocation.ActivityId '
        '    FROM ActivityAllocation '
        '    JOIN Employees ON (ActivityAllocation.EmployeeId = Employees.EmployeeId) '
        f'   WHERE Employees.username = \'{login.username}\' '
        ') '
        'GROUP BY '
        'Activities.ActivityId, '
        'Subjects.SubjectName, '
        'Employees.CompleteName, '
        'Activities.StartDate, '
        'Activities.SlotsAmount, '
        'Activities.MeetingPlace '
        'ORDER BY Activities.ActivityId '
        )
        table_rows = self.database.execute_query(query)
        activities = [
            Activity(table_rows[i][0], table_rows[i][1], table_rows[i][2], table_rows[i][3], table_rows[i][4], table_rows[i][5], table_rows[i][6])
            for i in range(len(table_rows[:]))
        ]
        return activities

    def getUserAvaiableActivities(self, login : LoginInfo):
        query = (
        'SELECT '
        'Activities.ActivityId as Id, '
        'Subjects.SubjectName as Subject, '
        'Employees.CompleteName as Tutor, '
        'Activities.StartDate as StartDate, '
        'Activities.SlotsAmount as Slots, '
        'count(ActivityAllocation.ActivityId) as OccupiedSlots, '
        'Activities.MeetingPlace as MeetingPlace '
        'FROM Activities '
        'JOIN Subjects ON (Subjects.SubjectId = Activities.SubjectId) '
        'JOIN Employees ON (Activities.TutorId = Employees.EmployeeId) '
        'JOIN ActivityAllocation ON (Activities.ActivityId = ActivityAllocation.ActivityId) '
        'WHERE ActivityAllocation.ActivityId NOT in '
        '( '
        '    SELECT ActivityAllocation.ActivityId '
        '    FROM ActivityAllocation '
        '    JOIN Employees ON (ActivityAllocation.EmployeeId = Employees.EmployeeId) '
        f'   WHERE Employees.username = \'{login.username}\' '
        ') '
        'GROUP BY '
        'Activities.ActivityId, '
        'Subjects.SubjectName, '
        'Employees.CompleteName, '
        'Activities.StartDate, '
        'Activities.SlotsAmount, '
        'Activities.MeetingPlace '
        'ORDER BY Activities.ActivityId '
        )
        table_rows = self.database.execute_query(query)
        activities = [
            Activity(table_rows[i][0], table_rows[i][1], table_rows[i][2], table_rows[i][3], table_rows[i][4], table_rows[i][5], table_rows[i][6])
            for i in range(len(table_rows[:]))
        ]
        return activities

    def subscribeUserToActivity(self, login : LoginInfo, activity_id : int):
        query = (
            'INSERT INTO ActivityAllocation (ActivityId, EmployeeId)'
            f'VALUES ({activity_id},{login.userId})'
        )
        self.database.execute_insert(query)

    