import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from splitwise.models.users import User
from splitwise.services.dashboard import DashBoard

class Splitwise:

    def __init__(self):
        pass
    
    def start_application(self):

        User1 = User('u1',"Pradeep",'p@p.com',787878787878)
        User2 = User('u2',"Prashant",'q@p.com',343434343434)
        User3 = User('u3',"Priyanshu",'d@p.com',676767676767)
        User4 = User('u4',"Prakash",'a@p.com',121212121221)
        UsersObj = {'u1':User1,'u2':User2,'u3':User3,'u4':User4}

        dashboad = DashBoard()
        dashboad.setUsers(UsersObj)

        # print(dashboad.getUsers())

        while True:
            inp_list = list(input().split())

            if inp_list[0] == "STOP":
                break           

            if len(inp_list) == 1 and inp_list[0] == "SHOW":
                dashboad.getDebtSummary()
            elif len(inp_list) == 2 and inp_list[0] == "SHOW":
                dashboad.getDebtSummaryForUser(inp_list[1])
            elif len(inp_list) > 2 and inp_list[0] == 'EXPENSE':
                acting_user = inp_list[1]
                amount_used = float(inp_list[2])
                total_users_involved = int(inp_list[3])

                if inp_list[4+total_users_involved].strip() == 'EQUAL':
                    each_share = amount_used/total_users_involved

                    for i in range(4,4+total_users_involved):
                        if inp_list[i] != acting_user:
                            dashboad.process_transaction(acting_user,inp_list[i],each_share)

                elif inp_list[4+total_users_involved].strip() == 'EXACT':
                    exact_shares = {}
                    for i in range(4,4+total_users_involved):
                        exact_shares[inp_list[i]] = inp_list[i+total_users_involved+1]
                    for userid,share in exact_shares.items():
                        if acting_user != userid:
                            dashboad.process_transaction(acting_user,userid,float(share))

                elif inp_list[4+total_users_involved].strip() == 'PERCENT':
                    byPer_exact_amount = {}
                    for i in range(4,4+total_users_involved):
                        byPer_exact_amount[inp_list[i]] = amount_used*float(inp_list[i+total_users_involved+1])/100
                    for userid,share in byPer_exact_amount.items():
                        if acting_user != userid:
                            dashboad.process_transaction(acting_user,userid,share)

if __name__ == '__main__':
    obj = Splitwise()
    obj.start_application()