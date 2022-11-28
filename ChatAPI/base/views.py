from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User
from .serializers import MessageSerializer
from .models import Message
from django.contrib.auth import logout
# Create your views here.



# Register
@api_view(['POST'])
def register(request):
    # add an input validator, if the input is valid proceed to create the user 
    User.objects.create_user(username=request.data['username'],email= request.data['email'],password= request.data['password'])
    print(request.data['username'])
    print(request.data['email'])
    print(request.data['password'])
    return Response({'message':'User Registered'})



#Logout
@api_view(["POST"])
def Logout(request):
    print(request.user)
    logout(request)
    return Response({'message' : 'Logged Out'})




# Write message
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request):
    try:
        reciver = User.objects.get(email=request.data['reciver'])
    except:
        return Response({'Error':' user matching query does not exist.'}) 
    Message.objects.create(
        sender=request.user,
        reciver=reciver,
        subject=request.data['subject'],
        details=request.data['details'])
    return Response({'message : Message Posted'})





# Get all messages for a specific user (the logged user)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_messages(request):
<<<<<<< HEAD
    message = Message.objects.filter(sender=request.user.id)
=======
    message = Message.objects.filter(reciver=int(request.user.id))
>>>>>>> 9e53af29e67d5e20dc1550b5b2d50400196bfafd
    serializer = MessageSerializer(message, many=True)
    return Response(serializer.data)





# Get all unread messages for a specific user (the logged user)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_unread_user_messages(request):
    unread_message = Message.objects.filter(sender=request.user.id, read=False)
    serializer = MessageSerializer(unread_message, many=True)
    return Response(serializer.data)
   




# Read message (return one message)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def read_message(request):
    message_id = request.data['message_id']
    try:
        select_message = Message.objects.get(id=message_id, reciver=request.user.id)  
    except:
        return Response({'Error':' Message matching query does not exist.'}) 
    
    select_message.read = True
    select_message.save()
    return Response({'message' : 'Marked as Read'})



# Delete message (as owner or as receiver)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_message(request):
    message_id = request.data['id']
    message = Message.objects.get(id=message_id)
    sender = message.sender
    reciver = message.reciver

    if request.user.id == sender.id:
        print(request.user.id == sender.id)
        message.delete()
        return Response({'message' : 'Message Deleted'})

    elif request.user.id == reciver.id:
        print(request.user.id == reciver.id)
        message.delete()
        return Response({'message' : 'Message Deleted'})

    else:
        print(sender.id, reciver.id, request.user.id)
        return Response({'Error : you are not the sender or reciver'})
        

# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def delete_message(request):
#     message_id = request.data['id']
#     message = Message.objects.get(id=message_id)
#     message.delete()
#     print(message)
#     return Response({'message' : 'Message Deleted'})



# Endpoints to use the API
@api_view(['GET'])
def endpionts(request):
    data=[
        '/register',
        '/login',
        '/logout',
        '/send_message',
        '/read_message',
        '/get_user_messages',
        '/get_unread_user_messages',
        '/delete_message',
        ]
    return Response (data)









