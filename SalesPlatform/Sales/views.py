from django.shortcuts import render
from Sales.models import Users,Contacts
from Sales.serializers import UserSerializer,ContactSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

def base_template(request):
    render(request,'sales/base.html')    

def user_template(request):
    usersdata = Users.users.all()
    serializer = UserSerializer(usersdata, many=True)
    users = serializer.data
    render(request,'sales/users.html',context=users)    

def contacts_template(request):
    contactsdata = Contacts.contacts.all()
    serializer = ContactSerializer(contactsdata, many=True)
    contacts = serializer.data
    render(request,'sales/contacts.html',context=contacts)

# Create your views here.
def user_list(request):
    """
    List all code users, or create a new user.
    """
    if request.method == 'GET':
        users = Users.users.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request.body)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def contact_list(request):
    """
    List all contacts, or create a new contact.
    """
    if request.method == 'GET':
        contacts = Contacts.contacts.all()
        serializer = ContactSerializer(contacts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request.body)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)        