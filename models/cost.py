import datetime

class Cost:
    def __init__(self, title, category, amount):
        self.title = title
        self.category = category
        self.amount = amount
        self.date_added = datetime.datetime.now()

    def __str__(self):
        return f'{self.title} - {self.amount}'