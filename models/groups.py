class Groups:
    '''
    Group functionality is not supported yet...
    '''
    def __init__(self):
        self.__GroupName = ""
        self.__Users = {}

    def getUsers(self):
        return self.__Users
    
    def setUsers(self,UsersObject):
        self.__Users = UsersObject
    
    def getGroupName(self):
        return self.__GroupName
    
    def setGroupName(self,GroupName):
        self.__GroupName =  GroupName