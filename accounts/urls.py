# from django.urls import path
# from . import views

# urlpatterns = [
#     path('signup/', views.signup, name='signup'),
#     path('signin/', views.login, name='signin'),
#     path('logout/', views.logout_user, name='logout'),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('signup/', views.signup, name='signup'),
#     path('signin/', views.signin, name='signin'),
#     path('update/', views.update_user, name='update_user'),
#     path('delete/', views.delete_user, name='delete_user'),
#     path('logout/', views.logout_user, name='logout'),
# ]

from django.urls import path
from .views import get_users,create_user,user_detail 
#from .views import signup, signin, update_user, delete_user, logout_user


urlpatterns = [
    path('users/', get_users, name = 'get_users'),
    path('users/create/', create_user, name = 'create_user'),
    path('users/<int:pk>/', user_detail, name = 'user_detail')
]
