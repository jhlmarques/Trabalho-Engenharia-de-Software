from typing import NamedTuple
from datetime import datetime

class LoginInfo(NamedTuple):
    userId : int
    username : str
    realName : str
    roleName : str
    roleId : int

class Activity(NamedTuple):
    id : int
    subject : str
    tutor : str
    startDate : datetime
    slots : int
    slotsOccupied : int
    meetingPlace : str