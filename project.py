from abc import ABC 
from enum import Enum 


class TaskStatus(Enum):
    OPEN,PROGRESS,STRUCK,DONE= 1,2,3,4
    
class AccountStatus(Enum):
    ACTIVE,CLOSE=1,2
    
class Constants:
    def __init__(self):
        self.NUMBER_OF_DAYS_IN_SPRINT = 14
        
class Account(ABC):
    def __init__(self,id, name, password, status=AccountStatus.ACTIVE):
        self.__id = id
        self.__name = name
        self.__password = password
        self.__status = status
        
    def reset_password(self):
        pass

class Employee(Account):
    
    def __init__(self,id,name, password, status=AccountStatus.ACTIVE):
        self.__task_list = [] 
        super().__init__(id,name,password,status)
    
    def change_task_status(self,task):
        pass
    
    def add_contributor(self,task):
        pass
    

class TeamLead(Employee):
    
    def __init__(self,id,name,password,status=AccountStatus.ACTIVE):
        super().__init__(id,name,password,status)
        
    def create_task(self,task):
        pass
    
    def delete_task(self,task):
        pass

class Admin(TeamLead):
    def add_users(self,user):
        pass
    
    def delete_users(self,user):
        pass
    

