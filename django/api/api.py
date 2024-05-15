from typing import List
import json, jwt

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, HttpResponse

from ninja import NinjaAPI
from .models import User
from .squemas import UserSchema, LoginSquema

api = NinjaAPI(version='API_STOCK')



@api.post('login/', tags=['Login'])
def login(request, login_data: LoginSquema):
    user = get_object_or_404(User, email=login_data.email)
    
    if user.password == login_data.password:
       response_data = [{'msg': 'Login'}]
       return HttpResponse( content=json.dumps(response_data), content_type='application/json', status=200)

    else:
        response_data = [{'msg': 'Usuário ou Senha Inválidas'}]
        return HttpResponse( content=json.dumps(response_data), content_type='application/json', status=403)

    

@api.get('user/', response=List[UserSchema], tags=['User'])
def list(request):
    return User.objects.all()

