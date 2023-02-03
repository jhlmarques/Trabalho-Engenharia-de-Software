from typing import NamedTuple
from datetime import datetime

class LoginInfo(NamedTuple):
    username : str
    realName : str
    roleName : str
    roleId : int

class Activity(NamedTuple):
    subject : str
    tutor : str
    startDate : datetime
    slots : int
    slotsOccupied : int
    meetingPlace : str