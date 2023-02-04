from typing import NamedTuple
from datetime import datetime

class LoginInfo(NamedTuple):
    userId : int
    username : str
    realName : str
    roleId : int
    roleName : str

class Activity(NamedTuple):
    id : int
    subject : str
    subjectId : int
    tutorId : int
    tutor : str
    startDate : datetime
    slots : int
    slotsOccupied : int
    meetingPlace : str