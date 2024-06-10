# your User class goes here
class User:
    def __init__(self, name, email=None, driver_license=None):
        self.name = name 
        self.email = email
        self.drivers_license = driver_license

UserBob = ("Bob", "bob@email.com", 12345)
UserClint = ("Clint", "Clint@email.com", 67890)
UserSherly = ("Sherly", "Sherly@email.com", "09876")            