from db.user_db import UserDb

class User:
    def __init__(self,name, family, hourly_rate, total_hour, total_minute, id=None):
        self.name = name
        self.family = family
        self.hourly_rate = hourly_rate
        self.total_hour = total_hour
        self.total_minute = total_minute
        self.salary = self.calc_salary()
        self.id = id


    def full_name(self):
        return ' '.join([self.name, self.family])

    def calc_salary(self):
        total_hour = (self.total_minute / 60) + self.total_hour
        salary = int(total_hour * self.hourly_rate)

        return salary
    
    def get_all_users(self, rows):
        all_users = []
        for row in rows:
            user_id, name, family, role, hourly_rate, total_hour, total_minute, _ = row
            if role == 'Developer':
                user = Developer(name, family, hourly_rate, total_hour, total_minute)
            elif role == "Manager":
                user = Manager(name, family, hourly_rate, total_hour, total_minute)

            user.id = user_id
            all_users.append(user)
        
        return all_users
    
    def __repr__(self):
        return f"<({self.id}){self.name} - {self.family} - {self.hourly_rate} - {self.salary}>"
    

            
class Developer(User):
    def __init__(self, name, family, hourly_rate, total_hour, total_minute):
        super().__init__(name, family, hourly_rate, total_hour, total_minute)
        self.role = 'Developer'

    

class Manager(User):
    def __init__(self, name, family, hourly_rate, total_hour, total_minute):
        super().__init__(name, family, hourly_rate, total_hour, total_minute)
        self.role = 'Manager'




# dev1 = Developer('hassan', 'hassani', 200000, 12, 30)
# print(dev1.full_name())
# print(dev1.calc_salary())

# cost1 = Cost('rent', 'additional cast', 5000000)
# print(cost1)
# print(cost1.date_added)

# user = User('hassan', 'hassani', 200000, 12, 30)
# print(getattr(user, 'role'))
# print(help(user))

userdb = UserDb()

# userdb.init_db()
manager1 = Manager('hassan', 'mahdi', 500000, 10, 4)
dev1 = Developer('saeed', 'nazari', 2000000, 12, 43)
# userdb.delete(manager1)
userdb.delete(1)
rows = userdb.fetch_all()
print(rows)
# print(dev1.get_all_users(rows))



