from django.shortcuts import render

from .models import UserMessage
# Create your views here.

def getmessages(request):
    all_messages = UserMessage.objects.filter(name = 'baby',address='焦作')
    # all_messages.delete()
    for message in all_messages:
        message.delete()
        # print(message)
    # if request.method =="POST":
    #     name = request.POST.get('name','')
    #     message = request.POST.get('message','')
    #     address = request.POST.get('address','')
    #     email = request.POST.get('email','')
    #
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.address = address
    #     user_message.message = message
    #     user_message.emile = email
    #     user_message.object_id = "h2"
    #
    #     user_message.save()
    return render(request,'messages.html')
