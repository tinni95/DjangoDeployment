from django.shortcuts import render
from UserApp.models import User

def index(request):
    return render(request,'UserApp/index.html')

def users(request):
    users_list = User.objects.order_by('first_name')
    user_dic ={"users":users_list}
    return render(request,'UserApp/users.html',context=user_dic)
