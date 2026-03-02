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
