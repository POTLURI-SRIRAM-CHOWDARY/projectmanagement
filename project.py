from abc import ABC 
from enum import Enum 


class TaskStatus(Enum):
    OPEN,PROGRESS,STRUCK,DONE= 1,2,3,4
    
class AccountStatus(Enum):
    ACTIVE,CLOSE=1,2
    
class Constants:
    def __init__(self):
        self.NUMBER_OF_DAYS_IN_SPRINT = 14
        

