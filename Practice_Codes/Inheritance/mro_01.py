class Boss:
    def report(self):
        print("Boss")

class Manager1(Boss):
    def report(self):
        print("Manager1 : Report to Boss")

class Manager2(Boss):
    def report(self):
        print("Manager1 : Report to Boss")

class TeamLead1(Manager2,Manager1):
    def report(self):
        print("TeamLead1 : Report to Manager1")

class TeamLead2(Manager2,Manager1):
    def report(self):
        print("TeamLead1 : Report to Manager1")
        
class Developer(TeamLead2,TeamLead1):
    def report(self):
        print("TeamLead1 : Report to Manager1")

print(Developer.__mro__)