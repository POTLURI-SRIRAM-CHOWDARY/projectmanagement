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
    
class Project:
    def __init__(self,id,startdate):
        self.__id = id
        self.__startdate = startdate
        self.__enddate = startdate+Constants.NUMBER_OF_DAYS_IN_SPRINT
        self.__tasks = []
        
    def add_task(self,task):
        pass
        
    def remove_task(self,task):
        pass
    
    def get_end_date(self):
        pass
    
class ProjectStats(self):
    
    def __init__(self,project):
        self.__project = project
    

    def minimum_time_to_complete_project(self):
        pass

class Task:
    def __init__(self,name,description,startdate,enddate,employee):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__startdate = startdate
        self.__enddate = enddate
        self.__owner = employee
        self.__status = TaskStatus.OPEN
        self.__dependencytasks =[]
        
    def get_status(self):
        pass
    
    def get_dependency_tasks(self):
        pass
    
    def change_status(self,status):
        pass
    
    def change_name(self,name):
        pass
    
    def number_of_days_to_complete_task(self):
        pass
    
    def change_description(self,description):
        pass
    
    def change_end_date(self,enddate):
        pass
    
    def add_dependency_tasks(self,task):
        pass
    
    def remove_dependency_tasks(self,tasks):
        pass



