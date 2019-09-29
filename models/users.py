class User:
    def __init__(self,UserID,UserName,Email,MobileNumber):
        self.__UserID = UserID
        self.__UserName = UserName
        self.__Email = Email
        self.__MobileNumber = MobileNumber
        self.__CurrentBalance = 0
        self.__Dues = {}
    
    def getUserID(self):
        return self.__UserID
    
    def getUserName(self):
        return self.__UserName

    def getEmail(self):
        return self.__Email
    
    def getMobileNumber(self):
        return self.__MobileNumber
    
    def setCurrentBalance(self,Amount):
        self.__CurrentBalance = self.__CurrentBalance + Amount
    
    def getDuesDetails(self):
        return self.__Dues

    def removeUserFromDebtList(self,UserID):
        if UserID in self.__Dues:
            del self.__Dues[UserID]
    
    def setDues(self,UserID,Amount,IsSummary=False):
        if UserID in self.__Dues and self.__Dues[UserID] and IsSummary == False:
            new_amount = self.__Dues[UserID] + Amount

            if new_amount != 0:
                self.__Dues[UserID] = new_amount
            else:
                del self.__Dues[UserID]
        else:
            self.__Dues[UserID] = Amount

