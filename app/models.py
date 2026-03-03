from flask_login import UserMixin
from email_validator import validate_email,EmailNotValidError
from werkzeug.security import generate_password_hash, check_password_hash
class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data["_id"])
        self.name = user_data["name"]
        self.email = user_data["email"]
        self.hash = user_data["hash"]
    def __str__(self):
        return f"Username: {self.name} and email:{self.email}"
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,value):
        try:
            email_info = validate_email(value, check_deliverability=False)
            self._email = email_info.normalized  
        except EmailNotValidError as e:
            raise ValueError(str(e))
def passwordvalid(password):
        upperflag=0
        lowerflag=0
        specialflag=0
        lenthflag=0
        for s in password:
            if s.isupper():
                upperflag=1
            elif s.islower():
                lowerflag=1
            elif s.isspace():
                raise ValueError("Password cannot have blank space")
            elif s in ['@','_','-']:
                specialflag=1
        if len(password) >=6:
            lenthflag=1
        if upperflag+lowerflag+specialflag+lenthflag !=4:
            raise ValueError("Password must have at least 6 characters and at least 1 lower 1 upper 1 special[@,_,-]")
        return True