from datetime import datetime


class User:
    def __init__(self, name, email, drivers_license = None, post = "", log = {} ):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license
        self._post = post
        self._log = log
    
    def __str__(self):
        return f'the name of this User is {self.name}, {self.email}, {self.drivers_license}'
    
        
    def make_post(self): 
        check = input("Post y/n?")
        if check.lower() == "y": 
            words = input("post ")
            self.set_post = words
        else:
            return "Have a good day"

    @property
    def get_post(self):
        return self._post
    
    @get_post.setter
    def set_post(self, words):
        if isinstance(words, str):
            format_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self._log.update({format_date:words})

        else:
            "Wrong Format"


    @get_post.deleter
    def delete_post(self):
        pass
user2 = User("Bob", "Bob@email.com", 4567)
user1 = User("Chris", "chrisr222@gmail.com", 234245436)
user1.make_post()
# your User class goes here
print(f'{user1._log}')
# your improved User class goes here# your improved User class goes here