from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import User,Todo
from .serializers import UserSerializer, TodoSerializer

def hello_world(request):
    return HttpResponse("Hello World. You have built an API.")

def add(request):
    print(request.GET)
    a=int(request.GET.get("a"))
    b=int(request.GET.get("b"))
    c=a+b
    response = {
        "message":"success",
        "sum":c
    }
    return JsonResponse(response, status=200)
    #return HttpResponse(json.dumps(response))
    
def create_user(request):
    try:
        data=json.loads(request.body) #loads the data in the form of dictionary from the request
        serializer=UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        print(user)
        return JsonResponse(UserSerializer(user).data, status=200)
        # print(data)    
        # fields = ["name", "date_of_birth"]
        
        # for field in fields :
        #     if field not in data.keys():
        #         return JsonResponse({
        #             "message ":field + " is mandatory"
        #         },status=400)
        # User.objects.create(name=data["name"], date_of_birth=data["date_of_birth"])        
        # user=User.objects.get(name=data["name"])
        
        # return JsonResponse({
        #     "name":user.name,
        #     "id": user.id,
        #     "date_of_birth": user.date_of_birth,    
        # }, status = 201)
    except Exception as e:
         return JsonResponse({
            "error":e.__str__() 
         },status=400)   
            
def get_user(request):
    try:
        user_id=int(request.GET.get("id"))
        user=User.objects.get(pk=user_id)
        return JsonResponse({
            "name":user.name,
            "id": user.id,
            "date_of_birth": user.date_of_birth,    
        }, status = 200)
    except Exception as e:
         return JsonResponse({
            "error":e.__str__() 
         },status=404)  
         
def add_todo(request):
    try:
        data=json.loads(request.body)
        serializer=TodoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        todo=serializer.save()
        return JsonResponse(TodoSerializer(todo).data,status=201)
        
    except Exception as e:
         return JsonResponse({
            "error":e.__str__() 
         },status=400)
         
def get_todo(request):
    try :
        todo_id=int(request.GET.get("id"))
        todo=Todo.objects.get(pk=todo_id)
        return JsonResponse(TodoSerializer(todo).data,status=200)
    except Exception as e:
         return JsonResponse({
            "error":e.__str__() 
         },status=404)      
                                
# Create your views here.
