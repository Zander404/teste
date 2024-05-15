from ninja import ModelSchema
from .models import User


class UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ['username', 'email']
        read_only_fields = ['username', 'email']


class LoginSquema(ModelSchema):
    class Config:
        model = User
        model_fields = ['email', 'password']
        read_only_fields = ['email','password']