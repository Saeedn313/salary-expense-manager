import datetime
from db import UserDb

class User:
    def __init__(self, name, family, hourly_rate, total_hour, total_minute):
        self.name = name
        self.family = family
        self.hourly_rate = hourly_rate
        self.total_hour = total_hour
        self.total_minute = total_minute


    def full_name(self):
        return ' '.join([self.name, self.family])

    def calc_salary(self):
        total_hour = (self.total_minute / 60) + self.total_hour
        salary = int(total_hour * self.hourly_rate)

        return salary

class Developer(User):
    def __init__(self, name, family, hourly_rate, total_hour, total_minute):
        super().__init__(name, family, hourly_rate, total_hour, total_minute)
        self.role = 'Developer'

class Manager(User):
    def __init__(self, name, family, hourly_rate, total_hour, total_minute):
        super().__init__(name, family, hourly_rate, total_hour, total_minute)
        self.role = 'Manager'


class Cost:
    def __init__(self, title, category, amount):
        self.title = title
        self.category = category
        self.amount = amount
        self.date_added = datetime.datetime.now()

    def __str__(self):
        return f'{self.title} - {self.amount}'

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
userdb.init_db()

# dev1 = Developer('saeed', 'nazari', 2000000, 12, 43)
# print(dev1)
# userdb.add_user(dev1)

