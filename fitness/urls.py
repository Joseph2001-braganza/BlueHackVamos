from django.urls import path
from .views import Login, SignUp, Index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', Index.as_view(), name='indexpage'),
    path('login', Login.as_view(), name='login'),
    path('signup', SignUp.as_view(), name='signup'),
]