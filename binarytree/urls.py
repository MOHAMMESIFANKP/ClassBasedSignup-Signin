from django.urls import path
from .views import *

urlpatterns = [
    path('', UsersList.as_view(), name='UsersList'),
    path('form', SubmitForm.as_view(), name='SubmitForm'),
    path('signup/', Signup.as_view(), name='Signup'),
    path('signin/', Signin.as_view(), name='Signin'),
    path('signout/', signout.as_view(), name='signout'),
    path('search/', SearchUsersView.as_view(), name='search_users'),
    
]
