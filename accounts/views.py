#from django.http import HttpResponse


# Create your views here.
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

# def signup(request):
#     if request.method == "POST":
#         fullname = request.POST['fullname']
#         email = request.POST['email']
#         username = request.POST['username']
#         password = request.POST['password']

#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password,
#             first_name=fullname
#         )
#         user.save()
#         return redirect('login')

#     return render(request, 'signup.html')

# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('dashboard')
#         else:
#             return render(request, 'signin.html', {'error': 'Invalid credentials'})

#     return render(request, 'signin.html')

# from django.contrib.auth.decorators import login_required

# @login_required
# def delete_account(request):
#     request.user.delete()
#     return redirect('signup')

# def logout_user(request):
#     logout(request)
#     return redirect('signin')


# import json
# from django.http import JsonResponse
# # from rest_framework.decorators import api_view
# # from rest_framework.response import Response
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from .serializers import (
#     UserSignupSerializer,
#     UserSigninSerializer,
#     UserUpdateSerializer
# )


# # from django.http import JsonResponse, HttpResponse
# # from django.contrib.auth.models import User
# # from django.contrib.auth import authenticate, login, logout
# # import json

# def signup(request):
#     if request.method == "POST":
#         data = json.loads(request.body)

#         username = data.get("username")
#         password = data.get("password")
#         email = data.get("email")
#         full_name = data.get("full_name")

#         if User.objects.filter(username=username).exists():
#             return JsonResponse({"error": "Username already exists"}, status=400)

#         user = User.objects.create_user(
#             username=username,
#             password=password,
#             email=email,
#             full_name=full_name
#         )

#         return JsonResponse({"message": "User Created Successfully"})

# def signin(request):
#     if request.method == "POST":
#         data = json.loads(request.body)

#         username = data.get("username")
#         password = data.get("password")

#         user = authenticate(username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return JsonResponse({"message": "Login Successful"})
#         else:
#             return JsonResponse({"error": "Invalid Credentials"}, status=401)

# def update_user(request):
#     if request.method == "PUT":
#         data = json.loads(request.body)

#         username = data.get("username")

#         try:
#             user = User.objects.get(username=username)
#             user.email = data.get("email", user.email)
#             user.full_name = data.get("full_name", user.full_name)
#             user.save()

#             return JsonResponse({"message": "User Updated Successfully"})
#         except User.DoesNotExist:
#             return JsonResponse({"error": "User not found"}, status=404)

# def delete_user(request):
#     if request.method == "DELETE":
#         data = json.loads(request.body)
#         username = data.get("username")

#         try:
#             user = User.objects.get(username=username)
#             user.delete()
#             return JsonResponse({"message": "User Deleted Successfully"})
#         except User.DoesNotExist:
#             return JsonResponse({"error": "User not found"}, status=404)

# def logout_user(request):
#     logout(request)
#     return JsonResponse({"message": "Logged Out Successfully"})

# from django.http import HttpResponse, JsonResponse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt
# import json

# from .serializers import (
#     UserSignupSerializer,
#     UserSigninSerializer,
#     UserUpdateSerializer
# )
# # Django uses a CSRF token:
# # A secret token added to forms
# # Server checks this token for POST / PUT / DELETE requests
# # If token is missing → request rejected

# @csrf_exempt
# def signup(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         serializer = UserSignupSerializer(data=data)
#         print("datais",data)

#         if serializer.is_valid():
#             serializer.save()
#             return HttpResponse({"message": "User Created Successfully"}, status=201)
#         else:
#             return HttpResponse(serializer.errors, status=400)

# @csrf_exempt
# def signin(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         serializer = UserSigninSerializer(data=data)

#         if serializer.is_valid():
#             user = authenticate(
#                 username=serializer.validated_data['username'],
#                 password=serializer.validated_data['password']
#             )

#             if user:
#                 login(request, user)
#                 return JsonResponse({"message": "Login Successful"})
#             return JsonResponse({"error": "Invalid Credentials"}, status=401)

#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def update_user(request):
#     if request.method == "PUT":
#         data = json.loads(request.body)

#         try:
#             user = User.objects.get(username=data.get("username"))
#         except User.DoesNotExist:
#             return JsonResponse({"error": "User not found"}, status=404)

#         serializer = UserUpdateSerializer(user, data=data, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({"message": "User Updated Successfully"})

#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def delete_user(request):
#     if request.method == "DELETE":
#         data = json.loads(request.body)

#         try:
#             user = User.objects.get(username=data.get("username"))
#             user.delete()
#             return JsonResponse({"message": "User Deleted Successfully"})
#         except User.DoesNotExist:
#             return JsonResponse({"error": "User not found"}, status=404)

# def logout_user(request):
#     logout(request)
#     return JsonResponse({"message": "Logged Out Successfully"})


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth import authenticate, login, logout

@api_view(['GET'])  #reading/getting/retrieving data(read)
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many= True)
    return Response(serializer.data)
     
@api_view(['POST'])    #creating/posting/inserting data(create)
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':          #to find specific user by their primary key or id
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':      #updating/modifying data(complete update = PUT  ,  partial update = PATCH)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':      #deleting/removing data
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['POST'])
# def create_user(request):
#     serializer = UserSigninSerializer(data = request.data)


