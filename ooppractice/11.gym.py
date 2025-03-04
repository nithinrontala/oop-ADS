class Member:
    def __init__(self,id,name,type):
        self.memberID = id
        self.name = name
        self.membershipType = type

    def MemberInfo(self):
        return f"ID: {self.memberID}, name: {self.name}, type: {self.membershipType}"
    
class MembershipPlan:
    def __init__(self,pid,pname,fee):
        self.planID = pid
        self.name = pname
        self.fee = fee

    def getPlanDetails(self):
        return f"name: {self.name}, fee: {self.fee}, planid: {self.planID}"

class Gym:
    def __init__(self,m,plan):
        self.members = m
        self.plans = plan

    def registerMember(self,m):
        self.members.append(m)

    def assignPlan(self,mid,pid):
        for i in self.members:
            if i.memberID == mid:
                i.planID = pid
                return True
        return False
    
def main():
# Create members and membership plans
    member1 = Member(1, "David", "monthly")
    member2 = Member(2, "Linda", "yearly")
    plan1 = MembershipPlan(101, "Standard", 50.0)
    plan2 = MembershipPlan(102, "Premium", 80.0)
    gym = Gym([], [])
    gym.registerMember(member1)
    gym.registerMember(member2)
    # Test assigning membership plans
    assign1 = gym.assignPlan(member1.memberID, plan1.planID)
    assign2 = gym.assignPlan(member2.memberID, plan2.planID)
    print("Plan assigned to David:", assign1)
    print("Plan assigned to Linda:", assign2)
    # Attempt assignment for a non-existent member
    assign_invalid = gym.assignPlan(999, plan1.planID)
    print("Plan assignment to non-existent member:", assign_invalid)
if __name__ == '__main__':
    main()