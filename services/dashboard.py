import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from splitwise.models.users import User

class DashBoard:
    def __init__(self):
        self.__Users = {}
        self.__DebtSummary = {} #{"u1":{"u2":30},""} //u1 owes u2 Rs. 30
        self.__TransactionHistory = {}
    
    def getUsers(self):
        return self.__Users

    def getDebtSummary(self):
        
        if self.__DebtSummary:
            for from_user,owe_details in (self.__DebtSummary).items():
                for to_user,amount in owe_details.items():
                    print(from_user + " owes " + to_user + " : " + str(amount))
        else:
            print("No balances")

    def getDebtSummaryForUser(self,UserID):
        
        if self.__DebtSummary:
            for from_user,owe_details in (self.__DebtSummary).items():
                for to_user,amount in owe_details.items():
                    if from_user == UserID or to_user == UserID:
                        print(from_user + " owes " + to_user + " : " + str(amount))
        else:
            print("No balances")
    
    def getTransactionHistory(self):
        return self.__TransactionHistory
    
    def setUsers(self,UsersObj):
        self.__Users = UsersObj
    
    def processDebtSummaryForUserPair(self,User1ID,User2ID):

        user1_details = (self.__Users)[User1ID]
        user2_details = (self.__Users)[User2ID]

        if User1ID in user2_details.getDuesDetails():
            amount_to_be_given_by_user1_to_user2 = user2_details.getDuesDetails()[User1ID]
        else:
            amount_to_be_given_by_user1_to_user2 = 0

        if User2ID in user1_details.getDuesDetails():
            amount_to_be_given_by_user2_to_user1 = user1_details.getDuesDetails()[User2ID]
        else:
            amount_to_be_given_by_user2_to_user1 = 0

        if amount_to_be_given_by_user2_to_user1 == amount_to_be_given_by_user1_to_user2:
            self.__Users[User1ID] = user1_details.removeUserFromDebtList(User2ID)
            self.__Users[User2ID] = user2_details.removeUserFromDebtList(User1ID)

            del self.__DebtSummary[User1ID]
            del self.__DebtSummary[User2ID]

        elif amount_to_be_given_by_user1_to_user2 > amount_to_be_given_by_user2_to_user1:
            diff = amount_to_be_given_by_user1_to_user2 - amount_to_be_given_by_user2_to_user1
            (self.__Users[User1ID]).removeUserFromDebtList(User2ID)
            (self.__Users[User2ID]).setDues(User1ID,diff,IsSummary=True)        

            if User2ID in self.__DebtSummary and User1ID in self.__DebtSummary[User2ID]:
                del self.__DebtSummary[User2ID][User1ID]

            if User1ID in self.__DebtSummary:
                self.__DebtSummary[User1ID][User1ID] = diff
            else:
                self.__DebtSummary[User1ID] = {User2ID:diff}

        else:
            diff = amount_to_be_given_by_user2_to_user1 - amount_to_be_given_by_user1_to_user2
            (self.__Users[User2ID]).removeUserFromDebtList(User1ID)
            (self.__Users[User1ID]).setDues(User2ID,diff,IsSummary=True)        

            if User1ID in self.__DebtSummary and User2ID in self.__DebtSummary[User1ID]:
                del self.__DebtSummary[User1ID][User2ID]

            if User2ID in self.__DebtSummary:
                self.__DebtSummary[User2ID][User1ID] = diff
            else:
                self.__DebtSummary[User2ID] = {User1ID:diff}
    
    def process_transaction(self,actingUserID, forUserID, Amount):
        obj = self.__Users[actingUserID]
        obj.setDues(forUserID,Amount)
        self.processDebtSummaryForUserPair(actingUserID,forUserID)   
