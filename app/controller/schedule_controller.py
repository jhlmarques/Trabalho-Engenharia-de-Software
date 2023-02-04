from controller.database_controller import DatabaseController
from model.models import Activity, LoginInfo
from controller.queries_sql import Queries


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
            if login.realName != table_rows[i][2]:
                activities.append(Activity(*table_rows[i]))

        return activities

    def subscribeUserToActivity(self, login : LoginInfo, activity : Activity):
        if activity.slotsOccupied < activity.slots:
            query = Queries.query_subscribeUserToActivity(login, activity)
            self.database.execute_insert(query)
            return True
        else:
            return False

    