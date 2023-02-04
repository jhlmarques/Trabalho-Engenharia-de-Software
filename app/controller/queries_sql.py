class Queries:
    @staticmethod
    def query_getActivityFromId(activityId):
        return ('SELECT '
        'Activities.ActivityId as Id, '
        'Subjects.SubjectName as Subject, '
        'Subjects.SubjectId as SubjectId, '
        'Employees.EmployeeId as TutorId, '
        'Employees.CompleteName as Tutor, '
        'Activities.StartDate as StartDate, '
        'Activities.SlotsAmount as Slots, '
        'count(ActivityAllocation.ActivityId) as OccupiedSlots, '
        'Activities.MeetingPlace as MeetingPlace '
        'FROM Activities '
        'JOIN Subjects ON (Subjects.SubjectId = Activities.SubjectId) '
        'JOIN Employees ON (Activities.TutorId = Employees.EmployeeId) '
        'LEFT JOIN ActivityAllocation ON (Activities.ActivityId = ActivityAllocation.ActivityId) '
        f'WHERE ActivityAllocation.ActivityId = {activityId} '
        'OR ActivityAllocation.ActivityId IS NULL '
        'GROUP BY '
        'Activities.ActivityId, '
        'Subjects.SubjectName, '
        'Subjects.SubjectId, '
        'Employees.EmployeeId, '
        'Employees.CompleteName, '
        'Activities.StartDate, '
        'Activities.SlotsAmount, '
        'Activities.MeetingPlace '
        'ORDER BY Activities.ActivityId ')


    @staticmethod
    def query_getUserSubscribedActivities(login):
        return (
        'SELECT '
        'Activities.ActivityId as Id, '
        'Subjects.SubjectName as Subject, '
        'Subjects.SubjectId as SubjectId, '
        'Employees.EmployeeId as TutorId, '
        'Employees.CompleteName as Tutor, '
        'Activities.StartDate as StartDate, '
        'Activities.SlotsAmount as Slots, '
        'count(ActivityAllocation.ActivityId) as OccupiedSlots, '
        'Activities.MeetingPlace as MeetingPlace '
        'FROM Activities '
        'JOIN Subjects ON (Subjects.SubjectId = Activities.SubjectId) '
        'JOIN Employees ON (Activities.TutorId = Employees.EmployeeId) '
        'LEFT JOIN ActivityAllocation ON (Activities.ActivityId = ActivityAllocation.ActivityId) '
        'WHERE ActivityAllocation.ActivityId in '
        '( '
        '    SELECT ActivityAllocation.ActivityId '
        '    FROM ActivityAllocation '
        '    JOIN Employees ON (ActivityAllocation.EmployeeId = Employees.EmployeeId) '
        f'   WHERE Employees.username = \'{login.username}\' '
        ')'
        'GROUP BY '
        'Activities.ActivityId, '
        'Subjects.SubjectName, '
        'Subjects.SubjectId, '
        'Employees.EmployeeId, '
        'Employees.CompleteName, '
        'Activities.StartDate, '
        'Activities.SlotsAmount, '
        'Activities.MeetingPlace '
        'ORDER BY Activities.ActivityId '
        )

    @staticmethod
    def query_getUserAvailableActivities(login):
        return (
        'SELECT '
        'Activities.ActivityId as Id, '
        'Subjects.SubjectName as Subject, '
        'Subjects.SubjectId as SubjectId, '
        'Employees.EmployeeId as TutorId, '
        'Employees.CompleteName as Tutor, '
        'Activities.StartDate as StartDate, '
        'Activities.SlotsAmount as Slots, '
        'count(ActivityAllocation.ActivityId) as OccupiedSlots, '
        'Activities.MeetingPlace as MeetingPlace '
        'FROM Activities '
        'JOIN Subjects ON (Subjects.SubjectId = Activities.SubjectId) '
        'JOIN Employees ON (Activities.TutorId = Employees.EmployeeId) '
        'LEFT JOIN ActivityAllocation ON (Activities.ActivityId = ActivityAllocation.ActivityId) '
        'WHERE ActivityAllocation.ActivityId NOT in '
        '( '
        '    SELECT ActivityAllocation.ActivityId '
        '    FROM ActivityAllocation '
        '    JOIN Employees ON (ActivityAllocation.EmployeeId = Employees.EmployeeId) '
        f'   WHERE Employees.username = \'{login.username}\' '
        ') OR ActivityAllocation.ActivityId IS NULL '
        'GROUP BY '
        'Activities.ActivityId, '
        'Subjects.SubjectName, '
        'Subjects.SubjectId, '
        'Employees.EmployeeId, '
        'Employees.CompleteName, '
        'Activities.StartDate, '
        'Activities.SlotsAmount, '
        'Activities.MeetingPlace '
        'ORDER BY Activities.ActivityId '
        )

    @staticmethod
    def query_subscribeUserToActivity(login, activity):
        return (
            'INSERT INTO ActivityAllocation (ActivityId, EmployeeId) '
            f'VALUES ({activity.id},{login.userId})'
        )

    @staticmethod
    def query_getLoginInfo(username):
        return (
            'SELECT EmployeeId, Username, CompleteName, Employees.RoleId, RoleName '
            'FROM dbo.Employees '
            'JOIN dbo.Roles ON (Employees.RoleId = Roles.RoleId) '
            f'WHERE Username = \'{username}\''
        )

    @staticmethod
    def query_get_user_password(username):
        return (f'select Password from dbo.Employees where Username = \'{username}\'')