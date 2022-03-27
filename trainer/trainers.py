
class Trainer:
    def __init__(self, firstname='', lastname=str(), alias=str(), photo=str()):
        self.firstname = firstname
        self.lastname = lastname
        self.alias = alias
        self.photo = photo

    def __str__(self):
        return f"{self.lastname, self.firstname}"
